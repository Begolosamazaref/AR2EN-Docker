from flask import Flask, request, jsonify
from transformers import MarianMTModel, MarianTokenizer
import uuid
from threading import Thread
from time import sleep

app = Flask(__name__)

# Model and tokenizer initialization
MODEL_NAME = "Helsinki-NLP/opus-mt-ar-en"
tokenizer = None
model = None

tasks = {}

def load_model():
    global tokenizer, model
    tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)
    model = MarianMTModel.from_pretrained(MODEL_NAME)

def translate_async(task_id, text):
    """Perform translation asynchronously."""
    sleep(2)  # Simulate processing time
    translation = model.generate(**tokenizer(text, return_tensors="pt", padding=True))
    result = tokenizer.decode(translation[0], skip_special_tokens=True)
    tasks[task_id]['status'] = 'completed'
    tasks[task_id]['result'] = result

@app.route('/translate/ar2en', methods=['POST'])
def translate():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Invalid input. Provide "text".'}), 400

    text = data['text']
    task_id = str(uuid.uuid4())
    tasks[task_id] = {'status': 'processing', 'result': None}

    # Start translation in a separate thread
    thread = Thread(target=translate_async, args=(task_id, text))
    thread.start()

    return jsonify({'task_id': task_id}), 202

@app.route('/translate/ar2en/status/<task_id>', methods=['GET'])
def get_status(task_id):
    if task_id not in tasks:
        return jsonify({'error': 'Task ID not found'}), 404

    return jsonify(tasks[task_id])

if __name__ == '__main__':
    load_model()  # Initialize the model and tokenizer here
    app.run(host='0.0.0.0', port=5000)

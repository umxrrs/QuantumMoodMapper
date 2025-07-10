from flask import Flask, jsonify
from cogs.audio_analyzer import AudioAnalyzer
from cogs.mood_predictor import MoodPredictor
from cogs.art_generator import ArtGenerator
import requests
import json
import os

application = Flask(__name__)
audio_analyzer = AudioAnalyzer()
mood_predictor = MoodPredictor()
art_generator = ArtGenerator()

with open('config.json', 'r') as f:
    configuration = json.load(f)

@application.route('/api/mood', methods=['GET'])
def get_mood():
    audio_data = audio_analyzer.capture_audio()
    features = requests.post(config['audio_processor_url'], json={'audio': audio_data.tolist()}).json()['features']
    mood = mood_predictor.predict(features)
    return jsonify({'mood': mood})

@application.route('/api/art', methods=['GET'])
def get_art():
    audio_data = audio_analyzer.capture_audio()
    features = requests.post(config['audio_processor_url'], json={'audio': audio_data.tolist()}).json()['features']
    mood = mood_predictor.predict(features)
    art_url = art_generator.generate(mood)
    return jsonify({'art_url': art_url})

if __name__ == '__main__":
    os.makedirs(config['art_output_dir'], exist_ok=True)
    app.run(host='0.0.0.0', port=config['api_port'])

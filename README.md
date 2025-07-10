# 🎧 QuantumMoodMapper

**QuantumMoodMapper** is a machine learning-powered application that analyzes **ambient audio** to predict user **mood**, then generates **personalized generative art** based on the prediction.

- 🧠 Built with **Python** (TensorFlow) for mood prediction  
- 🎛️ **Node.js** microservice for real-time audio processing  
- 🎨 Mood-based **generative art creation**  
- 🔗 RESTful API for seamless frontend integration  
- ⚙️ Scalable **microservice architecture**

---

## ✨ Features

- 🎙️ **Real-time ambient audio analysis**
- 😌 **Mood prediction** using a pre-trained ML model
- 🖼️ **Generative art** tailored to your mood
- 🧱 **Scalable microservice architecture**
- 🔗 **RESTful API** for integration with any frontend

---

## 🧰 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10+**
- **Node.js 18+**
- **FFmpeg** (for audio processing)
- **Microphone** (for capturing ambient audio)

---

## ⚙️ Installation
---
### 1. **Clone the repository**
---
```bash
git clone https://github.com/umxrrs/QuantumMoodMapper.git
cd QuantumMoodMapper
```
---
### 2. Set up the Python environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
---
### 3. Set up the Node.js microservice
```bash
cd services/audio-processor
npm install
```
---
### 4. Start the Python backend
```bash
cd ../../src
python main.py
```
---

### 5. Start the Node.js audio processor
```bash
cd services/audio-processor
npm start
```
---

## 🚀 Usage

- Make sure your microphone is active and properly configured.  
- The app will automatically capture ambient audio, predict your mood, and generate personalized art based on the analysis.  
- Access the RESTful API endpoints:

  - **Mood data:** `http://localhost:5000/api/mood`  
  - **Generated art URLs:** `http://localhost:5000/api/art`

---

## License

This project is licensed under the [MIT License](LICENSE).
---

## Credits

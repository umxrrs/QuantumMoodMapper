import librosa
import numpy as np
import sounddevice as sd

class AudioAnalyzer:
    def capture_audio(self, duration=10.0, sampling_rate=44100):
        recording = sd.rec(int(duration * sampling_rate), samplerate=sampling_rate, channels=1)
        sd.wait()
        return np.squeeze(recording)

const Meyda = require('meyda');

module.exports = class AudioProcessor {
    constructor(audioData) {
        this.audioData = audioData;
        this.meyda = Meyda.createMeydaAnalyzer({
            audioContext: new AudioContext(),
            source: { get: () => this.audioData },
            bufferSize: 512,
            featureExtractors: ['rms', 'spectralCentroid', 'mfcc']
        });
    }

    extractFeatures() {
        return this.meyda.get();
    }
}

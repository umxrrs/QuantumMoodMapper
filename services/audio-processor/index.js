const express = require('express');
const MeydaProcessor = require('./audioProcessor.js');
const app = express();

app.use(express.json());

app.post('/process', (req, res) => {
    const audioData = req.body.audio;
    const processor = new MeydaProcessor(audioData);
    const features = processor.extractFeatures();
    res.json({features: features});
});

app.listen(3001, () => console.log('Audio processor running on port 3001));

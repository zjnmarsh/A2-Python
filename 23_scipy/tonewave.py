import numpy as np
import scipy.io.wavfile
samplingRate, soundSamples = scipy.io.wavfile.read('tone.wav')
soundSamplesNew = []
for i in range(len(soundSamples)):
    if (i % 2) == 0:
        soundSamplesNew.append(soundSamples[i])
soundSamplesNew = np.asarray(soundSamplesNew)
scipy.io.wavfile.write('ToneFreqDoubled.wav', samplingRate, soundSamplesNew)


import math
import wave
import array

def createSine(  freq=440,length = 3 ,volume = .85, sampleRate =44100) :
 sin = math.sin
 pi = math.pi
 twopi = 2*pi
 data = array.array('h')
 numSamples = int(length * sampleRate)
 cyclesPerSample = float(freq)/sampleRate
 volumeScale = (.85)*32767

 for samp in xrange(numSamples):
    phi = samp * cyclesPerSample
    phi -= int(phi)
    
    data.append(int(round(volumeScale * sin(twopi * phi))))
 return  data

f = wave.open('biWave.wav', 'w')
f.setparams((1, 2, 44100, 0, "NONE", "Uncompressed"))
for i in range(16):
	set = createSine(1200, 0.03) 
	f.writeframes(set.tostring())
	set = createSine(2200, 0.03) 
	f.writeframes(set.tostring())
f.close()

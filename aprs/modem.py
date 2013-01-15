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

f = wave.open('modem.wav', 'w')
f.setparams((1, 2, 44100, 0, "NONE", "Uncompressed"))
fh = open('message.txt', "rb")
b = 1
while b:
 b = fh.read(1)
 if b == '0': 
    set = createSine(1200, 0.00083) 
    f.writeframes(set.tostring())
    print set
 else:
    set = createSine(2200, 0.00083) 
    f.writeframes(set.tostring())
    print set
f.close()

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
 volumeScale = volume*32767

 for samp in xrange(numSamples):
  phi = samp * cyclesPerSample
  phi -= int(phi)
  data.append(int(round(volumeScale * sin(twopi * phi))))
 return  data

CODE = {'A': '13',     'B': '3111',   'C': '3131', 
        'D': '311',    'E': '1',      'F': '1131',
        'G': '331',    'H': '1111',   'I': '11',
        'J': '1333',   'K': '313',    'L': '1311',
        'M': '33',     'N': '31',     'O': '333',
        'P': '1331',   'Q': '3313',   'R': '131',
      'S': '111',    'T': '3',      'U': '113',
        'V': '1113',   'W': '133',    'X': '3113',
        'Y': '3133',   'Z': '3311',
        
        '0': '33333',  '1': '13333',  '2': '11333',
        '3': '11133',  '4': '11113',  '5': '11111',
        '6': '31111',  '7': '33111',  '8': '33311',
        '9': '33331',  ' ': 's', 
        }

def main():
 msg = 'hello world'
 out = ''
 for char in msg:
  out += CODE[char.upper()] + 'b'
 print out
 f = wave.open('morse.wav', 'w')
 f.setparams((1, 2, 44100, 0, "NONE", "Uncompressed"))
 b = 1
 for b in out:
  if b == '1':
   set = createSine(700, 0.12)
   f.writeframes(set.tostring())
   set = createSine(0, 0.12)
   f.writeframes(set.tostring())
  elif b == '3':
   set = createSine(700, 0.36)
   f.writeframes(set.tostring())
   set = createSine(0, 0.12)
   f.writeframes(set.tostring())
  elif b == 'b':
   set = createSine(0, 0.36)
   f.writeframes(set.tostring())
  elif b == 's':
   set = createSine(0, 0.48)
   f.writeframes(set.tostring())
  else:
   set = createSine(0, 0.12)
   f.writeframes(set.tostring())
 f.close()
  
if __name__ == "__main__":
 main()


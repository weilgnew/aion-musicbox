from pyaudio import PyAudio
import wave
import sys
import math
import random
from scipy.io import wavfile
import numpy as np

# notes hold the dictionary to frequency of different notes
note=[]

# Import the note's frequency data
count = 0
filename = 'note_frequency.txt'
with open(filename) as file_note:
    for line in file_note:
        note_freq = line.split('\t')
        note.append((note_freq[0], float(note_freq[1])))
        #count = count + 1

file_note.close()

# Melody generation algorithm
# Functions to define the movement of the melody

def root_next():
    x = random.normalvariate(3.5, 1)
    if x > 3.5 and x <= 4.5:
        return 5
    if x >= 2.5 and x <= 3.5:
        return 4
    if x >= 1.8 and x <= 5.2:
        return 6
    if x < 1.8:
        return 2
    if x > 5.2:
        return 3

def second_next():
    x = random.normalvariate(3.5, 1)
    if x >= 2.7 and x <= 4.3:
        return 5
    if x >= 2 and x < 2.7:
        return 4
    if x > 4.3 and x <= 5 :
        return 6
    if x < 2:
        return 1
    if x > 5:
        return 3

def third_next():
    x = random.normalvariate(3.5, 1)
    if x >= 2.7 and x <= 4.3:
        return 6
    if x >= 2 and x < 2.7:
        return 4
    if x > 4.3 and x <= 5 :
        return 5
    if x < 2:
        return 1
    if x > 5:
        return 2

def fourth_next():
    x = random.normalvariate(3.5, 1)
    if x >= 2.7 and x <= 4.3:
        return 5
    if x >= 2 and x < 2.7:
        return 1
    if x > 4.3 and x <= 5 :
        return 2
    if x < 2:
        return 3
    if x > 5:
        return 6

def fifth_next():
    x = random.normalvariate(3.5, 1)
    if x >= 2.7 and x <= 4.3:
        return 1
    if x >= 2 and x < 2.7:
        return 4
    if x > 4.3 and x <= 5 :
        return 6
    if x < 2:
        return 2
    if x > 5:
        return 3

def sixth_next():
    x = random.normalvariate(3.5, 1)
    if x > 3.5 and x <= 4.5:
        return 2
    if x >= 2.5 and x <= 3.5:
        return 5
    if x >= 1.5  and x < 2.5:
        return 3
    if x > 4.5 and x <= 5.5 :
        return 4
    if x < 1.5 or x > 5.5 :
        return 1

def seventh_next():
    x = random.normalvariate(3.5, 1)
    if x > 3.5 and x <= 4.5:
        return 1
    if x >= 2.5 and x <= 3.5:
        return 3
    if x >= 1.8 and x <= 5.2:
        return 6
    if x >= 1.2 and x <= 5.8:
        return 2
    if x < 1.2:
        return 4
    if x > 5.8:
        return 5

# Generate the melody with function
melody = [5]
print(melody[0])
length = 50
for i in range(1, length):
    print(i)
    if melody[i-1] == 1:
        melody.append(root_next())
    if melody[i-1] == 2:
        melody.append(second_next())
    if melody[i-1] == 3:
        melody.append(third_next())
    if melody[i-1] == 4:
        melody.append(fourth_next())
    if melody[i-1] == 5:
        melody.append(fifth_next())
    if melody[i-1] == 6:
        melody.append(sixth_next())
    if melody[i-1] == 7:
        melody.append(seventh_next())
    
print(melody)

# Play the melody

volume=10
sample_rate = 22050
duration = 0.5

# Set the root
root = 37

n_samples = int(sample_rate*duration)

samples = []
music = []
# Create the melody array
for i in range(0, length):
    if melody[i] == 1:
        play = 0
    if melody[i] == 2:
        play = 2
    if melody[i] == 3:
        play = 4
    if melody[i] == 4:
        play = 5
    if melody[i] == 5:
        play = 7
    if melody[i] == 6:
        play = 9
    if melody[i] == 7:
        play = 11
        
    s = lambda t: volume * np.sin(2 * 3.142 * note[root+play][1] * t / sample_rate)
    for t in xrange(n_samples):
        samples.append(int(s(t) * 127 + 128))

samples2 = np.asarray(samples)
wavfile.write('wave_test.wav', sample_rate, samples2.astype(np.dtype('i2')))





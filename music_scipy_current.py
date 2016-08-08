import random
from scipy.io import wavfile
import numpy as np
from waveform_generator import waveform_gen_exp
from chord_gen import chord_maj_gen

##############################################################################################################################
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

##############################################################################################################################
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
        
###########################################################################################################################
# Set the parameters
# Generation of the melody
melody = [1]
print(melody[0])
length = 50     # set the melody length
root = 36       # set the melody root note
volume=15       # set the volume, self explanatory I believe 
sample_rate = 22050 # sampling rate for the wav file, rule of thumb: the upper frequency is half of sampling rate
tempo = 20      # how long for one bar, in sec 
bar = 10        # how many bar, not the one with liquor

############################################################################################################################
# Yes, this is where it generates the melody, or movement, progression
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
    
# Just to let you know the progresion
print(melody)

samples = [] # what is this for? I forgot. Check if it is needed, if not just delete it

##############################################################################################################################
# beat generator, it doesnt need to be here, best is in another function or file. Well,  when I have time
beat = []
for i in range(0,100):
    if i%2 == 0:
        beat.append(1)
        beat.append(0.5)
        beat.append(1)
        beat.append(0.5)
        beat.append(0.25)
        beat.append(0.25)


    else:
        beat.append(0.5)
        beat.append(0.5)

#beat = [0.5]*51
#print(beat)

#############################################################################################################################
# Create the melody array
for i in range(0, length):
    if melody[i] == 1:
        melody[i] = 0 + root
    if melody[i] == 2:
        melody[i] = 2 + root
    if melody[i] == 3:
        melody[i] = 4 + root
    if melody[i] == 4:
        melody[i] = 5 + root
    if melody[i] == 5:
        melody[i] = 7 + root
    if melody[i] == 6:
        melody[i] = 9 + root
    if melody[i] == 7:
        melody[i] = 11 + root

print(melody)
piece = chord_maj_gen(root, melody)


# generate the waveform with waveform_gen function
samples = waveform_gen_exp(bar, tempo, sample_rate, piece, beat)

##############################################################################################################################
# generate the wav file
samples2 = np.asarray(samples)
wavfile.write('wave_test0608.wav', sample_rate, samples2.astype(np.dtype('i2')))





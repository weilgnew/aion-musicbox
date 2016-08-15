from scipy.io import wavfile
import numpy as np
import datetime
from waveform_generator import waveform_gen_exp
from chord_gen import chord_maj_ran_gen
from chord_gen import chord_maj_gen_2
from melody_gen import melody_gen_sim
from beat_gen import beat_gen_sim
from beat_gen import beat_gen_chord_2

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

        
###########################################################################################################################
# Set and intialise the parameters
# Generation of the melody
melody = [1]
length = 60     # set the melody length
root = 40       # set the melody root note
volume = 15       # set the volume, self explanatory I believe 
sample_rate = 22050 # sampling rate for the wav file, rule of thumb: the upper frequency is half of sampling rate
tempo = 0.125      # fastest speed for one note, in sec 
bar = 10        # how many bar, not the one with liquor
beat = None        # variable for beat generation (discrete)
beat_time = None   # variable for beat generation (duration)
piece = None       # variable for final piece
samples = None     # variable for wave generation (raw)
samples2 = None    # variable for wave generation (processed)
nowdate = None     # variable for obtaining current date (for saving)


############################################################################################################################
# Yes, this is where it generates the melody, or movement, progression

melody = melody_gen_sim(length)
    
# Just to let you know the progresion
print(melody)


##############################################################################################################################
# beat generator, it doesnt need to be here, best is in another function or file. Well,  when I have time

beat = beat_gen_chord_2(length)

beat_time = [i * tempo for i in beat] # convert every component from beat count to real time duration

#############################################################################################################################
# Convert the melody into semitone count
for i in range(0, len(melody)):
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
piece = chord_maj_gen_2(root, melody)

print(piece)
# generate the waveform with waveform_gen function
samples = waveform_gen_exp(bar, tempo, sample_rate, piece, beat_time)

##############################################################################################################################
# generate the wav file
samples2 = np.asarray(samples)
#generate date for saving
nowdate = datetime.datetime.now()
wavfile.write('%d_%d_%dt%d.%d.%dwave_test.wav' %(nowdate.year, nowdate.month, nowdate.day, nowdate.hour, nowdate.minute, \
                nowdate.second), sample_rate, samples2.astype(np.dtype('i2')))

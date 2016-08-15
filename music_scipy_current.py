from scipy.io import wavfile
import numpy as np
import datetime
from waveform_gen import waveform_gen_exp
from waveform_gen import waveform_gen_exp_short
from waveform_gen import waveform_gen_new
from waveform_gen import waveform_gen_new_2
from chord_gen import chord_maj_ran_gen
from chord_gen import chord_maj_gen_2
from progression_gen import prog_gen_sim
from beat_gen import beat_gen_ran
from beat_gen import beat_gen_ran_2
from beat_gen import beat_gen_ran_3
from beat_gen import beat_gen_chord_2
from beat_gen import beat_gen_ran_bar
from melody_gen import melody_gen_1

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
# Set the parameters
# Generation of the melody
# Total piece length is determine by number of bar
progression = [1]
root = 60       # set the progression root note
volume = 15       # set the volume, self explanatory I believe 
sample_rate = 22050 # sampling rate for the wav file, rule of thumb: the upper frequency is half of sampling rate
tempo = 0.2      # minimum spacing between notes, in second
beats_per_bar = 8        # number of beats in one bar
bar = 120           # how many bar, not the one with liquor
note_duration = 4    # Duration for one note

############################################################################################################################
# Yes, this is where it generates the movement, progression

progression = prog_gen_sim(bar)

# Just to let you know the progresion
print(progression)


##############################################################################################################################
# beat generator

beat = beat_gen_ran_3(int(bar/12), beats_per_bar)
beat = beat_gen_ran_3(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran(int(bar/12), beats_per_bar)
beat = beat_gen_ran_3(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran_2(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran_2(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran_2(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran_3(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran(int(bar/12), beats_per_bar)
beat = beat+beat_gen_ran_3(int(bar/12), beats_per_bar)


beat2 = beat_gen_ran_2(bar, beats_per_bar)
beat3 = beat_gen_ran_3(bar, beats_per_bar)

#############################################################################################################################
# Convert the progression into semitone count
for i in range(0, len(progression)):
    if progression[i] == 1:
        progression[i] = 0 + root
    if progression[i] == 2:
        progression[i] = 2 + root
    if progression[i] == 3:
        progression[i] = 4 + root
    if progression[i] == 4:
        progression[i] = 5 + root
    if progression[i] == 5:
        progression[i] = 7 + root
    if progression[i] == 6:
        progression[i] = 9 + root
    if progression[i] == 7:
        progression[i] = 11 + root

progression_2 = []
progression_2 = [note-12 for note in progression]

progression_3 = []
progression_3 = [note+12 for note in progression]

print(progression)
piece_melody = melody_gen_1(root, progression, beat)
piece_melody2 = melody_gen_1(root, progression_2, beat2)
piece_melody3 = melody_gen_1(root, progression_3, beat3)


# declare list to store waveform
waveform = [0] * int((bar + 4) * tempo * beats_per_bar * sample_rate)

# generate the waveform with waveform_gen function
samples = waveform_gen_new(bar, tempo, sample_rate, piece_melody, waveform, note_duration)
#samples = waveform_gen_new(bar, tempo, sample_rate, piece_melody2, waveform, note_duration)
#samples = waveform_gen_new_2(bar, tempo, sample_rate, piece_melody3, waveform, note_duration)


##############################################################################################################################
# generate the wav file
samples2 = np.asarray(samples)
#generate date for saving
nowdate = datetime.datetime.now()
wavfile.write('%d_%d_%d-t%d.%d.%d-wave_test.wav' %(nowdate.year, nowdate.month, nowdate.day, nowdate.hour, nowdate.minute, \
                nowdate.second), sample_rate, samples2.astype(np.dtype('i2')))


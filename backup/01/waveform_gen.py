import numpy as np


##############################################################################################################################
# notes hold the dictionary to frequency of different notes
note_freq=[]
# Import the note's frequency data
count = 0
filename = 'note_frequency.txt'
with open(filename) as file_note:
    for line in file_note:
        note_freq_line = line.split('\t')
        note_freq.append((note_freq_line[0], float(note_freq_line[1])))
        #count = count + 1

file_note.close()

##############################################################################################################################




##################################################################################################################################
# sine half-wavelength envelope
def waveform_gen_sine(bar, tempo, sample_rate, piece_list,beat_list):
    # volume and duration for note
    volume = 10
    note_duration = 4
    
    # declare list to store waveform
    waveform = [0] * (bar + 1) * sample_rate
    # Total sample for one note
    note_sample = sample_rate * note_duration
    # The time progress for waveform
    t = 0
    # Count for the note
    count = 0

    for note in piece_list:
        # generate waveform using note in melody list
        print(note[1])
        for n in range(note_sample):
            waveform[t+n] = waveform[t+n] + volume * np.sin(2 * 3.142 * note[1] * n / sample_rate)*np.sin(3.142 * t /note_sample) * 127 + 128
            #waveform[t+n] = 127 * waveform[t+n] + 128
        count = count + 1
        print(count)
        t = t + int(sample_rate * beat_list[count])
    
    return waveform


#################################################################################################################################
 # exponential envelope, sounds more natural, exponential decay
def waveform_gen_exp(bar, tempo, sample_rate, piece_list,beat_list):
    # volume and duration for note
    volume = 30
    note_duration = 2
    
    # declare list to store waveform
    waveform = [0] * (bar + 1)  * note_duration * 8 * sample_rate
    # Total sample for one note
    note_sample = sample_rate * note_duration
    # The time progress for waveform
    t = 0
    # Count for the note
    count = 0

    for note in piece_list:
        # generate waveform using note in piece list
        print(count)
        for n in range(note_sample):
            for i in note:
                waveform[t+n] = waveform[t+n] + volume * np.sin(2 * 3.142 * note_freq[i][1] * n / sample_rate)*np.exp(-0.0001*n) * 127 + 128
            #waveform[t+n] = 127 * waveform[t+n] + 128
        count = count + 1
        t = t + int(sample_rate * beat_list[count])
    
    # remove addtional blanks in waveform list
    # intialise counters
    count = 0
    waveform2 = []
    for i in waveform:
        if (i == 0):
            count = count +1
            if count == 4:
                break
        else:
            waveform2.append(i)
    
    #np.savetxt('waveform_text.txt',waveform, fmt ='%10.5f')
    return waveform2


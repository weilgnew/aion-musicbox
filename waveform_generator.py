import numpy as np

##################################################################################################################################
# sine half-wavelength envelope
def waveform_gen_sine(bar, tempo, sample_rate, melody_list,beat_list):
    # volume and duration for note
    volume = 10
    note_duration = 4
    
    # declare list to store waveform
    waveform = [0] * (bar + 1) * tempo * sample_rate
    # Total sample for one note
    note_sample = sample_rate * note_duration
    # The time progress for waveform
    t = 0
    # Count for the note
    count = 0

    for note in melody_list:
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
def waveform_gen_exp(bar, tempo, sample_rate, melody_list,beat_list):
    # volume and duration for note
    volume = 30
    note_duration = 4
    
    # declare list to store waveform
    waveform = [0] * (bar + 1) * tempo * sample_rate
    # Total sample for one note
    note_sample = sample_rate * note_duration
    # The time progress for waveform
    t = 0
    # Count for the note
    count = 0

    for note in melody_list:
        # generate waveform using note in melody list
        print(note[1])
        for n in range(note_sample):
            waveform[t+n] = waveform[t+n] + volume * np.sin(2 * 3.142 * note[1] * n / sample_rate)*np.exp(-0.00005*n) * 127 + 128
            #waveform[t+n] = 127 * waveform[t+n] + 128
        count = count + 1
        t = t + int(sample_rate * beat_list[count])
    
    #np.savetxt('waveform_text.txt',waveform, fmt ='%10.5f')
    return waveform


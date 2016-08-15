# Generate beat, tempo for the piece

##############################################################################
def beat_gen_sim(length):
    beat = []
    for i in range(0,length):
        if i%2 == 0:
            beat.append(4)
            beat.append(2)
            beat.append(4)
            beat.append(2)
        else:
            beat.append(4)
            beat.append(4)
            
    return beat

###############################################################################

def beat_gen_reg_1(length):
    beat = []
    beat.append(8)
    beat.append(8)
    beat.append(8)
    beat.append(8)
    for i in range(0,length):
            beat.append(4)
            beat.append(4)
            beat.append(8)
            
            beat.append(4)
            beat.append(4)
            beat.append(4)
            beat.append(4)
            
    return beat
    
###############################################################################

def beat_gen_chord_2(length):
    beat = []

    for i in range(0,length):
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            beat.append(6)
            
    return beat

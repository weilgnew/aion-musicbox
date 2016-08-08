# Generate beat, tempo for the piece

##############################################################################
def beat_gen_sim(length):
    beat = []
    for i in range(0,length):
        if i%2 == 0:
            beat.append(8)
            beat.append(4)
            beat.append(8)
            beat.append(4)
        else:
            beat.append(4)
            beat.append(4)
            
    return beat

###############################################################################

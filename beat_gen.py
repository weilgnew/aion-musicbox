import random

# Generate beat, tempo for the piece

##############################################################################
# randomly generate 2 bars of beats, then repeat
# 3/5 chance to be active beat
def beat_gen_ran(bar,beats_per_bar):
    beat = []
    if bar%2 != 0:
        print("error! bar must be even number")
        return 0
    
    for n in range(2*beats_per_bar):
        beat.append(random.choice([0,0,1,1,1]))
            
    return beat*(bar/2)
    
print(beat_gen_ran(4,8))

##############################################################################
# randomly generate 2 bars of beats, then repeat
# 4/5 chance to be active beat
def beat_gen_ran_2(bar,beats_per_bar):
    beat = []
    if bar%2 != 0:
        print("error! bar must be even number")
        return 0
    
    for n in range(2*beats_per_bar):
        beat.append(random.choice([0,1,1,1,1]))
            
    return beat*(bar/2)
    
#print(beat_gen_ran(10,4))


###############################################################################
# randomly generate 2 bars of beats, then repeat
# 2/5 chance to be active beat
def beat_gen_ran_3(bar,beats_per_bar):
    beat = []
    if bar%2 != 0:
        print("error! bar must be even number")
        return 0
    
    for n in range(2*beats_per_bar):
        beat.append(random.choice([0,0,0,1,1]))
            
    return beat*(bar/2)
    
#print(beat_gen_ran(10,4))


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
            beat.append(4)
            beat.append(4)
            beat.append(4)
            beat.append(4)           
            beat.append(4)
            beat.append(4)
            beat.append(4)
            beat.append(4)
            beat.append(4)
            beat.append(4)
            beat.append(4)
            
    return beat
    
###############################################################################
def beat_gen_ran_bar(bar_length):
    beat = []
     
    #generate the random beat in a bar
    #for i in range(8):
        #if random.choice([1,2]) == 1:
        #    beat.append(2)
        #else:
        #    beat.append(4)
    beat.append(2)
    beat.append(2)
    beat.append(6)
    beat.append(6)
    
    beat.append(2)
    beat.append(6)
    beat.append(2)
    beat.append(6)
    
    beat.append(2)
    beat.append(2)
    beat.append(6)
    beat.append(6)
    
    beat.append(6)
    beat.append(6)
    beat.append(2)
    beat.append(2)
    
    return beat*100
        
     
     
    
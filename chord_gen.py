import random

################################################################################
def chord_maj_ran_gen(root, melody_list):
    # major triad
    # 0, 4, 7 half steps up
    # 0, -5, -8 half step down
    
    # Baseline generator, revolving one octave down the input root
    # Random generate 1 or 2 notes, major triad 
    piece = [[]]
    i = 0
    for note in melody_list:
        if random.randint(1,2) == 2:
            piece[i].append(note - 12 + random.choice([0,4,7]))
            piece[i].append(note - 12 + random.choice([-8,-5]))
        else:
            piece[i].append(note - 12 + random.choice([0,4,7]))
            
        i = i + 1
        piece.append([])
        
    
    # Soprano generator, revolving one octave up the input root
    # Random Generate 3 or 4 notes, major triad
    i = 0
    for note in melody_list:
        if random.randint(3,4) == 3:
            piece[i].append(note + 12 + random.choice([0,4]))
            piece[i].append(note + 12 + random.choice([-5,-8]))
            piece[i].append(note + 12 + random.choice([7,-12]))
        else:
            piece[i].append(note + 12 + random.choice([0,4]))
            piece[i].append(note + 12 + random.choice([-5,-8]))
            piece[i].append(note + 12 + random.choice([7,-12]))
            piece[i].append(note + 12 + random.choice([12,16]))
    
        i = i + 1
   
    return piece
    
###############################################################################
# generate the chord based on the first rule of thumbs

def chord_maj_gen(root, melody_list):
    # major triad
    # 0, 4, 7 half steps up
    # 0, -5, -8 half step down
    
    # generate the first initial chord 
    piece = [[]]
    if random.randint(1,2) == 2:
        piece[0].append(root - 12 + random.choice([0,4,7]))
        piece[0].append(root - 12 + random.choice([-8,-5]))
    else:
        piece[0].append(root - 12 + random.choice([0,4,7]))
    
    piece[0].append(root + 12 + random.choice([0,4]))
    piece[0].append(root + 12 + random.choice([-5,-8]))
    piece[0].append(root + 12 + random.choice([7,-12]))
    
    piece.append([])
    # generate the subsequent chords based on rules of thumb
    # baseline movement
    i = 1    
    for note in melody_list:
        chord = [note-12, note-8, note-5, note-24, note-20, note-17 ]
        for n in chord:
            if n in piece[-1]:
                piece[i].append(n)
        if len(piece[i]) == 0:
            piece[i].append(note - 12 + random.choice([0,4,7]))
            piece[i].append(note - 12 + random.choice([-8,-5]))
      
        i = i+1
        piece.append([])
              
    # Soprano generator, revolving one octave up the input root
    # Random Generate 3 or 4 notes, major triad
    i = 1
    for note in melody_list:
        chord = [note+12, note+16, note+19, note+4, note+7, note]
        for n in chord:
            if n in piece[-1]:
                piece[i].append(n)
        if len(piece[i]) < 4:
            piece[i].append(note + 12 + random.choice([0,4]))
            piece[i].append(note + 12 + random.choice([-5,-8]))
            piece[i].append(note + 12 + random.choice([7,-12]))
        
        i = i+1
        
    return piece
    
###############################################################################
# generate the melodic chord based on the first and second rule of thumbs
# add in conjuncy melodic motion

def chord_maj_gen_2(root, melody_list):
    # major triad
    # 0, 4, 7 half steps up
    # 0, -5, -8 half step down
    
    # generate the baseline
    piece = [[]]
    for note in melody_list:
        piece.append([note - 12 ])
        piece.append([note - 12 + 4])
        piece.append([note - 12 + 7])
        piece.append([note - 12 + 12])
        
        
    # generate the soprano
    i = 0
    for note in melody_list:
        chord = [note+12, note+16, note+19, note+4, note+7, note]
        for n in chord:
            if n in piece[-2]:
                piece[i*4].append(n)
        piece[i*4+1].append(note + 12 + random.choice([0,-5]))
        piece[i*4+1].append(note + 12 + random.choice([4, 7]))
        piece[i*4+3].append(note + 12 + random.choice([-8,-5]))
        piece[i*4+3].append(note + 12 + random.choice([7,4]))  
        i = i+1
        
    
    return piece
    

#####################################################################
# generate the melodic chord based on the first and second rule of thumbs
# add in conjuncy melodic motion

def chord_maj_gen_2(root, melody_list):
    # major triad
    # 0, 4, 7 half steps up
    # 0, -5, -8 half step down
    
    # generate the baseline
    piece = [[]]
    for note in melody_list:
        piece.append([note - 12 ])
        piece.append([note - 12 + 4])
        piece.append([note - 12 + 7])
        piece.append([note - 12 + 12])
        
        
    # generate the soprano
    i = 0
    for note in melody_list:
        chord = [note+12, note+16, note+19, note+4, note+7, note]
        for n in chord:
            if n in piece[-2]:
                piece[i*4].append(n)
        piece[i*4+1].append(note + 12 + random.choice([0,-5]))
        piece[i*4+1].append(note + 12 + random.choice([4, 7]))
        piece[i*4+3].append(note + 12 + random.choice([-8,-5]))
        piece[i*4+3].append(note + 12 + random.choice([7,4]))  
        i = i+1
        
    
    return piece
    
#####################################################################



#melody = [1,2,3,4,5]
#print(chord_maj_gen(0, melody))

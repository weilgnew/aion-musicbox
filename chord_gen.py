import random

def chord_maj_gen(root, melody_list):
    # major trial
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
    # Random Generate 3 or 4 notes, major trial
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
    

#melody = [1,2,3,4,5]
#print(chord_maj_gen(0, melody))

import random 

################################################################################
def melody_gen_1(root, progression_list, beat_list):
    # major triad
    # 0, 4, 7 half steps up
    # 0, -5, -8 half step down
    # major scale: 0,2,4,5,7,9,11,12
    
    # Baseline generator, revolving one octave down the input root
    # Random generate 1 or 2 notes, major triad
    chord = [-36,-32,-29,-27,-25,-24,-20,-17,-15,-13,-12,-8,-5,-3,-1,0,2,4,5,7,9,11,12,14,16,17,19,21,23,24,26,28,29,31,33,35,36,38,40,41]
    piece = []
    piece.append([])
    i = 0
    for beat in beat_list:
        print(progression_list[int(i/8)])
        if beat == 0:
            piece[i].append(0)
        else:
            # for the first beat
            if i == 0:
                piece[i].append(progression_list[int(i/8)] + random.choice([0,4,7]))
                piece[i].append(progression_list[int(i/8)] + random.choice([-8,-5]))
                
            # for the start of previous rest beat or new progression
            elif (0 in piece[i-1]) or (int(i/8)>int(((i-1)/8))):
                print(int(i/8))
                piece[i].append(progression_list[int(i/8)] + random.choice([0,4,7]))
                piece[i].append(progression_list[int(i/8)] + random.choice([-8,-5]))
            # for the continuation notes
            else:
                if i > 2:
                    if not 0 in piece[i-2]:
                        if piece[i-1][0] > piece[i-2][0]:
                            piece[i].append(chord[chord.index(piece[i-1][0]-progression_list[int(i/8)])+random.choice([0,0,1,2,3])]+progression_list[int(i/8)])
                        else:
                            piece[i].append(chord[chord.index(piece[i-1][0]-progression_list[int(i/8)])-random.choice([0,0,1,2,3])]+progression_list[int(i/8)])                  
                    
                        if piece[i-1][1] > piece[i-2][1]:
                            piece[i].append(chord[chord.index(piece[i-1][1]-progression_list[int(i/8)])+random.choice([0,0,1,2,3])]+progression_list[int(i/8)])
                        else:
                            piece[i].append(chord[chord.index(piece[i-1][1]-progression_list[int(i/8)])-random.choice([0,0,1,2,3])]+progression_list[int(i/8)])
                    else:
                        piece[i].append(chord[chord.index(piece[i-1][0]-progression_list[int(i/8)])+random.choice([-3,-2,-1,0,0,1,2,3])]+progression_list[int(i/8)])
                        piece[i].append(chord[chord.index(piece[i-1][1]-progression_list[int(i/8)])+random.choice([-3,-2,-1,0,0,1,2,3])]+progression_list[int(i/8)])   
                else:
                    piece[i].append(chord[chord.index(piece[i-1][0]-progression_list[int(i/8)])+random.choice([-3,-2,-1,0,0,1,2,3])]+progression_list[int(i/8)])
                    piece[i].append(chord[chord.index(piece[i-1][1]-progression_list[int(i/8)])+random.choice([-3,-2,-1,0,0,1,2,3])]+progression_list[int(i/8)])  
           
        print(piece[i])
        i = i+1
        piece.append([])        
        

    return piece

print(melody_gen_1(40,[1,10],[1,1,1,0,0,1,1,1,1,1,1,0,0,1,1,1]))
##############################################################################
# Convert the melody in relative scale into absolute note positon
def melody_converter(progression_list, beats_per_bar, piece):
    piece_converted = []
    i = 0 # counter for melody
    for chord in progression_list:
        for n in range(beats_per_bar):
            for note in piece[i]:
                if note > 7:
                    note = note-7
                    if note == 1:
                        piece_converted.append(chord+12)
                    if note == 2:
                        piece_converted.append(chord+2+12)
                    if note == 3:
                        piece_converted.append(chord+4+12)
                    if note == 4:
                        piece_converted.append(chord+5+12)           
                    if note == 5:
                        piece_converted.append(chord+7+12)
                    if note == 6:
                        piece_converted.append(chord+9+12)
                    if note == 7:
                        piece_converted.append(chord+11+12)
                    continue
                elif note < 1:
                    note = note+8
                    if note == 1:
                        piece_converted.append(chord-12)
                    if note == 2:
                        piece_converted.append(chord+2-12)
                    if note == 3:
                        piece_converted.append(chord+4-12)
                    if note == 4:
                        piece_converted.append(chord+5-12)           
                    if note == 5:
                        piece_converted.append(chord+7-12)
                    if note == 6:
                        piece_converted.append(chord+9-12)
                    if note == 7:
                        piece_converted.append(chord+11-12)
                    continue
                else:
                    if note == 1:
                        piece_converted.append(chord)
                    if note == 2:
                        piece_converted.append(chord+2)
                    if note == 3:
                        piece_converted.append(chord+4)
                    if note == 4:
                        piece_converted.append(chord+5)           
                    if note == 5:
                        piece_converted.append(chord+7)
                    if note == 6:
                        piece_converted.append(chord+9)
                    if note == 7:
                        piece_converted.append(chord+11)
                    if note == 8:
                        piece_converted.append(chord+12)          
            
            i = i + 1
        
    return piece_converted
    
                    #if piece[i-1][1] > piece[i-2][1]:
                    #        piece[i].append(piece[i-1][1]+random.choice([0,4,7]))
                    #    else:
                    #        piece[i].append(piece[i-1][1]-random.choice([0,5,8]))
                    #else:
                    #    piece[i].append(piece[i-1][0]+random.choice([-8,-5,0,4,7]))
                    #    piece[i].append(piece[i-1][1]+random.choice([-8,-5,0,4,7]))   
# Generate melody
import random

#######################################################################
# simple melody gen, rules from harmony book
def melody_gen_sim(length):
    def root_next():
        x = random.normalvariate(3.5, 1)
        if x > 3.5 and x <= 4.5:
            return 5
        if x >= 2.5 and x <= 3.5:
            return 4
        if x >= 1.8 and x <= 5.2:
            return 6
        if x < 1.8:
            return 2
        if x > 5.2:
            return 3
    
    def second_next():
        x = random.normalvariate(3.5, 1)
        if x >= 2.7 and x <= 4.3:
            return 5
        if x >= 2 and x < 2.7:
            return 4
        if x > 4.3 and x <= 5 :
            return 6
        if x < 2:
            return 1
        if x > 5:
            return 3
    
    def third_next():
        x = random.normalvariate(3.5, 1)
        if x >= 2.7 and x <= 4.3:
            return 6
        if x >= 2 and x < 2.7:
            return 4
        if x > 4.3 and x <= 5 :
            return 5
        if x < 2:
            return 1
        if x > 5:
            return 2
    
    def fourth_next():
        x = random.normalvariate(3.5, 1)
        if x >= 2.7 and x <= 4.3:
            return 5
        if x >= 2 and x < 2.7:
            return 1
        if x > 4.3 and x <= 5 :
            return 2
        if x < 2:
            return 3
        if x > 5:
            return 6
    
    def fifth_next():
        x = random.normalvariate(3.5, 1)
        if x >= 2.7 and x <= 4.3:
            return 1
        if x >= 2 and x < 2.7:
            return 4
        if x > 4.3 and x <= 5 :
            return 6
        if x < 2:
            return 2
        if x > 5:
            return 3
    
    def sixth_next():
        x = random.normalvariate(3.5, 1)
        if x > 3.5 and x <= 4.5:
            return 2
        if x >= 2.5 and x <= 3.5:
            return 5
        if x >= 1.5  and x < 2.5:
            return 3
        if x > 4.5 and x <= 5.5 :
            return 4
        if x < 1.5 or x > 5.5 :
            return 1
    
    def seventh_next():
        x = random.normalvariate(3.5, 1)
        if x > 3.5 and x <= 4.5:
            return 1
        if x >= 2.5 and x <= 3.5:
            return 3
        if x >= 1.8 and x <= 5.2:
            return 6
        if x >= 1.2 and x <= 5.8:
            return 2
        if x < 1.2:
            return 4
        if x > 5.8:
            return 5
    
    melody = []
    for i in range(1, length):
        print(i)
        if melody[i-1] == 1:
            melody.append(root_next())
        if melody[i-1] == 2:
            melody.append(second_next())
        if melody[i-1] == 3:
            melody.append(third_next())
        if melody[i-1] == 4:
            melody.append(fourth_next())
        if melody[i-1] == 5:
            melody.append(fifth_next())
        if melody[i-1] == 6:
            melody.append(sixth_next())
        if melody[i-1] == 7:
            melody.append(seventh_next())
    
    return melody
############################################################################
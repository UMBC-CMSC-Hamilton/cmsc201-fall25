from random import randint

def exploding_d6 ():
    roll = randint (1 , 6)
    print('\t', roll)
    # if roll in [1, 2, 3]:
    if roll == 1 or roll == 2 or roll == 3:
        return 1
    elif roll == 4 or roll == 5:
        return 1 + exploding_d6()
    else:
        return 1 + exploding_d6() + exploding_d6()

for i in range(10):
    print(exploding_d6())
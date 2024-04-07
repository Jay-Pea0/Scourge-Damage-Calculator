from random import randint
import math

# define variables
# Total damage on round starts at 0
total = 0
#Level starts at 1
level = 1
#how many rounds of combat is going to run for
numRounds = 1000000
#Strength starts at +3
STR = 3
#Number of attacks starts at 1
numAttacks = 1

#get weapon damage dice
userInput = input("Please input the damage dice of your weapon (e.g. 1d10)\n")
userInput = userInput.split("d")
numDamageDice = int(userInput[0])
damageDie = int(userInput[1])
#get if using GWM or not
userInput = input("Great Weapon Master?\n[1] No\n[2] Yes\n")
if (userInput=="1"):
    hitOn = 8
    GWMDMG = 0
else:
    hitOn = 13
    GWMDMG = 10
#get if they have advantage to hit or not
rollType = input("[1] Normal to hit\n[2] Advantage\n[3] Disadvantage\n")


while (level < 21):
    #Calc PB for level
    PB = math.ceil(level/4) + 1

    #STR goes up at level 4 and 8
    if ((level == 4) or (level == 8)):
        STR += 1
    #extra attack at 5
    if (level == 5):
        numAttacks +=1
        
    #core program
    for i in range (numRounds): 

        twod20 = [randint(1,20), randint(1,20)]
        if (rollType == "1"):
            d20 = twod20[0]
        elif (rollType == "2"):        
            twod20.sort()
            d20 = twod20[1]
        else:      
            twod20.sort()
            d20 = twod20[0]
        

        
        for i in range (numAttacks):
            #on a miss
            if (d20 < hitOn):
                total += 0
            else:
                dice = []
                diceTotal = 0
                #on a hit
                if (d20 != 20):
                    for i in range(numDamageDice):
                        DMGRoll = randint(1,damageDie)
                        if (DMGRoll < PB):
                            DMGRoll = PB
                        dice.append(DMGRoll)
                    for d in dice:
                        diceTotal += d
                    total += (diceTotal + STR + GWMDMG)
                #on a crit
                else:
                    for i in range(numDamageDice*2):
                        DMGRoll = randint(1,damageDie)
                        if (DMGRoll < PB):
                            DMGRoll = PB
                        dice.append(DMGRoll)
                    for d in dice:
                        diceTotal += d
                    total += (diceTotal + STR + GWMDMG)


    # average out results
    print("Level "+str(level)+" Average:")
    print(total/numRounds)

    # Increase level
    level += 1
    # reset round total
    total = 0




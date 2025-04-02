from matplotlib import pyplot as plt
import random

low_broke = 28
high_profit = 65
random_multiple = 0

#constants for comparison
Cnumber_of_bettors = 1000
Cfunds = 10000
Cinitial_wager = 100
Cwager_count = 100

#profit and loss constants
simple_p_count = 0
martingale_p_count = 0
multiples_p_count = 0



def rolldice():
    roll = random.randint(1,100)

    if roll == 100:
        #print("roll was 100, you loose")
        return False
    elif roll <= 50:
        #print("roll below 50, you loose")
        return False
    elif 100 > roll > 50:
        #print("roll was above 50, you win")
        return True


def martingale_bettor(funds, initial_wager, wager_count):
    global broke_count
    global martingale_p_count
    value = funds
    wager = initial_wager
    wagerX = []
    valueY = []
    currentWager = 1
    previousWager = 'win'
    previous_wager_value = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rolldice():
                value += wager
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value < 0:
                    broke_count += 1
                    break

        elif previousWager == 'loss':
            if rolldice():
                wager = previous_wager_value * 2
                if value - wager < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                wager = previous_wager_value * 2
                if value - wager < 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value < 0:
                    broke_count += 1
                    break

        currentWager += 1
    plt.plot(wagerX,valueY, color = "blue")
    if valueY[len(valueY)-1] > Cfunds:
        martingale_p_count += 1
    
def multiples_bettor(funds, initial_wager, wager_count):
    global broke_count
    global multiples_p_count
    value = funds
    wager = initial_wager
    bet_coefficient = random_multiple
    wagerX = []
    valueY = []
    currentWager = 1
    previousWager = 'win'
    previous_wager_value = initial_wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            if rolldice():
                value += wager
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value < 0:
                    broke_count += 1
                    break

        elif previousWager == 'loss':
            if rolldice():
                wager = previous_wager_value * bet_coefficient
                if value - wager < 0:
                    wager = value
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                wager = previous_wager_value * bet_coefficient
                if value - wager < 0:
                    wager = value
                value -= wager
                previousWager = 'loss'
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value < 0:
                    broke_count += 1
                    break

        currentWager += 1
    plt.plot(wagerX,valueY, color = "orange")
    if valueY[len(valueY)-1] > Cfunds:
        multiples_p_count += 1

### Martingale bettor ###

broke_count = 0
martingale_p_count = 0
end_values = []
for j in range (0, Cnumber_of_bettors):
    end_values.append(martingale_bettor(Cfunds, Cinitial_wager, Cwager_count))

martingate_broke_rate = (broke_count/float(Cnumber_of_bettors)) * 100
print("Martingate broke rate is " + str(martingate_broke_rate) + " %")
print("Martingale bet profit chance is " + str((martingale_p_count)/float(j)*100) + " %")

### Multiples bettor loop ###

for i in range (1, 100):
    end_values = []
    random_multiple = random.randint(1, 100)/10
    broke_count = 0
    multiples_p_count = 0
    for j in range (0, Cnumber_of_bettors):
        #martingale_bettor(funds, initial_bet, wager_count):
        end_values.append(multiples_bettor(Cfunds, Cinitial_wager, Cwager_count))

    multiples_broke_rate = (broke_count/float(Cnumber_of_bettors)) * 100
    multiples_profit_rate = (multiples_p_count/float(Cnumber_of_bettors)) * 100
    #print("For multiple " + str(random_multiple) + " broke rate is " + str(multiples_broke_rate) + " %" + " and profit chance is " + str(multiples_profit_rate) + " %")
    if ((multiples_broke_rate) < 27) and ((multiples_profit_rate) > 64):
        print("Multiple " + str(random_multiple) + " is a winner")
        print("For multiple " + str(random_multiple) + " broke rate is " + str(multiples_broke_rate) + " %" + " and profit chance is " + str(multiples_profit_rate) + " %")

print("Analysis Complete")

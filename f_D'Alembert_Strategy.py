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


def dalembert_bettor(funds, initial_wager, wager_count):
    global broke_count
    global dalambert_p_count
    value = funds
    wager = initial_wager
    wagerX = []
    valueY = []
    currentWager = 1
    previousWager = 'win'
    previous_wager_value = wager

    while currentWager <= wager_count:
        if previousWager == 'win':
            wager = previous_wager_value - initial_wager
            # the wager cannot be below starting bet unless account value is below the starting bet
            if (wager < initial_wager) and value >= (initial_wager):
                wager = initial_wager
            if rolldice():
                value += wager
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                value -= wager 
                previousWager = 'loss'
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value <= 0:
                    broke_count += 1
                    break

        elif previousWager == 'loss':
            wager = previous_wager_value + initial_wager
            if wager + initial_wager > value:
                wager = value 
            if rolldice():
                value += wager
                previous_wager_value = wager
                previousWager = 'win'
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                value -= wager
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value <= 0:
                    broke_count += 1
                    break

        currentWager += 1
        print("Account value is " + str(value) + " wager is now " + str(wager))
    plt.plot(wagerX,valueY)
    if valueY[len(valueY)-1] > Cfunds:
        dalambert_p_count += 1
    
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
                print(value)
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

### D'Alembert bettor ###

broke_count = 0
dalambert_p_count = 0
end_values = []
for j in range (0, Cnumber_of_bettors):
    end_values.append(dalembert_bettor(Cfunds, Cinitial_wager, Cwager_count))

dalambert_broke_rate = (broke_count/float(Cnumber_of_bettors)) * 100
dalambert_profit_rate = (dalambert_p_count/float(Cnumber_of_bettors) * 100)
print("D'Alembert broke rate is " + str(dalambert_broke_rate) + " %")
print("D'Alembert bet profit chance is " + str(dalambert_profit_rate) + " %")

plt.show()

from matplotlib import pyplot as plt
import random

#constants for comparison
Cnumber_of_bettors = 1000
Cfunds = 100000
Cinitial_wager = 100
Cwager_count = 1000
total_ret = 0

total_ret = 0

def rolldice():
    roll = random.randint(1,100)
    if roll <= 50:
        return False
    elif roll > 50:
        return True


def dalembert_bettor(funds, initial_wager, wager_count):
    global broke_count
    global dalambert_p_count
    global total_ret
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
    plt.plot(wagerX,valueY, color = "blue")
    if valueY[len(valueY)-1] > Cfunds:
        dalambert_p_count += 1
    total_ret += (value)
    
### D'Alembert bettor ###


broke_count = 0
dalambert_p_count = 0
end_values = []
for j in range (0, Cnumber_of_bettors):
    end_values.append(dalembert_bettor(Cfunds, Cinitial_wager, Cwager_count))

dalambert_broke_rate = (broke_count/float(Cnumber_of_bettors)) * 100
dalambert_profit_rate = (dalambert_p_count/float(Cnumber_of_bettors) * 100)


### Multiples bettor loop ###

sampsize = 1000
counter = 1

while counter <= sampsize:
    dalembert_bettor(Cfunds, Cinitial_wager, Cwager_count)
    counter += 1

print("Total invested is " + str(Cnumber_of_bettors * Cfunds))
print("Total return is " + str(total_ret))
print("Return of investment (difference) is " + str(total_ret - (Cnumber_of_bettors * Cfunds)))
print("D'Alembert broke rate is " + str(dalambert_broke_rate) + " %")
print("D'Alembert bet profit chance is " + str(dalambert_profit_rate) + " %")

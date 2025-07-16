from matplotlib import pyplot as plt
import random



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
                value += wager
                wager = initial_wager
                previousWager = 'win'
                wagerX.append(currentWager)
                valueY.append(value)
            else:
                wager = previous_wager_value * 2
                value -= wager
                previousWager = 'loss'
                previous_wager_value = wager
                wagerX.append(currentWager)
                valueY.append(value)
                if value < 0:
                    broke_count += 1
                    break

        currentWager += 1
    plt.plot(wagerX,valueY)
        

broke_count = 0


end_values = []
#number of bettors
for i in range (0, 100):
    #martingale_bettor(funds, initial_bet, wager_count):
    end_values.append(martingale_bettor(10000, 100, 1000))
    i += 1

plt.xlabel("wager number")
plt.ylabel("account value")

plt.axhline(0, color = "red")

print(broke_count)

broke_rate = (broke_count/float(i)) * 100
print("broke rate is " + str(broke_rate) + " %")
#print(end_values)

plt.show()

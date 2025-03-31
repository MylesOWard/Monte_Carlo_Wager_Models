from matplotlib import pyplot as plt
import random


#constants for comparison
Cnumber_of_bettors = 100
Cfunds = 10000
Cinitial_wager = 100
Cwager_count = 1000


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

def simple_bettor(funds, initial_bet, wager_count):
    value = funds 
    wager = initial_bet

    value_list = []
    wager_list = []

    current_wager = 1
    
    while(current_wager < wager_count + 1):
        global broke_count
        if value - wager < 0:
            wager = value
        if rolldice():
            value += wager
            wager_list.append(current_wager)
            value_list.append(value)  
        else:
            value -= wager 
            wager_list.append(current_wager)
            value_list.append(value)  
        current_wager += 1
        #print(value)
    if current_wager == wager_count:
        if value <= 0: 
            value = 0
            print("broke")
            return(value)
        else:
            print(value)
            return(value)
    plt.plot(wager_list, value_list, color = "green")

### Simple bettor ###     

broke_count = 0

end_values = []

for i in range (0, Cnumber_of_bettors):
    #martingale_bettor(funds, initial_bet, wager_count):
    end_values.append(simple_bettor(Cfunds, Cinitial_wager, Cwager_count))
    i += 1

plt.xlabel("wager number")
plt.ylabel("account value")

plt.axhline(0, color = "red")

print(broke_count)

simple_broke_rate = (broke_count/float(i)) * 100
print("simple broke rate is " + str(simple_broke_rate) + " %")
#print(end_values)

### Martingale bettor ###

broke_count = 0

end_values = []

for j in range (0, Cnumber_of_bettors):
    #martingale_bettor(funds, initial_bet, wager_count):
    end_values.append(martingale_bettor(Cfunds, Cinitial_wager, Cwager_count))
    j += 1

plt.xlabel("wager number")
plt.ylabel("account value")

plt.axhline(0, color = "red")

print(broke_count)

martingate_broke_rate = (broke_count/float(j)) * 100
print("martingate broke rate is " + str(martingate_broke_rate) + " %")


plt.show()

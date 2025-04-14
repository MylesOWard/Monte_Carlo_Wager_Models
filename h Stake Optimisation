from matplotlib import pyplot as plt
import random

def rolldice():
    roll = random.randint(1,100)

    if roll == 100:
        return False
    elif roll <= 50:
        #print("roll below 50, you loose")
        return False
    elif roll > 50:
        #print("roll was above 50, you win")
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


Cfunds = 10000

for i in range(0,5):
    #Cinitial_wager = 100
    #Cwager_count = 100000
    Cinitial_wager = random.uniform(1.00, 1000.00)
    Cwager_count = random.uniform(10.00, 10000.00)

    total_ret = 0
    dalambert_p_count = 0
    broke_count = 0
    Cnumber_of_bettors = 10000

    counter = 1

    while counter <= Cnumber_of_bettors:
        dalembert_bettor(Cfunds, Cinitial_wager, Cwager_count)
        counter += 1

    ROI = total_ret - (Cfunds * Cnumber_of_bettors)
    percentage_ROI = (ROI / (Cfunds * Cnumber_of_bettors))*100

    dalambert_broke_rate = (broke_count/float(Cnumber_of_bettors)) * 100
    dalambert_profit_rate = (dalambert_p_count/float(Cnumber_of_bettors) * 100)

    wager_sizer_percent = (Cinitial_wager/Cfunds)

    if ROI > 0:
        print("#####")
        print("For a starting wager of " + str(Cinitial_wager) + " making " + str(Cwager_count) + " bets:")
        print("Total invested is " + str(Cnumber_of_bettors * Cfunds) + (" and total return is " + str(total_ret)))
        print("Return of investment (difference) is " + str(total_ret - (Cnumber_of_bettors * Cfunds)))
        print("So percentage return on investment is " + str(round(percentage_ROI,2))+ ("%"))
        print("D'Alembert broke rate is " + str(round(dalambert_broke_rate,2)) + (" %"))
        print("D'Alembert bet profit chance is " + str(round(dalambert_profit_rate, 2)) + (" %"))
        print("#####")

        saveFile = open('monteCarlo.csv','a')
        saveLine = '\n'+str(percentage_ROI)+','+str(wager_sizer_percent)+','+str(Cwager_count)+',g'
        saveFile.write(saveLine)
        saveFile.close()

    if ROI < 0:
        print("#####")
        print("For a starting wager of " + str(Cinitial_wager) + " making " + str(Cwager_count) + " bets:")
        print("Total invested is " + str(Cnumber_of_bettors * Cfunds) + (" and total return is " + str(total_ret)))
        print("Return of investment (difference) is " + str(total_ret - (Cnumber_of_bettors * Cfunds)))
        print("So percentage return on investment is " + str(round(percentage_ROI,2))+ ("%"))
        print("D'Alembert broke rate is " + str(round(dalambert_broke_rate,2)) + (" %"))
        print("D'Alembert bet profit chance is " + str(round(dalambert_profit_rate, 2)) + (" %"))
        print("#####")


        saveFile = open('monteCarlo.csv','a')
        saveLine = '\n'+str(percentage_ROI)+','+str(wager_sizer_percent)+','+str(Cwager_count)+',g'
        saveFile.write(saveLine)
        saveFile.close()

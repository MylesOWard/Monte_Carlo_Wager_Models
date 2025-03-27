from matplotlib import pyplot as plt
import random
import statistics

# simple roulette style random chance with a ~1% house edge 
def rolldice():
    roll = random.randint(1,100)
    if roll == 100:
        # print("roll was 100, you loose")
        return False 
    elif 100 > roll > 50:
        # print("roll was above 50, you win")
        return True
    else:
        # print("roll below 51, you loose")
        return False
    return roll

# funds represents the total account value of the bettor
# once the account value hits 0 the bettor is broke
def simple_bettor(funds, initial_bet, wager_count):
    value = funds 
    wager = initial_bet

    value_list = []
    wager_list = []

    current_wager = 1
    
    while(current_wager < wager_count + 1):
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
    plt.plot(wager_list, value_list)
        
i = 0
end_values = []

# number of bettors
for i in range (0, 100):
    end_values.append(simple_bettor(10000, 100, 1000))
    i += 1


plt.xlabel("wager #")
plt.ylabel("account value")
plt.show()

print(end_values)

mean = statistics.mean(end_values)
print("expectation value is " + str(mean))

from byotest import *


usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins = {200: 20, 100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}


'''
Change the function so that instead of a list of coins, 
the function works with a dictionary that contains the coin denominations, 
and the quantity of each coin available. By default, 
assume there are 20 of each coin, but this can be overridden by 
passing a dictionary to the function as with the previous example.

If a coin that would normally be used to make change isn't available 
the program should attempt to use smaller coins to make up the change.

If it is not possible to make the change with the coins available, 
the function should raise an error.
'''


def get_change(amount, coins = eur_coins):
    change = []
    '''we create a loop to access the elements in the dictionary
    - dictionaries are not organised so we need to sorted and reverse de way we access it
    - in order to give change you start from the biggest number'''
    for denomination in sorted(coins.keys(), reverse=True):
        ''' while loop will be sure the number will be used as many times as possible
        before it looks for a minor value to continue.
        we access the value of every key, which is the amount of coins we have on every
        denomination and rest 1 every time we use a coin.
        * in the while loop we append to the empty change array every values that is used
         in the operation amount - denomination'''
        while denomination <= amount and coins[denomination] > 0:
            #print(amount, denomination)
            amount -= denomination
            #print(amount)
            coins[denomination] -= 1
            #print(coins[denomination])
            change.append(denomination)
            #print(change)
            #print(coins)

    if amount != 0:
        raise Exception("Insufficient coins to give change.")

    return change


test_are_equal(get_change(0), [])

test_are_equal(get_change(1), [1])
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])
test_are_equal(get_change(90), [50, 20, 20])

test_are_equal(get_change(35, usd_coins), [25, 10])

print('all tests passed ')

get_change(1345, eur_coins)

print(get_change(1345, eur_coins))
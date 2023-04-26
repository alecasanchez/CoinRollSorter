
# Global constants in order of value highest to lowest
_quarter = 24
_dime = 18
_nickel = 21
_penny = 19

# Defining the function "tally_coins" to sort the coins by value.
# bag_coins is the parameter
def tally_coins(bag_coins):

# Variables to keep track of the coin count
    quarter_count = 0
    dime_count = 0
    nickel_count = 0
    penny_count = 0
    foreign_count = 0

# Running a for loop to check condition for all coins in bag
    for coin in bag_coins:
        if coin == _quarter:
            quarter_count+=1
        elif coin == _dime:
            dime_count+=1
        elif coin == _nickel:
            nickel_count+=1
        elif coin == _penny:
            penny_count+=1
        else:
            foreign_count+=1
    return (quarter_count, dime_count, nickel_count, penny_count, foreign_count)

# Display each coin tally and total value
# [] index brakets define the list literals corresponding to "coin_counts"
# Calling the function "display_coins"
def display_coins(coin_counts):
    print("The bag contains the following coins:")
    print("Quarter:", coin_counts[0])
    print("Dime:", coin_counts[1])
    print("Nickel:", coin_counts[2])
    print("Penny:", coin_counts[3])
    print("Foreign:", coin_counts[4])
    print("Total value in the bag: $", calculate_total(coin_counts))

# Returns the total value of the bag with correct denominations
def calculate_total(coins):

# Result is coin value multiplied by number of coin
    res = 0.25*coins[0] + 0.10*coins[1] + 0.05*coins[2] + 0.01*coins[3]
    return res

# Coins listed by diameter
# variable __name__ == the main module __main__ 
def main():
    bag_coin= [24,18,21,20,19,24,18,21,20,19,24,18,21,19,24,18,23,21,19,24,18,21,19,24,18,21,30,32,24,26]
    coin_counts = tally_coins(bag_coin)
    display_coins(coin_counts)
if __name__ == "__main__":
    main()
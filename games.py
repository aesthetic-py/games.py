import random

money = 100

#Write your game of chance functions here

def coin_flip(guess, bet):

    #Make sure the user entered a valid bet.
    if bet <=0:
        print("Your wager must be higher than 0.")
        return
    elif bet > money:
        print("You do not have enough money to place that bet.")
        return

    #Start the game
    print(f"Let's play! You guessed {guess}.")
    coin_result = random.randint(0,1)

    #Show the results of the coin flip to the user
    if coin_result == 0:
        print("Heads")
    elif coin_result == 1:
        print("Tails")
    else:
        print("The coin did not land on the table. Please retry.")

    #Display the outcome of the game
    if coin_result == 0 and guess == "heads":
        print(f"You won ${bet} well done!")
        return bet
    elif coin_result == 1 and guess == "tails":
        print(f"You won ${bet} well done!")
        return bet
    else:
        print(f"Better luck next time. You lost ${bet}.")
        return -bet

#coin_flip("heads", 15)

def cho_han(guess, bet):
    #Make sure the user entered a valid bet.
    if bet <=0:
        print("Your wager must be higher than 0.")
        return
    elif bet > money:
        print("You do not have enough money to place that bet.")
        return

    #Start the game
    print(f"Let's roll the dice. You guessed {guess}.")
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1+dice2

    #Show the results
    print(f"The dice show {dice1} and {dice2}. A total of {dice_sum}.")
    if dice_sum%2 == 0 and guess == "even":
        print(f"You guessed correctly! You won {bet}!")
        return bet
    elif dice_sum%2 != 0 and guess == "odd":
        print(f"You guessed correctly! You won {bet}")
        return bet
    else:
        print(f"Better luck next time. You lost ${bet}.")
        return -bet

#play_cho_han("even", 12)

def higher_card(bet):
    #Make sure the user entered a valid bet.
    if bet <=0:
        print("Your wager must be higher than 0.")
        return
    elif bet > money:
        print("You do not have enough money to place that bet.")
        return

    #Start the game
    p1 = random.randint(1, 14)
    p2 = random.randint(1, 14)

    #Show the results
    print(f"You drew a {p1}.")
    print(f"Player two draws a {p2}.")
    if p1>p2:
        print(f"Congratulations! You won ${bet}!")
        return bet
    elif p1 == p2:
        print("It's a tie!")
        return 0
    else:
        print("Sorry, better luck next time!")

#higher_card(100)

def roulette(guess, bet):

    #Make sure the user entered a correct value for their bet.
    if bet <=0:
        print("Your wager must be higher than 0.")
        return
    elif bet > money:
        print("You do not have enough money to place that bet.")
        return


    #Possible outcomes
    roulette_roll_list = [00, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
                     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                     31, 32, 33, 34, 35, 36]

    #Spin the ball
    roulette_roll = random.choice(roulette_roll_list)
    print(f"The wheel landed on {roulette_roll}.")

    #Even vs odd outcome
    if roulette_roll % 2 == 0 and guess == "even":
        print(f"Congratulations! You won ${bet}.")
        return bet*2
    elif roulette_roll%2 != 0 and guess == "odd":
        print(f"Congratulations! You won ${bet}.")
        return bet*2
    elif guess == roulette_roll:
        print(f"Congratulations! You won ${bet}.")
        return bet*35
    else:
        print("Sorry, better luck next time.")
        return -bet


#play_roulette("even", 25)

#Call your game of chance functions here
'''
money += coin_flip("heads", 10)
money += higher_card(5)
money += cho_han("even", 2)
money += roulette("even", 10)
money += roulette(3, 1)
money += roulette("odd", money)
print("Your total amount of money is " + str(money))
'''

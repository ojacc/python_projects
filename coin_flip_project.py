import random
#b = random.randint(2,9)
def coin_flip():
    play_on = True
    #continuee = True
    possible_results = ["heads", "tails"]
    results_to_print = ["Heads", "Tails"]
    wins_losses = ["Wins", "Losses"]
    count = [0, 0]
    while play_on:
        print("A coin flip is going to be performed. Which outcome do you expect?")
        heads_or_tails = input("Heads or Tails? ")
        if not heads_or_tails.lower() in possible_results:
            print("Unvalid input. Please type: 'Heads' or 'Tails'.")
            continue
        flip_result = possible_results[random.randint(0,1)]
        print("Flipping...\nCoin has landed...\nResult: " + results_to_print[possible_results.index(flip_result)])
        if heads_or_tails.lower() == flip_result:
            count[0] += 1
            print("Congratulations, you won!")
        else:
            count[1] += 1
            print("You lost, shame on you!")
        wins_losses_count = list(zip(wins_losses, count))
        while True:
            what_next = input("Choose one:\nA: Flip again\nB: Check score\nC: Exit game\n")
            if what_next in ["A", "a", "Flip again", "flip again"]:
                break
            elif what_next in ["C", "c", "Exit game", "exit game"]:
                print("Goodbye!")
                play_on = False
                break
            elif what_next in ["B", "b", "Check score", "check score"]:
                print("Current score:", wins_losses_count)
    return wins_losses_count

#coin_flip() 


def roll_dice():
    play_on = True
    wins_losses = ["Wins", "Losses"]
    count = [0, 0]
    while play_on:
        print("A 6-sided dice (1-6) is going to be rolled. Which outcome do you expect?")
        user_guess = int(input())
        if not user_guess in [1, 2, 3, 4, 5, 6]:
            print("Unvalid input. Please select an integer between 1 and 6.")
            continue
        dice_result = random.randint(1,6)
        print("Rolling...\nResult:", dice_result)
        if user_guess == dice_result:
            count[0] += 1
            print("Congratulations, you won!")
        else:
            count[1] += 1
            print("You fucking loser!")
        wins_losses_count = list(zip(wins_losses, count))
        while True:
            what_next = input("Choose one:\nA: Roll again\nB: Check score\nC: Exit game\n")
            if what_next in ["A", "a", "Roll again", "roll again"]:
                break
            elif what_next in ["C", "c", "Exit game", "exit game"]:
                print("Goodbye!")
                play_on = False
                break
            elif what_next in ["B", "b", "Check score", "check score"]:
                print("Current score:", wins_losses_count)
    return wins_losses_count

roll_dice()




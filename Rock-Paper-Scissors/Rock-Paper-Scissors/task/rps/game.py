import random
from collections import defaultdict

def obtain_options_list():
    line = input()
    if line == '':
        return ['paper', 'scissors', 'rock']
    else:
        return line.split(',')

def check_if_win(options, pcPick, userPick):
    if pcPick == userPick:
        return 1 # draw

    targetIdx = options.index(userPick)

    newOptions = options[:-1]
    if len(options) != targetIdx:
        newOptions = options[targetIdx + 1:] + options[:targetIdx]
    # print(newOptions)
    halfLen = int((len(newOptions)) / 2)
    # print(halfLen)
    pcChoiceIdx = newOptions.index(pcPick)
    if pcChoiceIdx < halfLen:
        return 0 # lose
    else:
        return 2 # win


def play_game(options, score = 0):
    while True:
        option = input()
        if option == "!exit":
            print("Bye!")
            break
        elif option == "!rating":
            print(f"Your rating: {score}")
            continue
        elif option not in options:
            print("Invalid input")
            continue

        pcPick = random.choice(options)
        userPick = option
        state = check_if_win(options, pcPick, userPick)

        # print(pick)
        result_string = [
            "Sorry, but computer chose {}".format(pcPick),
            'There is a draw ({})'.format(pcPick),
            'Well done. Computer chose {} and failed'.format(pcPick)
        ]

        score_table =[
            0,
            50,
            100
        ]

        score += score_table[state]

        print(result_string[state])

    return score



def read_file():
    fileObj = open("rating.txt", "r")

    rating = defaultdict(int)
    for line in fileObj:
        words = line.split(' ')
        rating[words[0]] = words[1]

    return rating


def main():
    name = input("Enter your name: ")
    print(f"Hello, {name}")

    options = obtain_options_list()
    print("Okay, let's start")

    rating = read_file()
    play_game(options, rating[name])

if __name__ == "__main__":
    main()

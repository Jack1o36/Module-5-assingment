from random import randint
START = 1
RANGE = 2
EXIT = 3
name = "dummy"
name2 = "stupid"
ranges = 1000


def main():

def display_menu():
    print("1: start")
    print("2: range")
    print("3: exit")
    choice = int(input(": "))
    
    if choice == 1:
        random_number_game()
    
    elif choice == 2:
        rangeselect()
    
    elif choice == 3:
        display_menu()
    
    else:
        print("give us real numbers please")
        display_menu()
def players_name():
    players = int(input("how many players (1-2): "))
    while players > 2 or players < 1:
        print("cant go that low")
        players = int(input("how many players (1-2): "))
    if players == 1:
        name = input("whats your name: ")
    if players == 2:
        name = input("whats your name: ")
        name2 = input("whats your name player 2: ")
    random_number_game()
def rangeselect():
    global ranges
    ranges = int(input("whats the range:(1-"))
    display_menu()
def random_number_game():
    numberai = randint(1, ranges)
    tries = 0
    print(f"Entering {name}")
    global number
    number = int(input("number: "))
    while number > numberai or number < numberai:
        if number < numberai:
            tries += 1
            print("gotta go higher")
            number = int(input("number: "))
        if number > numberai:
            tries += 1
            print("lower than that")
            number = int(input("number: "))
        if number <= 0:
            print("sorry we cant go that low")
        if number == numberai:
            print(f"good job you got it after {tries} tries")
    if number == numberai and tries < 1:
        print("you got it first try. thats a 1 in 1000")
        
    if players == 2:
        print(f"entering {name2}")
        numberai = randint(1, ranges)
        number = int(input("number: "))
    while number > numberai or number < numberai:
        if number < numberai:
            tries += 1
            print("gotta go higher")
            number = int(input("number: "))
        if number > numberai:
            tries += 1
            print("lower than that")
            number = int(input("number: "))
        if number <= 0:
            print("sorry we cant go that low")
        if number == numberai:
            print(f"good job you got it after {tries} tries")
    if number == numberai and tries < 1:
        print("you got it first try. thats a 1 in 1000")
    display_menu()

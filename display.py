import time
from menu import menu_map

print("Welcome to the music library.")
time.sleep(1)
print("In our programm you will be able to access and search your music library.")
time.sleep(1)

def display_menu():
    print(menu_map)
    answer = input("")
    while not answer.isdigit():
        print("You have entered an incorrect sign. Please try again :)")
        time.sleep(3)
        print(menu_map)
        answer = input("")

    return int(answer)

display_menu()


import time
from menu import menu_map
from music_reports import import_file
from music_reports import display_albums

list_albums = []
import_file(list_albums)
print(list_albums)

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

#display_menu()

def navigating(answer):
    if answer == 1:
        display_albums(list_albums) 
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        pass
    elif answer == 5:
        pass
    elif answer == 6:
        pass
    elif answer == 7:
        pass
    elif answer == 8:
        pass
    elif answer == 0:
        print("Goodbye!")
        return False # exiting program
    else: 
        print("Please enter a correct sign to access the library")
        time.sleep(2)
        display_menu()

is_open = True
while is_open == True:
    is_open = navigating(display_menu())

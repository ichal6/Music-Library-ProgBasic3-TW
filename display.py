import time
import os
from menu import menu_map
from menu import menu_visual
from music_reports import import_file
from music_reports import add_new_album
from music_reports import display_albums
from music_reports import find_albums_genre
from music_reports import find_time_range
from music_reports import by_album_name
from music_reports import by_artist
from music_reports import shortest_longest
from music_reports import editing_albums
from music_reports import save_to_file
from music_reports import suggesting
from music_reports import open_in_browser
from music_reports import full_report


def display_menu():
    os.system("clear")
    print(menu_visual)
    print(menu_map)
    answer = input("")
    while not answer.isdigit():
        print("You have entered an incorrect sign. Please try again :)")
        time.sleep(3)
        print(menu_map)
        answer = input("")
    os.system("clear")
    return int(answer)


def navigating(answer):
    print(menu_visual)
    if answer == 1:  # display all albums
        display_albums(list_albums)
    elif answer == 2:  # find by genre
        find_albums_genre(list_albums)
    elif answer == 3:  # find by time range
        find_time_range(list_albums)
    elif answer == 4:  # find the shortest title
        shortest_longest(list_albums, False)
    elif answer == 5:  # find the longest title
        shortest_longest(list_albums, True)
    elif answer == 6:  # find by name of artist
        by_artist(list_albums)
    elif answer == 7:  # find by album name
        by_album_name(list_albums)
    elif answer == 8:  # full report
        full_report(list_albums)
    elif answer == 9:  # view all similar music genres albums
        suggesting(list_albums)
    elif answer == 10:  # add new album
        add_new_album(list_albums)
        import_file(list_albums)
    elif answer == 11:  # edit album
        editing_albums(list_albums)
        albums = ""
        for disc in list_albums:
            albums += "{},{},{},{},{}\n".format(disc[0], disc[1], disc[2], disc[3], disc[4])
        save_to_file(albums)
    elif answer == 12:  # dodaj do menu
        open_in_browser(list_albums)
    elif answer == 0:  # exit
        print("Goodbye!")
        return False  # exiting program
    else:
        print("Please enter a correct sign to access the library")
        time.sleep(2)
        display_menu()
    input("Press enter by go to menu.")
    os.system("clear")
    return True


is_open = False
is_open_file = False  # checks if the file opened successfully
list_albums = []

is_open_file = import_file(list_albums)


if is_open_file:
    print(menu_visual)
    is_open = True
    print("Welcome to the music library.")
    time.sleep(1)
    print("In our programm you will be able to access and search your music library.\n")
    time.sleep(1)

while is_open:
    is_open = navigating(display_menu())

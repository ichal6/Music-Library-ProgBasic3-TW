import time
import os
from menu import menu_map
from menu import menu_statistics
from menu import menu_visual
from music_reports import import_file
from music_reports import add_new_album
from music_reports import display_albums
from music_reports import find_albums_genre
from music_reports import find_time_range
from music_reports import by_album_name
from music_reports import by_artist
from music_reports import shortest_longest
from music_reports import oldest_youngest
from music_reports import given_genres
from music_reports import editing_albums
from music_reports import save_to_file
from music_reports import suggesting
from music_reports import open_in_browser


is_open = False
is_open_file = False
list_albums = []

is_open_file = import_file(list_albums)

if is_open_file:
    print(menu_visual)
    is_open = True
    print("Welcome to the music library.")
    time.sleep(1)
    print("In our programm you will be able to access and search your music library.\n")
    time.sleep(1)


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
    if answer == 1:
        display_albums(list_albums)
    elif answer == 2:
        genre = input("Please input genre: ")
        find_albums_genre(list_albums, genre)
    elif answer == 3:
        from_time = input("Please input start year: ")
        while not from_time.isdigit():
            print("You have entered an incorrect sign. Please try again :)")
            time.sleep(3)
            from_time = input("Please input start year: ")
        from_time = int(from_time)

        to_time = input("Please input end year: ")
        while not to_time.isdigit():
            print("You have entered an incorrect sign. Please try again :)")
            time.sleep(3)
            to_time = input("Please input end year: ")
        to_time = int(to_time)

        list_range = [from_time, to_time]
        find_time_range(list_albums, list_range)
    elif answer == 4:
        shortest_longest(list_albums, False)
    elif answer == 5:
        shortest_longest(list_albums, True)
    elif answer == 6:
        artist = input("Please enter name of artist: ")
        by_artist(list_albums, artist)
    elif answer == 7:
        name_album = input("Please enter name of album: ")
        by_album_name(list_albums, name_album)
    elif answer == 8:
        print("Here you get full statistics about your library. Press number to display: ")
        print(menu_statistics)
        user_choice = input("")
        while not user_choice.isdigit():
            print("You have entered an incorrect sign. Please try again :)")
            time.sleep(1)
            print(menu_statistics)
            user_choice = input("")
        user_choice = int(user_choice)
        if user_choice == 1:
            shortest_longest(list_albums, False)
        elif user_choice == 2:
            shortest_longest(list_albums, True)
        elif user_choice == 3:
            oldest_youngest(list_albums, False)
        elif user_choice == 4:
            oldest_youngest(list_albums, True)
        elif user_choice == 5:
            display_albums(list_albums)
        elif user_choice == 6:
            given_genres(list_albums)
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


while is_open:
    is_open = navigating(display_menu())

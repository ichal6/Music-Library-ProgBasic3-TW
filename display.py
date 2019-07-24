import time
from menu import menu_map
from music_reports import import_file
from music_reports import display_albums
from music_reports import find_albums_genre
from music_reports import find_time_range
from music_reports import by_album_name
from music_reports import by_artist
from music_reports import shortest_longest

is_open = False
is_open_file = False
list_albums = []

is_open_file = import_file(list_albums)

if is_open_file:
    is_open = True
    print("Welcome to the music library.")
    time.sleep(1)
    print("In our programm you will be able to access and search your music library.")
    time.sleep(1)
    print(list_albums)


def display_menu():
    print(menu_map)
    answer = input("")
    while not answer.isdigit():
        print("You have entered an incorrect sign. Please try again :)")
        time.sleep(3)
        print(menu_map)
        answer = input("")

    return int(answer)

# display_menu()


def navigating(answer):
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
        pass
    elif answer == 0:
        print("Goodbye!")
        return False  # exiting program
    else:
        print("Please enter a correct sign to access the library")
        time.sleep(2)
        display_menu()
    input("Press enter by go to menu.")
    return True


while is_open:
    is_open = navigating(display_menu())

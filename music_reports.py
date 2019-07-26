import datetime
import os
import webbrowser
import time
from menu import menu_statistics


def import_file(list_albums, filename="text_albums_data.txt"):  # imports file
    try:
        with open(filename, "r") as fileopen:
            for line in fileopen:
                line = line.replace('\n', '')  # replace new line with an empty char
                list_albums.append(line.split(","))  # divides the line of text according to commas
            return list_albums
    except OSError:  # informs user if  can't find the file
        print("File '" + filename + "' not found!")
        return False


def list_to_string(list_item, length, index):  # prints strings instead of list
    element_albums = 0
    str_item = ""
    format_str = "{:>3}. "
    while element_albums < 5:

        format_str += ("{:>" + str(length[element_albums]) + "} ")  # prints elements eavenly
        element_albums += 1
    str_item = format_str.format(index, list_item[0], list_item[1], list_item[2], list_item[3], list_item[4])

    return str_item  # returns strings


def length_of_albums(list_albums, kind):  # chcecks the length of columns
    length = [0, 0, 0, 0, 0]
    col = 0
    while col < 5:
        for album in list_albums:
            if len(album[col]) > length[col]:
                if album[0].lower() == kind.lower():
                    length[col] = len(album[col])
                elif album[1].lower() == kind.lower():
                    length[col] = len(album[col])
                elif album[2].lower() == kind.lower():
                    length[col] = len(album[col])
                elif album[3].lower() == kind.lower():
                    length[col] = len(album[col])
                elif album[4].lower() == kind.lower():
                    length[col] = len(album[col])
                elif "empty" == kind:
                    length[col] = len(album[col])
        col += 1
    return length  # returns value for print table


def display_albums(list_albums):  # display all albums
    length = length_of_albums(list_albums, "empty")
    index = 1
    for disc in list_albums:
        print(list_to_string(disc, length, index))
        index += 1


def find_albums_genre(list_albums):  # finds albums by genre and print them accordint to length of genre
    genre = input("Please input genre: ")
    length = length_of_albums(list_albums, genre)
    is_not_genre_in_albums = True
    index = 1
    for disc in list_albums:
        if disc[3].lower() == genre.lower():
            print(list_to_string(disc, length, index))
            is_not_genre_in_albums = False
            index += 1  # used to display elements evenly, checks length of elements chosen
    if is_not_genre_in_albums:
        print("Your genre is not in albums.")


def find_time_range(list_albums):  # find albums released betweeen particular dates
    from_time = input("Please input start year: ")
    while not from_time.isdigit():
        print("You have entered an incorrect sign. Please try again :)")
        from_time = input("Please input start year: ")
    from_time = int(from_time)

    to_time = input("Please input end year: ")
    while not to_time.isdigit():
        print("You have entered an incorrect sign. Please try again :)")
        to_time = input("Please input end year: ")
    to_time = int(to_time)

    list_range = [from_time, to_time]
    length = length_of_albums(list_albums, "empty")
    is_not_in_album = True
    index = 1
    for disc in list_albums:
        if int(disc[2]) in range(list_range[0], list_range[1]):
            print(list_to_string(disc, length, index))
            is_not_in_album = False
            index += 1  # used to display elements evenly, checks length of elements chosen
    if is_not_in_album:
        print("No found album by your input years")


def take_time(element):  # used to sort elements by time
    return element[4]


def take_date(element):  # used to sort elements by date
    return int(element[2])


def shortest_longest(list_albums, is_long):  # displays the shortest or the longest album
    index_album = 0
    for album in list_albums:  # changes minutes to seconds
        time = album[4]
        (m, s) = time.split(':')
        list_albums[index_album][4] = int(m) * 60 + int(s)
        index_album += 1
    list_albums.sort(key=take_time)  # sorts by time
    index_album = 0
    for album in list_albums:  # turns seconds to hours
        list_albums[index_album][4] = str(datetime.timedelta(seconds=list_albums[index_album][4]))
        index_album += 1
    if is_long:
        print("The longest album is: " + str(list_albums[-1][1]) + " " + str(list_albums[-1][4]))
    else:
        print("The shortest album is: " + str(list_albums[0][1]) + " " + str(list_albums[0][4]))
    list_albums.clear()
    import_file(list_albums)  # imports the original list


def by_artist(list_albums):  # show album by particular artist
    name_artist = input("Please enter name of artist: ")
    length = length_of_albums(list_albums, name_artist)
    is_not_in_album = True
    index = 1
    for disc in list_albums:
        if disc[0].lower().find(name_artist.lower()) > -1:
            print(list_to_string(disc, length, index))
            is_not_in_album = False
            index += 1
    if is_not_in_album:
        print("No found album")


def by_album_name(list_albums):  # show album by album name
    name_album = input("Please enter name of album: ")
    length = length_of_albums(list_albums, name_album)
    is_not_in_album = True
    index = 1
    for disc in list_albums:
        if disc[1].lower().find(name_album.lower()) > -1:
            print(list_to_string(disc, length, index))
            is_not_in_album = False
            index += 1
    if is_not_in_album:
        print("No found album")


def oldest_youngest(list_albums, is_young):  # show album oldest/youngest
    list_albums.sort(key=take_date)
    if is_young:
        print("The youngest album is: " + str(list_albums[-1][1]) + " " + str(list_albums[-1][2]))
    else:
        print("The oldest album is: " + str(list_albums[0][1]) + " " + str(list_albums[0][2]))


def given_genres(list_albums):
    genres = set()
    for disc in list_albums:
        genres.add(disc[3])
    list_apperance = []

    for disc in list_albums:
        list_apperance.append(disc[3])

    index = 0

    apperance = [0] * len(genres)
    index = 0
    for genre in genres:
        apperance[index] = list_apperance.count(genre)
        index += 1

    index = 0
    genres = list((genres))
    while index < len(genres):
        print(genres[index] + " - " + str(apperance[index]))
        index += 1


def suggesting(list_albums):
    name_artist = input("Find me artist similar to (e.g. Britney Spears): ")
    is_not_in_album = True
    index = 0
    artist_index = 0
    for disc in list_albums:
        if disc[0].lower().find(name_artist.lower()) > -1:
            artist_index = index
            is_not_in_album = False
            genre = list_albums[artist_index][3]
            find_albums_genre(list_albums, genre)
            break
        else:
            index += 1
    if is_not_in_album:
        print("No found album")


def editing_albums(list_albums):
    display_albums(list_albums)
    length = len(list_albums)
    row = input("Please choose the album: ")
    while not row.isdigit() or int(row) > length or int(row) == 0:
        print("Please input a number of album")
        row = input("Please choose the album: ")
    row = int(row)
    row -= 1

    is_editinng = True
    while is_editinng:
        # print(menu_editting)
        # user_input = int(input(""))
        user_choice = input("Would you like to edit this name %s [Y]es/[N]o: " % list_albums[row][0])

        while user_choice.lower() != "y" and user_choice.lower() != "n":
            user_choice = input("Would you like to edit this name %s [Y]es/[N]o: " % list_albums[row][0])
        if user_choice.lower() == "y":
            name_artist = input("Please insert name of artist: ")
            list_albums[row][0] = name_artist

        user_choice = input("Would you like to edit this title %s [Y]es/[N]o: " % list_albums[row][1])

        while user_choice.lower() != "y" and user_choice.lower() != "n":
            user_choice = input("Would you like to edit this title %s [Y]es/[N]o: " % list_albums[row][1])
        if user_choice.lower() == "y":
            name_album = input("Please insert name of album: ")
            list_albums[row][1] = name_album

        user_choice = input("Would you like to edit this year %s [Y]es/[N]o: " % list_albums[row][2])

        while user_choice.lower() != "y" and user_choice.lower() != "n":
            user_choice = input("Would you like to edit this year %s [Y]es/[N]o: " % list_albums[row][2])
        if user_choice.lower() == "y":
            year_album = input("Please insert year of album: ")
            while not year_album.isdigit() or int(year_album) == 0:
                year_album = input("Please insert year of album: ")
            list_albums[row][2] = year_album

        user_choice = input("Would you like to edit this genre %s [Y]es/[N]o: " % list_albums[row][3])
        while user_choice.lower() != "y" and user_choice.lower() != "n":
            user_choice = input("Would you like to edit this genre %s [Y]es/[N]o: " % list_albums[row][3])
        if user_choice.lower() == "y":
            genre_album = input("Please insert genre of album: ")
            list_albums[row][3] = genre_album

        user_choice = input("Would you like to edit this time %s [Y]es/[N]o: " % list_albums[row][4])

        while user_choice.lower() != "y" and user_choice.lower() != "n":
            user_choice = input("Would you like to edit this time %s [Y]es/[N]o: " % list_albums[row][4])
        if user_choice.lower() == "y":
            minutes_album = input("Please insert minutes of album: ")
            while not minutes_album.isdigit() or int(minutes_album) > 1000000:
                minutes_album = input("Please insert minutes of album: ")
            seconds_album = input("Please insert seconds of album: ")
            while not seconds_album.isdigit() or int(seconds_album) >= 60:
                seconds_album = input("Please insert seconds of album: ")
            time_album = "{}:{}".format(minutes_album, seconds_album)
            list_albums[row][4] = time_album
        is_editinng = False
    albums = ""
    for disc in list_albums:
        albums += "{},{},{},{},{}\n".format(disc[0], disc[1], disc[2], disc[3], disc[4])
    return albums


def save_to_file(string_album, filename="text_albums_data.txt"):
    try:
        with open(filename, "w") as filewrite:
            filewrite.write(string_album)
            filewrite.close()
            with open(filename, "rb+") as filewrite:
                filewrite.seek(-1, os.SEEK_END)
                filewrite.truncate()
                filewrite.close()
            return True
    except OSError:
        print("File '" + filename + "' not found!")
        return False


def add_new_album(list_albums, filename="text_albums_data.txt"):
    artist_new_album = input("Please write artist of new album: ")
    name_new_album = input("Please write name of new album: ")
    year_new_album = input("Please input the year of publishment: ")
    while not year_new_album.isdigit() or int(year_new_album) == 0:
        year_new_album = input("Please input the year of publishment: ")
    genre_new_album = input("Please input genre of new album: ")

    minutes_duration = input("Please insert minutes duration of album: ")
    while not minutes_duration.isdigit() or int(minutes_duration) > 1000000:
        minutes_duration = input("Please insert minutes duration of album: ")
    seconds_duration = input("Please insert seconds duration of album: ")
    while not seconds_duration.isdigit() or int(seconds_duration) > 59:
        seconds_duration = input("Please insert seconds duration of album: ")
    duration = minutes_duration + ":" + seconds_duration

    new_album = "\n{},{},{},{},{}".format(artist_new_album, name_new_album, year_new_album, genre_new_album, duration)
    try:
        with open(filename, "a") as filewrite:
            filewrite.write(new_album)
            return True
    except OSError:
        print("File '" + filename + "' not found!")
        return False


def open_in_browser(list_albums):
    display_albums(list_albums)
    user_listen = input("If you'd like to listen to an album input its number: ")
    while not user_listen.isdigit() or int(user_listen) > len(list_albums) or int(user_listen) == 0:
        print("The number you have entered is not attached to any album.")
        user_listen = input("If you'd like to listen to an album input its number: ")
    user_listen = int(user_listen)
    user_listen -= 1
    user_listen = list_albums[int(user_listen)][0] + " " + list_albums[int(user_listen)][1]
    user_listen = user_listen.replace(" ", "+")
    link = "https://www.youtube.com/results?search_query=" + user_listen
    webbrowser.open(link)


def full_report(list_albums):
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

from menu import menu_editting
import datetime
import os


def import_file(list_albums, filename="text_albums_data.txt"):  # imports file
    try:
        with open(filename, "r") as fileopen:
            for line in fileopen:
                line = line.replace('\n', '')
                list_albums.append(line.split(","))
            fileopen.close()
            return list_albums
    except OSError:
        print("File '" + filename + "' not found!")
        return False


def list_to_string(list_item, length, index):  # prints strings instead of list
    element_albums = 0
    str_item = ""
    format_str = "{:>3}. "
    while element_albums < 5:

        format_str += ("{:>" + str(length[element_albums]) + "} ")
        element_albums += 1
    str_item = format_str.format(index, list_item[0], list_item[1], list_item[2], list_item[3], list_item[4])

    return str_item


def length_of_albums(list_albums, kind):
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
    return length


def display_albums(list_albums):  # display all albums
    length = length_of_albums(list_albums, "empty")
    index = 1
    for disc in list_albums:
        print(list_to_string(disc, length, index))
        index += 1


def find_albums_genre(list_albums, genre):  # finds albums by genre and print them accordint to length of genre
    length = length_of_albums(list_albums, genre)
    is_not_genre_in_albums = True
    index = 1
    for disc in list_albums:
        if disc[3].lower() == genre.lower():
            print(list_to_string(disc, length, index))
            is_not_genre_in_albums = False
            index += 1
    if is_not_genre_in_albums:
        print("Your genre is not in albums.")


# find_albums_genre(list_albums, "progressive rock")


def find_time_range(list_albums, list_range):
    length = length_of_albums(list_albums, "empty")
    is_not_in_album = True
    index = 1
    for disc in list_albums:
        if int(disc[2]) in range(list_range[0], list_range[1]):
            print(list_to_string(disc, length, index))
            is_not_in_album = False
            index += 1
    if is_not_in_album:
        print("No found album by your input years")


def take_time(element):
    return element[4]


def take_date(element):
    return int(element[2])


def shortest_longest(list_albums, is_long):
    index_album = 0
    for album in list_albums:
        time = album[4]
        (m, s) = time.split(':')
        list_albums[index_album][4] = int(m) * 60 + int(s)
        index_album += 1
    list_albums.sort(key=take_time)
    index_album = 0
    for album in list_albums:
        list_albums[index_album][4] = str(datetime.timedelta(seconds=list_albums[index_album][4]))
        index_album += 1
    if is_long:
        print("The longest album is: " + str(list_albums[-1][1]) + " " + str(list_albums[-1][4]))
    else:
        print("The shortest album is: " + str(list_albums[0][1]) + " " + str(list_albums[0][4]))
    list_albums.clear()
    import_file(list_albums)


# shortest_longest(list_albums, True)


def by_artist(list_albums, name_artist):  # show album by particular artist
    length = length_of_albums(list_albums, name_artist)
    is_not_in_album = True
    index = 1
    for disc in list_albums:
        if disc[0].lower() == name_artist.lower():
            print(list_to_string(disc, length, index))
            is_not_in_album = False
            index += 1
    if is_not_in_album:
        print("No found album")


def by_album_name(list_albums, name_album):  # show album by album name
    length = length_of_albums(list_albums, name_album)
    is_not_in_album = True
    index = 1
    for disc in list_albums:
        if disc[1].lower() == name_album.lower():
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

# additional functions


def suggesting(list_albums):
    name_artist = input("Find me artist similar to: ")
    is_not_in_album = True
    index = 0
    artist_index = 0
    for disc in list_albums:
        if disc[0].lower() == name_artist.lower():
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
    row = input("Please choose the album: ")
    while not row.isdigit():
        print("Please input a number of album")
        row = input("Please choose the album: ")
    row = int(row)
    row -= 1

    is_editinng = True
    while is_editinng:
        print(menu_editting)
        user_input = int(input(""))
        if user_input == 1:
            name_artist = input("Please insert name of artist: ")
            list_albums[row][0] = name_artist
        elif user_input == 2:
            name_album = input("Please insert name of album: ")
            list_albums[row][1] = name_album
        elif user_input == 3:
            name_year = input("Please insert year of album: ")
            list_albums[row][2] = name_year
        elif user_input == 4:
            genre = input("Please insert genre of album: ")
            list_albums[row][3] = genre
        elif user_input == 5:
            duration = input("Please insert duration of album: ")
            list_albums[row][4] = duration
        elif user_input == 0:
            is_editinng = False


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


def add_new_album(new_album, filename="text_albums_data.txt"):
    try:
        with open(filename, "a") as filewrite:
            filewrite.write(new_album)
            filewrite.close()
            return True
    except OSError:
        print("File '" + filename + "' not found!")
        return False

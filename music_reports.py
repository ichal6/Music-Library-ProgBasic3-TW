import datetime


def import_file(list_albums, filename = "text_albums_data.txt"): #imports file 
    try:
        with open(filename, "r") as fileopen:
            for line in fileopen:
                line = line.replace('\n', '')
                list_albums.append(line.split(","))
            fileopen.close()
    except OSError:
        print("File '" + filename + "' not found!")
    return list_albums


list_albums = []
import_file(list_albums)


def length_of_albums(list_albums, kind):
    length = [0, 0, 0, 0, 0]
    col = 0
    while col < 5:
        for album in list_albums:
            if len(album[col]) > length[col]:
                if album[0] == kind:
                    length[col] = len(album[col])
                elif album[1] == kind:
                    length[col] = len(album[col])
                elif album[2] == kind:
                    length[col] = len(album[col])
                elif album[3] == kind:
                    length[col] = len(album[col])
                elif album[4] == kind:
                    length[col] = len(album[col])
                elif "empty" == kind:
                    length[col] = len(album[col])        
        col += 1
    return length
    

def find_albums_genre(list_albums, genre): #finds albums by genre and print them accordint to length of genre 
    length = length_of_albums(list_albums, genre)
    print(length)
    for disc in list_albums:
        if disc[3] == genre:
            print(list_to_string(disc,length))


def count_albums_genre(list_albums, genre): #count albums by genre 
    amount = 0
    for disc in list_albums:
        if disc[3] == genre:
            amount += 1
    return amount


def list_to_string(list_item, length): #prints strings instead of list
    element_albums = 0
    str_item = ""
    format_str = ""
    while element_albums < 5:

        format_str += ("{:>" + str(length[element_albums]) + "} ")
        element_albums += 1
    str_item = format_str.format(list_item[0], list_item[1], list_item[2], list_item[3],list_item[4])
    
    return str_item

# find_albums_genre(list_albums, "progressive rock")


def find_time_range(list_albums, list_range):    #format_str.format(str_it    #format_str.format(str_item = str_item + list_item[element_albums] + " ")t_item[3],list_item[4])em = str_item + list_item[element_albums] + " ")t_item[3],list_item[4])
    length = length_of_albums(list_albums, "empty")
    print(length)
    for disc in list_albums:
        if int(disc[2]) in range(list_range[0], list_range[1]):
            print(list_to_string(disc, length))


def take_time(element):
    return element[4]


def take_date(element):
    return int(element[2])


def shortest_longest(list_albums, is_long):
    index_album = 0
    for album in list_albums:
        time = album[4]
        (m, s) = time.split(':')
        list_albums[index_album][4] = int(m) *60 + int(s)
        index_album += 1
    list_albums.sort(key=take_time)
    index_album = 0
    for album in list_albums:
        list_albums[index_album][4] = str(datetime.timedelta(seconds = list_albums[index_album][4]))
        index_album += 1
    if is_long:
        print("The longest album is: " + str(list_albums[-1][1]) + " " + str(list_albums[-1][4]))
    else: 
        print("The shortest album is: " + str(list_albums[0][1]) + " " +str(list_albums[0][4]))


# shortest_longest(list_albums, True)


def by_artist(list_albums, name_artist): # show album by particular artist
    length = length_of_albums(list_albums, name_artist)
    print(length)
    for disc in list_albums:
        if disc[0] == name_artist:
            print(list_to_string(disc, length))


def by_album_name(list_albums, name_album): # show album by album name
    length = length_of_albums(list_albums, name_album)
    print(length)
    for disc in list_albums:
        if disc[1] == name_album:
            print(list_to_string(disc, length))


def oldest_youngest(list_albums, is_young):# show album oldest/youngest
    list_albums.sort(key=take_date)
    print(list_albums)
    if is_young:
        print("The youngest album is: " + str(list_albums[-1][1]) + " " + str(list_albums[-1][2]))
    else:
        print("The oldest album is: " + str(list_albums[0][1]) + " " + str(list_albums[0][2]))


def display_albums(list_albums):# display all albums
    length = length_of_albums(list_albums, "empty")
    print(length)
    for disc in list_albums:
        print(list_to_string(disc, length))


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


given_genres(list_albums)

# additional functions

def suggesting(): #suggests similar albums/artists
    pass

def adding_albums():
    pass

def editing_albums():
    pass

def save_to_file():
    pass


list_range = [0, 1980]

# find_time_range(list_albums, list_range)

# print(list_albums)

# by_artist(list_albums, "Pink Floyd")

# by_album_name(list_albums, "The Dark Side Of The Moon")

# oldest_youngest(list_albums, True)

# display_albums(list_albums)

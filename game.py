import random as rd
import re
import os
import json
import urllib.request
import urllib.parse
import urllib.error
import time

hm = json.loads(open("hollywood_links.json").read())
bm = json.loads(open("bollywood_links.json").read())

def choice(): #1
    print("\t\t\nChoose Category: (1.)Hollywood OR (2.)Bollywood(Default)")
    if input("\nEnter your Choice: ") == "1": category = hm
    else: category = bm
    os.system('cls')
    return category

def call(db, index):
    headers = {"User-Agent": "Chrome/81.0.4044.122"}
    req = urllib.request.Request(url="http://www.omdbapi.com/?apikey=7a486a08&i=" + urllib.parse.quote(db[index]), headers=headers)
    try:
        res = urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        return str(e)
    except urllib.error.URLError as e:
        return str(e)
    else:
        return json.loads(res.read())

def alter(title):
    title = title.replace(" ","|")
    title = title.replace("...","")
    title = title.replace("!","")
    title = title.upper()
    return title

def find_all_indexes(input_str, search_str): #2
    l1 = []
    length = len(input_str)
    d = 0
    while d < length:
        j = input_str.find(search_str, d)
        if j == -1:
            return l1
        l1.append(j)
        d = j + 1
    return l1

def digitfinder(title): #3
    regex = '\d+'
    digit = re.findall(regex, title)
    if len(digit) != 0:
        return print('\nTitle contains Number(s)!\n', end='\n')

def display(title): #4
    name = []
    for char in title:
        if char in ['A', 'E', 'I', 'O', 'U']: name.append(char)
        elif char in ["|",":",",","'","(",")","."]: name.append(char)
        else: name.append("_")
    return name

counter = True
def hint(movie, i): #5
    global counter
    if i == 4 and counter == True:
        if input("\n\nDo you want a Hint?(Y/N):").upper() == "Y":
            counter = False
            return print("\nPlot of the movie:\n {}".format(movie['Plot']))
        else:
            counter = False      

def info(db): #6
	if input('\nDo you want Information on the movie? (Y/N):').upper() == "Y":
		print('\n{:6}{:>61}'.format('Title:',db['Title']))
		print('\n{:9}{:>58}'.format('Released:',db['Released']))
		print('\n{:6}{:>61}'.format('Genre:',db['Genre']))
		print('\n{:9}{:>58}'.format('Director:',db['Director']))
		print('\n{:7}{:>60}'.format('Actors:',db['Actors']))
		print('\n{:13}{:>54}'.format('ImDb Ratings:',db['imdbRating']))
		print('\n{:7}{:>60}'.format('Awards:',db['Awards']))
		return print("\n")
	else:
		return print("\n")

def guessed_ltr(ltr, guessedlist, realname): #7
    global max_attempts
    if len(guessedlist) >= 1:
        if (ltr in guessedlist) and (ltr not in realname):
            max_attempts += 1
            return print('\n*You have already tried this/these letter ' + str(guessedlist))
        else:
            return guessedlist.append(ltr)
    else: 
        return guessedlist.append(ltr)

exit_token = False
def fullname_attempt(ltr, title, movie): #8
    global max_attempts, exit_token
    if len(ltr) > 1:
        if ltr.replace(" ", "|") == title:
            exit_token = True
        else:
            print("\nYou guessed it wrong!")
            print("\nThe movie was:{}\n".format(movie['Title']))
            time.sleep(3)
            max_attempts = 0

max_attempts = 7
def hangman(): #9
    category = choice()
    while True:
        index = rd.randint(0, 897)
        movie = call(category, index)
        if type(movie) == str: pass
        elif type(movie) == dict and movie['Response'] == 'False': pass
        else: break
    title = alter(movie['Title'])
    realname = [char for char in title]
    guessedlist = []
    digitfinder(title)
    name = display(title)
    print()
    for ele in name:
    	print(ele, end=' ')
    global max_attempts
    max_attempts = 7
    while max_attempts > 0:
        hint(movie, max_attempts)
        print("\n"+"__" * len(title)+"\n")
        ltr = input('Enter your Guess: ').upper()
        guessed_ltr(ltr, guessedlist, realname)
        fullname_attempt(ltr, title, movie)
        if (len(ltr) == 1) and (ltr in realname):
            places = find_all_indexes(title, ltr)
            for place in places:
                name[place] = ltr
            print("\n")
        elif (len(ltr) == 1) and (ltr not in realname):
            max_attempts -= 1
            if max_attempts != 0:
                print('\nNot Found.\tRemaining Chances-> ',max_attempts)
                input("\nPress Enter to continue")
                print("\n\n")
            else:
                print("\nYou Lost!")
                print('\nThe movie was: {}\n'.format(movie['Title']))
                input("\nPress Enter to continue")
        os.system('cls')
        global exit_token
        if max_attempts != 0 and exit_token == False:
            for ele in name:
                print(ele, end=' ')
        if name == realname or exit_token == True:
            print("\nCorrect!\n\nThe movie was: {}".format(movie['Title']))
            info(movie)
            break
    return max_attempts*10


if __name__ == '__main__':
    hangman()
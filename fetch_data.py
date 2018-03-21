#Retrieve song texts from the web: works for song texts taken from www.songtexte.com (see line 22)

#needed libraries

import requests #to retrieve data from a page on a website, could also use urllib2 or scrapy
from bs4 import BeautifulSoup #to pull data out of html and xml files

#url_file is a file with only one column consisting of urls
#name_of_lyrics is the name of the txt file to which we write the "decomposed" lyrics

def lyrics(url_file, name_of_lyrics):
    try:
        with open(url_file, 'r') as f:
            links = [line.translate({ord(c): "" for c in '\n'}) for line in f.readlines()] #list of urls with songtext
        page = []
        for i in range(len(links)):
            if requests.get(links[i]).status_code == 200:  #if the page is downloaded correctly
                page.append(requests.get(links[i]))
    except:
        print('The first entry is not a valid file name')

    try:
        with open(name_of_lyrics, 'w') as f:
            for i in range(len(page)):
                soup = BeautifulSoup(page[i].text, 'html.parser')
                song = soup.find_all(id="lyrics")[0].get_text() #write only what is contained in the id="lyrics" to file (i.e. the songtexts)
                song = song.translate({ord(c): " " for c in '()""?!.,\n'}) #replace special symbols with spaces
                f.write(song.lower()) #add all text of the song with no capitalized letters to the file
    except:
        print('The second entry is not a valid file name')

#Create a new song with lyrics takes from a txt file previously created

#needed libraries: codecademy module for Markov Chains

from markov_python.cc_markov import MarkovChain

#lyrics_file is the name of the file with the lyrics, n is the number of time we run the generate_text function

def new_song(lyrics_file, n):

    mc = MarkovChain() #create an instance of MarkovChain
    mc.add_file(lyrics_file) #adding lyrics contained in lyrics_file to the Markov Chain
    new = [] #list that will contain the new text

    if n > 0:
        for i in range(int(n)):
            new += mc.generate_text() #output a list of words
        new = ["I" if x=="i" else "I'm" if x=="i'm" else x for x in new] #making the text nicer
        song = '\n'.join([' '.join(new[5 * i: 5 * i + 5]) for i in range(int(len(new) / 5))]) #making sentences of 5 words and then going to a new line
    else:
        print('The chosen number is not valid')
        song = ''
    return song

#Converting the text to speech

#needed libraries

import pyttsx

#songtext is a string

def read_out_loud(songtext):
    if isinstance(songtext, str):
        engine = pyttsx.init()
        engine.setProperty('rate', 30)
        engine.say(songtext)
        engine.runAndWait()
    else:
        engine = pyttsx.init()
        engine.setProperty('rate', 30)
        engine.say('I can\'t read your input')
        engine.runAndWait()


from fetch_data import *

#Create a song in the style of Paramore

lyrics('urls.csv', 'lyrics.txt')

new = new_song('lyrics.txt', 3)
print(new)

read_out_loud(new)



#possibly useful commands for debugging

#from pprint import pprint
#pprint(lyrics)
#print(soup.prettify())
#print(soup.find_all(id="lyrics"))
#print(lyrics)

#print(requests.get(url).text) #shows the content of the page

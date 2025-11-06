songs = ["hello","roar","sweat","weather"]
print (songs[0])
print (songs[1])
print (songs[2])
print (songs[3])

songs.sort()
print (songs[0])
print (songs[1])
print (songs[2])
print (songs[3])

songs.append("melody")
print ("there are "+str(len(songs))+" in the array")

songs.pop(2)
print(songs)
print(len(songs))
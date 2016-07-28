#!/usr/bin/python

import eyed3

"""
This is a sample code showing how to exercise python modules.
In this case we utilize the eyed3 python mp3 library 

Note: Read the datasource to get your environment setup

Run: pip install eyed3 to install eyed3 into your environment
"""


#parsing an audio file sample found in "samples/hotline_bling.mp3"
audiofile = eyed3.load("samples/hotline_bling.mp3")

print audiofile
"""
prints out digital signature of music file as an
object of eyed3: <eyed3.mp3.Mp3AudioFile object at 0xb6dc0e0c>

if you want to get more details on the music object,you can use the tag object

"""
print audiofile.tag.album
#prints out the track's album

print audiofile.tag.artist
#prints out the track's artist

print audiofile.tag.track_num
#prints out the track's number in the album else displays None


"""
You can also change an object's tag information by calling the save method
of the object. One also has to preceed the new tag names with 'u' because eyed3
library expects a unicode string.
"""
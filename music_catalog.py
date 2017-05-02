import sys

#my_file = open(sys.argv[1], "r") 

# a Song includes the title, artist, and album of a song
class Song:
   def __init__(self, title, artist, album):
      self.title = title #title of the song
      self.artist = artist #the artist of the song
      self.album = album #the album the song is on

   def __eq__(self, other):
      return((type(other) == Song)
            and self.title == other.title
            and self.artist == other.artist
            and self.album == other.album)
   def repr(self):
      return ("Song({!r}, {!r}, {!r})".format(self.title, self.artist, self.album))



def check_line_valid(line):
   pairs = 0
   for index in range(0, len(line)):
      if (index != 0) and (line[index] == "-") and (index + 2 < len(line)) and  (line[index + 1] == "-") \
            and (line[index + 2] != "-") and line[index - 1] != "-":
         pairs += 1
   if pairs == 2:
      return True
   else:
      return False

   
def make_song(line):
   string = ""
   section = 0 # 0 is title, 1 is artist, 2 is album
   song = Song(None, None, None)
   for index in range(0, len(line)):
       if line[index] != "-":
         string += line[index]
       elif line[index + 1] == "-":
         if section == 0:
            song.title = string
         elif section == 1:
            song.artist = string
         string = ""
         section += 1
       if index == len(line)- 1:
          song.album = string

   return song
         









def make_list(filename):
   index = 0
   new_list = None
   for line in filename:
      if line == "":
         pass
      #elif check_line_valid(line) == True:
         






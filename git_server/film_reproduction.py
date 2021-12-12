
# importing vlc module
import tkvlc
#import webbrowser
from time import sleep
import urllib.request
# importing pafy module
import pafy
import re
  
class Reproduce_Film:
    
    def __init__(self):
        pass
    
    def reproduce_trailer_film(self,name_film):
        #reconstructed_title = self.reconstruct_title(name_film)
        #search_url = "https://www.youtube.com/results?search_query=trailer"+reconstructed_title
        search_url = "https://www.youtube.com/results?search_query=trailer"+name_film+"&sp=EgIYAQ%253D%253D"
        html = urllib.request.urlopen(search_url)
        video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
        first_trailer = "https://www.youtube.com/watch?v="+video_ids[0]
          
        #exampleVideoURL = "https://sample-videos.com/video123/mp4/720/big_buck_bunny_720p_10mb.mp4"
        exampleVideoTitle = name_film
        exampleIconPath = "./movie_posters/ciak.ico"
        player = Player(video=first_trailer, title=exampleVideoTitle, iconPath=exampleIconPath)
        player.start()
        
    
    '''    
    def reproduce_trailer_film(self,name_film):
        #reconstructed_title = self.reconstruct_title(name_film)
        #search_url = "https://www.youtube.com/results?search_query=trailer"+reconstructed_title
        search_url = "https://www.youtube.com/results?search_query=trailer"+name_film+"&sp=EgIYAQ%253D%253D"
        html = urllib.request.urlopen(search_url)
        video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
        first_trailer = "https://www.youtube.com/watch?v="+video_ids[0]
          
       
        video = pafy.new(first_trailer)
          
        # getting best stream
        best = video.streams[0]
          
        # creating vlc media player object
        media = vlc.MediaPlayer(best.url)
          
        # start playing video
        media.play()

        sleep(5) # Or however long you expect it to take to open vlc
        while media.is_playing():
             sleep(1)
    '''
    def reproduce_easter_egg(self):
        
        video = pafy.new("https://www.youtube.com/watch?v=hf1DkBQRQj4")
          
        # getting best stream
        best = video.streams[0]
          
        # creating vlc media player object
        media = vlc.MediaPlayer(best.url)
          
        # start playing video
        media.play()

        sleep(5) # Or however long you expect it to take to open vlc
        while media.is_playing():
            sleep(1)

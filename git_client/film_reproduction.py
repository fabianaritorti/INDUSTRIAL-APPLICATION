
# importing vlc module
import tkvlc #per linux dovrebbe funzionare
#import vlc
from time import sleep
import urllib.request
import pafy
import re
import os
import pytube
  
class Reproduce_Film:
    
    def __init__(self):
        pass
          
    def download_trailer(self,name_film):
        try:
            os.remove('./film/'+ (os.listdir('./film/')[0]))
        except:
            pass
        search_url = "https://www.youtube.com/results?search_query=trailer"+name_film+"&sp=EgIYAQ%253D%253D"
        html = urllib.request.urlopen(search_url)
        video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
        first_trailer = "https://www.youtube.com/watch?v="+video_ids[0]
        yt = pytube.YouTube(first_trailer) 
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download('./film/')
    
    def reproduce_trailer_film(self,name_film):
        self.download_trailer(name_film)
        video_path = ('./film/'+ (os.listdir('./film/')[0]))
        exampleVideoTitle = name_film
        exampleIconPath = "./movie_posters/ciak.ico"
        player = tkvlc.Player(video=video_path, title=exampleVideoTitle, iconPath=exampleIconPath)        
        player.start()

# rf = Reproduce_Film()
# trailer= rf.download_trailer('_Indiana_Jones_and_the_Last_Crusade_(1989)')
# rf.reproduce_trailer_film('_Indiana_Jones_and_the_Last_Crusade_(1989)')




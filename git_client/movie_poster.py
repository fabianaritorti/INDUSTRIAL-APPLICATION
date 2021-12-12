from simple_image_download import simple_image_download as simp #pip install simple_image_download
import requests
import cv2
import matplotlib
import tkinter
from PIL import ImageTk, Image
import numpy as np
from IPython.display import display
import speech_recognition as sr
#from pynput.keyboard import Key, Controller
import numpy
from utilities import listen_phrase,get_num
from playsound import playsound
from utilities import control_number

class MoviePoster_Visualizer:

    def __init__(self):
        pass
    
    def get_correct_film_link(self,links):
        for link in links:
            if(link.split('/')[2]=='www.gstatic.com'):
                pass
            else:
                return link
        return "Not found"
    
    def horizontal_stack(self,images):
        dim = len(images)
        horizontal_images = images[0]
        if(dim==1):
            return horizontal_images
        else:
            for i in range(1,dim):
                horizontal_images = numpy.hstack((horizontal_images,images[i]))
            return horizontal_images
    
    def show_movie_posters(self,film_names,r,m):
        response = simp.simple_image_download
        links = []
        correct_films = []
        for film_name in film_names:
            film_urls = response().urls(film_name, 3)
            links.append(self.get_correct_film_link(film_urls))
        correctLinks_counter = 0
        film_counter = 0
        for url in links:
            if(url!="Not found"):
                correct_films.append(film_names[film_counter])
                img_data = requests.get(url).content
                with open('./movie_posters/image_'+str(correctLinks_counter)+'.jpg', 'wb') as handler:
                    handler.write(img_data)
                correctLinks_counter+=1
            film_counter+=1
        num_films = len(correct_films)
        posters = self.vertical_stack(num_films)
        root = tkinter.Tk()
        img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(posters, cv2.COLOR_BGR2RGB)))
        panel = tkinter.Label(root, image = img)
        panel.pack(side = "bottom", fill = "both",
                   expand = "yes")
        root.update()
        playsound('./audio/choose_film.mp3')
        numero_scelto = control_number(r,m)-1
        root.destroy()  
        return correct_films[numero_scelto]
            
    def vertical_stack(self,num_films):
        images = []
        for j in range(0,num_films):
            image = cv2.imread('./movie_posters/image_'+str(j)+'.jpg')
            dsize = (200, 300)
            resized_image = cv2.resize(image, dsize)
            images.append(resized_image)
        remaining = num_films%4
        if(remaining==0):
            num_rows = num_films//4
        else:
            num_rows = (num_films//4)+1
        if(num_rows==1):
            first_row = self.horizontal_stack(images[0:num_films])
            return first_row
        else:
            missing_images = ((num_rows-1)*4)-num_films
            for j in range(num_films,num_rows*4):
                image = cv2.imread('./movie_posters/black.jpg')
                image = resized_image = cv2.resize(image, dsize)
                images.append(resized_image)
            vertical_images = self.horizontal_stack(images[0:4])
            for i in range(1,num_rows):                
                low_extr = (i*4)
                high_extr = (i*4)+4
                horizontal_images = self.horizontal_stack(images[low_extr:high_extr])
                vertical_images = numpy.vstack((vertical_images,horizontal_images))
            return vertical_images
            
   
        
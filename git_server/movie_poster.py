from simple_image_download import simple_image_download as simp #pip install simple_image_download
import requests
import cv2
import matplotlib
import tkinter
from PIL import ImageTk, Image
import numpy as np
from IPython.display import display
import speech_recognition as sr
from pynput.keyboard import Key, Controller
import numpy

class MoviePoster_Visualizer:

    def __init__(self):
        pass
    
    def get_num(self,text):
        dict={
            'uno': 0,
            'due': 1,
            'tre': 2,
            'quattro': 3,
            'cinque': 4,
            'sei': 5,
            'sette': 6,
            'otto': 7,
            'nove': 8,
            'dieci': 9,
            'undici': 10,
            'dodici': 11,
            'tredici': 12,
            'quattordici': 13,
            'quindici': 14
        }
        try:
            return int(text)
        except:
            return dict.get(text, -1)
    
    def listen_phrase(self,r,m):
        #r = sr.Recognizer()
        text = ""
        audio = ""
        #with sr.Microphone() as source:
        with m as source:
            r.adjust_for_ambient_noise(source)
            while(audio==""):
                audio = r.listen(source)
            try:
                text = r.recognize_google(audio,language="it-IT")
            except Exception as e:
                print(e)
        print(text)
        return text
    
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
     
    def check_choice(self,root):
        # display the next file
        print("dimmi un numero")
        r = sr.Recognizer()
        r.dynamic_energy_treshold=True
        m = sr.Microphone()
        numero_scelto = self.listen_phrase(r,m)
        while(numero_scelto!='uno'):
            print("dimmi un numero")
            numero_scelto = self.listen_phrase(r,m)
        root.quit()
        # either reschedule to display the file, 
        # or quit if there are no more files to display
        
    
    def show_movie_posters(self,film_names):

        r = sr.Recognizer()
        r.dynamic_energy_treshold=True
        m = sr.Microphone()
        response = simp.simple_image_download

        #response().download('the_return_of_jedi_movie_poster', 1)

        print(film_names)
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
        print(correct_films)
        
        num_films = len(correct_films)
        
        posters = self.vertical_stack(num_films)
        root = tkinter.Tk()
  
        # loading the image
        img = ImageTk.PhotoImage(Image.fromarray(cv2.cvtColor(posters, cv2.COLOR_BGR2RGB)))
        panel = tkinter.Label(root, image = img)
  
        # setting the application
        panel.pack(side = "bottom", fill = "both",
                   expand = "yes")
                   
        r = sr.Recognizer()
        r.dynamic_energy_treshold=True
        m = sr.Microphone()
        print("dimmi un numero")
        root.update()
        numero_scelto = self.get_num(self.listen_phrase(r,m))
        while(numero_scelto==-1):
            #root.update()
            print("dimmi un numero")
            numero_scelto = self.get_num(self.listen_phrase(r,m))
        root.destroy()  
        return correct_films[numero_scelto]
        # running the application
        
        
        #posters = cv2.resize(posters, (0,0), fx=0.5, fy=0.5)
        #cv2.imshow("movie_posters", posters) 
        #waits for user to press any key 
        #(this is necessary to avoid Python kernel form crashing)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        
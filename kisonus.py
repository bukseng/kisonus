import tkinter
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from tkinter import *
import keyboard
import pygame


audio_map = {
    'None': 'None',
    'Load From Computer': None,
    'Mechanical A': 'res/mech_00.wav',
    'Mechanical B': 'res/mech_01.wav',
    'Mechanical C': 'res/mech_02.wav',
    'Mechanical D': 'res/mech_03.wav',
    'Mechanical E': 'res/mech_04.wav',
    'Mechanical F': 'res/mech_05.wav',
    'Mechanical G': 'res/wood_00.wav',
    'Vintage A': 'res/norm_00.wav',
    'Vintage B': 'res/norm_01.wav',
    'Vintage C': 'res/norm_02.wav',
    'Typewriter A': 'res/typw_00.wav',
    'Typewriter B': 'res/typw_01.wav',
    'Typewriter C': 'res/silent_00.wav',
    'Laptop A': 'res/laptop_00.wav',
    'Laptop B': 'res/laptop_01.wav'
}

def play_sound(audio_file, volume=1.0):
    pygame.mixer.init()
    audio = pygame.mixer.Sound(audio_file)
    audio.set_volume(volume)
    audio.play()

def custom_sound():
    if chosen.get() == 'Load From Computer':
        audio_map['Load From Computer'] = askopenfilename()

def on_key_press(event):
    if current_sound != 'None':
        play_sound(current_sound)
        
  
def changeSound(event):
    global current_sound
    custom_sound()
    current_sound = audio_map[chosen.get()]            

current_sound = 'None'

keyboard.on_press(on_key_press)


root = Tk()
root.geometry('300x30')
root.title('Kisonus')
root.iconbitmap('res/kisonus_icon.ico')
root.resizable(0,0)


options = [
    'None', 'Load From Computer', 'Mechanical A','Mechanical B','Mechanical C','Mechanical D','Mechanical E','Mechanical F','Mechanical G',
    'Vintage A', 'Vintage B', 'Vintage C', 'Typewriter A', 'Typewriter B', 'Typewriter C', 'Laptop A', 'Laptop B'
]

chosen = StringVar()
chosen.set('None')    
  
drop = OptionMenu( root, chosen, *options, command=changeSound)
drop.config(font=tkFont.Font(family='Calibri', size=16))
drop.pack()


root.mainloop()
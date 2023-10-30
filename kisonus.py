from tkinter import Tk, StringVar, OptionMenu
import tkinter.font as tkFont
from tkinter.filedialog import askopenfilename
from keyboard import on_press
from pygame import mixer


audio_map = {
    'None': None,
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

def load_audios(audio_map):
    mixer.init()
    return {audio_name: mixer.Sound(audio_file) if audio_file else None for audio_name, audio_file in audio_map.items()}

audios = load_audios(audio_map)

def custom_sound(event):
    if selected_sound.get() == 'Load From Computer':
        mixer.init()
        try:
            audios['Load From Computer'] = mixer.Sound(askopenfilename())
        except:
            pass

def play_sound(event):
    try:
        audios[selected_sound.get()].play()
    except:
        pass
        
  
on_press(play_sound)

root = Tk()
root.geometry('300x30')
root.title('Kisonus')
root.iconbitmap('res/kisonus_icon.ico')
root.resizable(0,0)

selected_sound = StringVar()
selected_sound.set('None')    
  
drop = OptionMenu( root, selected_sound, *audio_map.keys(), command=custom_sound)
drop.config(font=tkFont.Font(family='Calibri', size=16))
drop.pack()


root.mainloop()
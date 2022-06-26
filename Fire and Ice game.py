import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import *
import random
from random import randint
import time
import sys
from PIL import ImageTk, Image




#To Do List
# - Score/Collision System
# - Michael changes element
# - Import assets
# - Add music
# - Polish game


#Variables
file = "C:/Users/parag/Documents/Fire and Ice/characters/Michael_walking.gif"
# fileUsed = 0

# info = Image.open(file)
# frames = info.n_frames
# imgs = [PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
# myImage = PhotoImage(file=file)


direction = 'RIGHT'
change_to = direction
player_pos = [200,450]  #where michael starts


screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 5000, height = 1000, bg = "#0e2415")
canvas.grid()
score = 0


#ICE MICHAEL
#michael_Ice = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/characters/Michael_ice.gif", format="gif -index 2")
#michael_Ice = michael_Ice.subsample(2,2)
#canvas.create_image(player_pos, image = michael_Ice)

#FIRE MICHAEL
#michael_fire = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/characters/Michael_fire.gif", format="gif -index 2")

#michael_fire = michael_fire.subsample(2,2)





#FIRE OBSTACLE
#fire = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/fire_obstacle.gif", format="gif -index 2")
#fire = fire.subsample(2,2)
#canvas.create_image(player_pos, image = fire)

#ICE OBSTACLE
#ice = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/fire_obstacle.gif", format="gif -index 2")
#ice = ice.subsample(2,2)
#canvas.create_image(player_pos, image = ice)



#BACKGROUND IMAGE
background = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/caveBackground.png")
background = background.subsample(2,3)
canvas.create_image(0, 70, image=background, anchor=NW)




#This is michael image changing shit






#Functions

def create_pipe1(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe1")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe1")
    screen.after(30, move_pipe1)
    screen.after(2500, create_pipe2)

def move_pipe1():
    canvas.move("colored_pipe1", -5, 0)
    canvas.update()
    screen.after(30, move_pipe1)

def create_pipe2(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe2")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe2")
    screen.after(30, move_pipe2)
    screen.after(2500, create_pipe3)

def move_pipe2():
    canvas.move("colored_pipe2", -5, 0)
    canvas.update()
    screen.after(30, move_pipe2)

def create_pipe3(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe3")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe3")
    screen.after(30, move_pipe3)
    screen.after(1900, create_pipe4)

def move_pipe3():
    canvas.move("colored_pipe3", -5, 0)
    canvas.update()
    screen.after(30, move_pipe3)

def create_pipe4(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe4")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe4")
    screen.after(30, move_pipe4)
    screen.after(1800, create_pipe5)

def move_pipe4():
    canvas.move("colored_pipe4", -5, 0)
    canvas.update()
    screen.after(30, move_pipe4)

def create_pipe5(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe5")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe5")
    screen.after(30, move_pipe5)
    screen.after(2200, create_pipe6)

def move_pipe5():
    canvas.move("colored_pipe5", -5, 0)
    canvas.update()
    screen.after(30, move_pipe5)

def create_pipe6(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe6")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe6")
    screen.after(30, move_pipe6)
    screen.after(2600, create_pipe7)

def move_pipe6():
    canvas.move("colored_pipe6", -5, 0)
    canvas.update()
    screen.after(30, move_pipe6)

def create_pipe7(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe7")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe7")
    screen.after(30, move_pipe7)
    screen.after(2600, create_pipe8)

def move_pipe7():
    canvas.move("colored_pipe7", -5, 0)
    canvas.update()
    screen.after(30, move_pipe7)

def create_pipe8(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe8")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe8")
    screen.after(30, move_pipe8)
    screen.after(2600, create_pipe9)

def move_pipe8():
    canvas.move("colored_pipe8", -5, 0)
    canvas.update()
    screen.after(30, move_pipe8)

def create_pipe9(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe9")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe9")
    screen.after(30, move_pipe9)
    screen.after(2600, create_pipe10)

def move_pipe9():
    canvas.move("colored_pipe9", -5, 0)
    canvas.update()
    screen.after(30, move_pipe9)

def create_pipe10(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe10")
    else:
        canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe10")
    screen.after(30, move_pipe10)
    screen.after(2400, create_pipe1)

def move_pipe10():
    canvas.move("colored_pipe8", -5, 0)
    canvas.update()
    screen.after(30, move_pipe10)




#ice_michael = 1
#fire_michael = 0

#if xcoor obtacle=200 and obstaclecolor != michael color :
    #die


pygame.init()

#determine_pipes()
create_pipe1()
eventstart()



screen.mainloop()









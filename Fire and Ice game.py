import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import *
import random
from random import randint
import time
import sys
from PIL import ImageTk

#Step 1: Create canvas
#Step 2: Draw Characters
#Step 3: Import Characters
#Step 4: Make Characters do stuff


#Variables

direction = 'RIGHT'
change_to = direction
player_pos = [200,450]


screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 1000, height = 1000)
canvas.grid()
score = 0

background = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/caveBackground.png")
background = background.subsample(3,3)
canvas.create_image(10, 10, image=background, anchor=NW)




#This is michael
player = PhotoImage(file = "C:/Users/parag/Documents/Fire and Ice/characters/Michael.png")
frame2 = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/characters/Michael_walking.gif", format="gif -index 2")
player = player.subsample(2,2)
canvas.create_image(player_pos, image = frame2)



#Functions
def shoot(event): #shoots shit by making the bullet
    if event.keysym == 'space':
        canvas.create_circle(width = 10, fill="black", tag = "bullet")
        screen.after(100, shoot_after)

def shoot_after(): #moves the bullet
    canvas.move("shot", -20, 0)
    canvas.update()
    screen.after(100, shoot_after)

#global pipe_id

def create_pipe1(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe1")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe1")
    screen.after(20, move_pipe1)
    spawnrate = 1000
    spawnrate = randint(600,1000)
    screen.after(spawnrate, create_pipe2)

def move_pipe1():
    speed = randint(-30, -10)
    canvas.move("colored_pipe1", speed, 0)
    canvas.update()
    screen.after(20, move_pipe1)

def create_pipe2(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe2")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe2")
    screen.after(20, move_pipe2)
    spawnrate = 1000
    spawnrate = randint(600,1000)
    screen.after(spawnrate, create_pipe1)

def move_pipe2():
    speed = randint(-30, -10)
    canvas.move("colored_pipe2", speed, 0)
    canvas.update()
    screen.after(20, move_pipe2)
    
   
    



pygame.init()

create_pipe1()


screen.mainloop()









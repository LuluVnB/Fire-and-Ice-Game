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
canvas = Canvas(screen, width = 1000, height = 1000)
canvas.grid()
score = 0

background = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/caveBackground.png")
background = background.subsample(3,3)
canvas.create_image(10, 10, image=background, anchor=NW)




#This is michael
# michael = PhotoImage(file = "C:/Users/parag/Documents/Fire and Ice/characters/Michael.png")
michaelWalking = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/characters/Michael_walking.gif", format="gif -index 2")
michaelWalking = michaelWalking.subsample(2,2)
canvas.create_image(player_pos, image = michaelWalking)



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
    screen.after(randint(600,1000), create_pipe2)

def move_pipe1():
    speed = (-20)
    canvas.move("colored_pipe1", -20, 0)
    canvas.update()
    screen.after(20, move_pipe1)

def create_pipe2(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe2")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe2")
    screen.after(20, move_pipe2)
    screen.after(randint(600,1000), create_pipe1)

def move_pipe2():
    speed = (-20)
    canvas.move("colored_pipe2", speed, 0)
    canvas.update()
    screen.after(20, move_pipe2)


def animation(count):
    frames = info.n_frames
    im2 = imgs[count]
    count += 1
    if count == frames:
        count = 0   



   




    canvas.itemconfig(develon, image=im2)
    global anim

    anim = root.after(100, lambda: animation(count))
    
   
    



pygame.init()

create_pipe1()


screen.mainloop()









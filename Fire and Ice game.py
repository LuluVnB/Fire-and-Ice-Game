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
canvas = Canvas(screen, width = 5000, height = 1000, bg = "#0e2415")
canvas.grid()
score = 0


#ICE MICHAEL
michael_Ice = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/characters/Michael_ice.gif", format="gif -index 2")
michael_Ice = michael_Ice.subsample(2,2)
canvas.create_image(player_pos, image = michael_Ice)

#FIRE MICHAEL
michael_fire = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/characters/Michael_fire.gif", format="gif -index 2")
michael_fire = michael_fire.subsample(2,2)
canvas.create_image(player_pos, image = michael_fire)




#FIRE OBSTACLE
fire = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/fire_obstacle.gif", format="gif -index 2")
fire = fire.subsample(2,2)
canvas.create_image(player_pos, image = fire)

#ICE OBSTACLE
ice = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/fire_obstacle.gif", format="gif -index 2")
ice = ice.subsample(2,2)
canvas.create_image(player_pos, image = ice)



#BACKGROUND IMAGE
background = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/caveBackground.png")
background = background.subsample(2,3)
canvas.create_image(0, 70, image=background, anchor=NW)




#This is michael
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

# def determine_pipes():
#         pipe_color = random.randint(0,1)  
#         if pipe_color == 0:
#             canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe1")
#         else:
#             canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe1")  
#
    
def create_pipe1(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe1")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe1")
    screen.after(20, move_pipe1)
    screen.after(3000, create_pipe2)

def move_pipe1():
    canvas.move("colored_pipe1", -10, 0)
    canvas.update()
    screen.after(20, move_pipe1)

def create_pipe2(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe2")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe2")
    screen.after(20, move_pipe2)
    screen.after(2500, create_pipe3)

def move_pipe2():
    canvas.move("colored_pipe2", -10, 0)
    canvas.update()
    screen.after(20, move_pipe2)

def create_pipe3(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe3")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe3")
    screen.after(20, move_pipe3)
    screen.after(1000, create_pipe4)

def move_pipe3():
    canvas.move("colored_pipe3", -10, 0)
    canvas.update()
    screen.after(20, move_pipe3)

def create_pipe4(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe4")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe4")
    screen.after(20, move_pipe4)
    screen.after(1000, create_pipe5)

def move_pipe4():
    canvas.move("colored_pipe4", -10, 0)
    canvas.update()
    screen.after(20, move_pipe4)

def create_pipe5(): #makes pipe and randomly decides its color
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = "colored_pipe5")
    else:
        canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = "colored_pipe5")
    screen.after(20, move_pipe5)
    screen.after(1000, create_pipe1)

def move_pipe5():
    canvas.move("colored_pipe5", -10, 0)
    canvas.update()
    screen.after(20, move_pipe5)



# def determine_pipes():
#     pipe_color = random.randint(0,1)  
#     if pipe_color == 0:
#         canvas.create_rectangle(900, 0, 1000, 1000, image = fire, tag = "colored_pipe1")
#     else:
#         canvas.create_rectangle(900, 0, 1000, 1000, image = ice , tag = "colored_pipe1")  
#     move_pipe():
    
# def move_pipe():
#     x=1000
#     while(x>200):
#         canvas.move("colored_pipe1", -20, 0)
#         x-=20
#         canvas.update()
#         screen.after(20, move_pipe)
#     x=1000
#     determine_pipes()


# def create_pipe():

#         screen.after(1000, create_pipe2)

#         canvas.move("colored_pipe1", -20, 0)
#         x=1000
#         x-=-20
#         canvas.update()
#         screen.after(20, move_pipe1)
    

# def create_pipe1(): #makes pipe and randomly decides its color
#     pipe_color = random.randint(0,1)  
#     if pipe_color == 0:
#         canvas.create_rectangle(900, 0, 1000, 1000, image = fire, tag = "colored_pipe1")
#     else:
#         canvas.create_rectangle(900, 0, 1000, 1000, image = ice, tag = "colored_pipe1")
#     screen.after(20, move_pipe1)
#     screen.after(1000, create_pipe2)

# def move_pipe1():
#     canvas.move("colored_pipe1", -20, 0)
#     canvas.update()
#     screen.after(20, move_pipe1)

# def create_pipe2(): #makes pipe and randomly decides its color
#     pipe_color = random.randint(0,1)  
#     if pipe_color == 0:
#         canvas.create_rectangle(900, 0, 1000, 1000, image = fire, tag = "colored_pipe2")
#     else:
#         canvas.create_rectangle(900, 0, 1000, 1000, image = ice, tag = "colored_pipe2")
#     screen.after(20, move_pipe2)
#     screen.after(1000, create_pipe1)

# def move_pipe2():
#     canvas.move("colored_pipe2", -20, 0)
#     canvas.update()
#     screen.after(20, move_pipe2)

pygame.init()

create_pipe1()


screen.mainloop()









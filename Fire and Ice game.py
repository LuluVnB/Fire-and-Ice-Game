import pygame
from pygame.locals import *
import tkinter as tk #L Gian like fr :skull:
from tkinter import *

#Step 1: Create canvas
#Step 2: Draw Characters
#Step 3: Import Characters
#Step 4: Make Characters do stuff

#Variables
screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 1000, height = 1000)
canvas.grid()

player = canvas.create_rectangle(100, 100, 120, 120)



#Functions

def shoot(event): #shoots shit by making the bullet
    if event.keysym == 'space':
        canvas.create_circle(width = 10, fill="black", tag = "bullet")
        screen.after(100, shoot_after)

def shoot_after(): #moves the bullet
    canvas.move("shot", 0, 20)
    canvas.update()
    screen.after(100, shoot_after)


    
 











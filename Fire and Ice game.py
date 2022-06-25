import pygame
from pygame.locals import *
import tkinter as tk #L Gian like fr :skull:
from tkinter import *

#Step 1: Create canvas
#Step 2: Draw Characters
#Step 3: Import Characters
#Step 4: Make Characters do stuff



#Functions

def shoot(event):
    if event.keysym == 'space':
        bullet = canvas.coords
 








screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 1000, height = 1000)
canvas.grid()

x = 100
y = 100
player = canvas.create_rectangle(x, y)

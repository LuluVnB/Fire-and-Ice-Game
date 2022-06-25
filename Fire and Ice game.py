import pygame
from pygame.locals import *
import tkinter as tk #L Gian like fr :skull:
from tkinter import *

#Step 1: Create canvas
#Step 2: 


screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 1000, height = 1000)
canvas.grid()

x = 100
y = 100
player = canvas.create_rectangle(x, x, x + 10, y + 10)
 
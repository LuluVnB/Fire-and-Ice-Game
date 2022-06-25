import pygame
from pygame.locals import *
import tkinter as tk
from tkinter import *
import random
import time
import sys

#Step 1: Create canvas
#Step 2: Draw Characters
#Step 3: Import Characters
#Step 4: Make Characters do stuff


#Variables
direction = 'RIGHT'
change_to = direction
player_pos = [250,150]

screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 1000, height = 1000)
canvas.grid()
score = 0


#This is michael
player = PhotoImage(file = "C:/Users/parag/Documents/Fire and Ice/characters/Michael.png")
player = player.subsample(2,2)
canvas.create_image(player_pos, image = player)


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

def create_pipe(pipe_id): #makes pipe and randomly decides its color
    for i in range(pipe_id):
        pipe_color = random.randint(0,1)  
        global pipe_num
        pipe_num = str(pipe_id)
        
        if pipe_color == 0:
            canvas.create_rectangle(900, 0, 1000, 1000, fill = "red", tag = pipe_num)
        else:
            canvas.create_rectangle(900, 0, 1000, 1000, fill = "blue", tag = pipe_num)
        screen.after(100, move_pipe)

def move_pipe():
    canvas.move(pipe_num, -20, 0)
    canvas.update()
    screen.after(100, move_pipe)
    
   
    



pygame.init()


while True:
    create_pipe(3)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

                
                
    if direction == 'UP':
        player_pos[1] -= 10
    if direction == 'DOWN':
        player_pos[1] += 10
    if direction == 'LEFT':
        player_pos[0] -= 10
    if direction == 'RIGHT':
        player_pos[0] += 10



    screen.mainloop()









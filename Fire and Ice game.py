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
#file = "C:/Users/parag/Documents/Fire and Ice/characters/Michael_walking.gif"
# fileUsed = 0

# info = Image.open(file)
# frames = info.n_frames
# imgs = [PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
# myImage = PhotoImage(file=file)


direction = 'RIGHT'
change_to = direction
player_pos = [10,450]  #where michael starts


screen = tk.Tk()
title = screen.title("Fire and Ice")
canvas = Canvas(screen, width = 5000, height = 1000, bg = "#0e2415")
def next_gifter(event):
    global key
    key = event.char
    next_gif()
    eventCont()

canvas.bind('<Key>', next_gifter)
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
#fire = PhotoImage(file="C:/Users/parag/Documents/Fire and IceC:/Users/parag/Documents/Fire and Ice/imgs/fire_obstacle.gif", format="gif -index 2")
#fire = fire.subsample(2,2)
#canvas.create_image(player_pos, image = fire)

#ICE OBSTACLE
#ice = PhotoImage(file="C:/Users/parag/Documents/Fire and IceC:/Users/parag/Documents/Fire and Ice/imgs/fire_obstacle.gif", format="gif -index 2")
#ice = ice.subsample(2,2)
#canvas.create_image(player_pos, image = ice)



#BACKGROUND IMAGE
background = PhotoImage(file="C:/Users/parag/Documents/Fire and Ice/imgs/caveBackground.png")
background = background.subsample(2,3)
canvas.create_image(0, 70, image=background, anchor=NW)

#This is michael image changing shit

global michaelColor #current color of michael
michaelColor = 2

def canvcreate():
    global info
    global character
    global move_files
    global imgs
    

    move_files = ["C:/Users/parag/Documents/Fire and Ice/characters/Michael_walking.gif", "C:/Users/parag/Documents/Fire and Ice/characters/Michael_fire.gif","C:/Users/parag/Documents/Fire and Ice/characters/Michael_ice.gif"]
    file_Used = 0
    file = move_files[file_Used]

    info = Image.open(file)
    frames = info.n_frames

    imgs = [PhotoImage(file=file, format=f'gif -index {i}') for i in range(frames)]
    myImage = PhotoImage(file=file)
    myImage = myImage.subsample(5,5)
    character = canvas.create_image(200, 500, image=myImage)

def animationFire(count):
    global anim
    global info
    info = Image.open("imgs/fire_obstacle.gif")
    frames = info.n_frames

    imgs = [PhotoImage(file="imgs/fire_obstacle.gif", format=f'gif -index {i}') for i in range(frames)]
    myImage = PhotoImage(file="imgs/fire_obstacle.gif")
    myImage = myImage.subsample(5,5)
    character = canvas.create_image(200, 500, image=myImage)


    im2 = imgs[count]
    count += 1
    if count == frames: 
        count = 0
    
    canvas.itemconfig(character, image=im2)

    anim = screen.after(100, lambda: animation(count))


def animation(count):
    global anim
    global info
    frames = info.n_frames
    im2 = imgs[count]
    count += 1
    if count == frames: 
        count = 0
    
    canvas.itemconfig(character, image=im2)

    anim = screen.after(100, lambda: animation(count))


"""


"""

def next_gif():
    global imgs
    global fileUsed
    global file         
    global count
    global info
    global michaelColor
    if key == "n":          #normal michael
        michaelColor = 2
        file_Used = 0
        file = move_files[file_Used]
        
        
    
    if key == "f":          #fire michael
        michaelColor = 0
        file_Used = 1
        file = move_files[file_Used]
        

    if key == "i":          #ice michael
        michaelColor = 1
        file_Used = 2
        file = move_files[file_Used]
        
    
    info = Image.open(file)
    frames = info.n_frames
    imgs = [PhotoImage(file=file, format=f"gif -index {i}") for i in range(frames)]

    myImage = PhotoImage(file=file)
    canvas.itemconfigure(character, image=myImage )
    screen.after_cancel(anim)
    count = 0
    animation(count)

def eventstart():
    canvcreate()
    count = 0
    animation(count)

def eventCont():
    next_gif()
    count=0
    screen.after_cancel(anim)
    animation(count)

def death():
    canvas.delete("all")
    screen.after(1, death)
    game_over()
    #screen2 = tk.TK()
    #root.geometry(200x200)
    #root.title("GAME OVER")
    #root.backgroumd

def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, 'red')
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (1000/2, 1000/4)
    Canvas.fill('black')
    Canvas.blit(game_over_surface, game_over_rect)
    #show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(3)
    pygame.quit()
    sys.exit()

#collsion check

    
#Creating and moving pipes

def create_pipe1(): #creates new pipe and randomly decides its color
    global pipe1
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe1 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe1")
    else:
        pipe1 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe1")
    screen.after(30, move_pipe1) #recurses function to move pipe
    screen.after(2500, create_pipe2) #calls to create new pipe
    global color1
    color1 = pipe_color
    screen.after(1, check)
    
def move_pipe1(): #moves pipe
    canvas.move("colored_pipe1", -5, 0)
    canvas.update()
    screen.after(30, move_pipe1)

def create_pipe2(): #duplicate
    global pipe2
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe2 = canvas.create_image(1400, 0, 1500, 1000, image=myImage , tag = "colored_pipe2")
    else:
        pipe2 = canvas.create_rectangle(1400, 0, 1500, 1000, image="/imgs/ice_obstacle.png", tag = "colored_pipe2")
    screen.after(30, move_pipe2)
    screen.after(2500, create_pipe3)
    global color2
    color2 = pipe_color


def move_pipe2():
    canvas.move("colored_pipe2", -5, 0)
    canvas.update()
    screen.after(30, move_pipe2)

def create_pipe3(): #duplicate
    global pipe3
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe3 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe3")
    else:
        pipe3 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe3")
    screen.after(30, move_pipe3)
    screen.after(1900, create_pipe4)
    global color3
    color3 = pipe_color


def move_pipe3():
    canvas.move("colored_pipe3", -5, 0)
    canvas.update()
    screen.after(30, move_pipe3)

def create_pipe4(): #duplicate
    global pipe4
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe4 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe4")
    else:
        pipe4 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe4")
    screen.after(30, move_pipe4)
    screen.after(1800, create_pipe5)
    global color4
    color4 = pipe_color

def move_pipe4():
    canvas.move("colored_pipe4", -5, 0)
    canvas.update()
    screen.after(30, move_pipe4)

def create_pipe5(): #duplicate
    global pipe5
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe5 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe5")
    else:
        pipe5 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe5")
    screen.after(30, move_pipe5)
    screen.after(2200, create_pipe6)
    global color5
    color5 = pipe_color

def move_pipe5():
    canvas.move("colored_pipe5", -5, 0)
    canvas.update()
    screen.after(30, move_pipe5)

def create_pipe6(): #duplicate
    global pipe6
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe6 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe6")
    else:
        pipe6 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe6")
    screen.after(30, move_pipe6)
    screen.after(2600, create_pipe7)
    global color6
    color6 = pipe_color

def move_pipe6():
    canvas.move("colored_pipe6", -5, 0)
    canvas.update()
    screen.after(30, move_pipe6)

def create_pipe7(): #duplicate
    global pipe7
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe7 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe7")
    else:
        pipe7 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe7")
    screen.after(30, move_pipe7)
    screen.after(2600, create_pipe8)
    global color7
    color7 = pipe_color

def move_pipe7():
    canvas.move("colored_pipe7", -5, 0)
    canvas.update()
    screen.after(30, move_pipe7)

def create_pipe8(): #duplicate
    global pipe8
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe8 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe8")
    else:
        pipe8 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe8")
    screen.after(30, move_pipe8)
    screen.after(2600, create_pipe9)
    global color8
    color8 = pipe_color

def move_pipe8():
    canvas.move("colored_pipe8", -5, 0)
    canvas.update()
    screen.after(30, move_pipe8)

def create_pipe9(): #duplicate
    global pipe9
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe9 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe9")
    else:
        pipe9 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe9")
    screen.after(30, move_pipe9)
    screen.after(2600, create_pipe10)
    global color9
    color9 = pipe_color

def move_pipe9():
    canvas.move("colored_pipe9", -5, 0)
    canvas.update()
    screen.after(30, move_pipe9)

def create_pipe10(): #duplicate
    global pipe10
    pipe_color = random.randint(0,1)  
    if pipe_color == 0:
        pipe10 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "red", tag = "colored_pipe10")
    else:
        pipe10 = canvas.create_rectangle(1400, 0, 1500, 1000, fill = "blue", tag = "colored_pipe10")
    screen.after(30, move_pipe10)
    screen.after(2400, create_pipe1)
    global color10
    color10 = pipe_color

def move_pipe10():
    canvas.move("colored_pipe8", -5, 0)
    canvas.update()
    screen.after(30, move_pipe10)

#10 total pipes

#collision check

#ice = 1
#fire = 0
#if xcoor obtacle=200 and obstaclecolor != michael color :

def check():
    a = canvas.bbox(character)
    b = canvas.bbox(pipe1)
    if b[0] in range(a[0],a[2]) or b[2] in range(a[0],a[2]) and b[1] in range(a[1],a[3]) or b[3] in range(a[1],a[3]) and michaelColor != color1:
        screen.after(20, death)
    b = canvas.bbox(p2)
    # if b[0] in range(a[0],a[2]) or b[2] in range(a[0],a[2]) and b[1] in range(a[1],a[3]) or b[3] in range(a[1],a[3]) and michaelColor != color2:
    #     screen.after(20, death)
    screen.after(20, check)

pygame.init()

#determine_pipes()
create_pipe1()

#User_Input

canvas.focus_set()

#Create Character
eventstart()



screen.mainloop()









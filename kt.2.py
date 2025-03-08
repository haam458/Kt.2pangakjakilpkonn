import turtle
import random

kujundid = ["viisnurk, ruut, ring, suvaline"]

tegevus = input("Millist kujundit soovid joonistada (viisnurk, ruut, ring, suvaline): ")
korrad = int(input("Mitu kujundit soovid joonistada: "))
 
aken = turtle.Screen()
aken.setup(width=800, height=800)


def kujundviis(kujundid, korrad):
    for viisnurk in range(korrad):
       turtle.penup()
       turtle.goto(random.randint(-250, 250),random.randint(-250, 250))
       turtle.pendown()
       for viisnurk in range (5):
           turtle.forward(100)
           turtle.left(72)           

def kujundruut(kujundid, korrad):
    for ruut in range(korrad):
       turtle.penup()
       turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
       turtle.pendown()
       for ruut in range(4):
           turtle.forward(100)
           turtle.left(90)

def kujundring(kujundid, korrad):
    for ring in range(korrad):
        turtle.penup()
        turtle.goto(random.randint(-250, 250), random.randint(-250, 250))
        turtle.pendown()
        for ring in range(1):
            turtle.circle(50)

def kujundsuv(kujundid, korrad):
    for suvaline in range(1):
        kujundsuv = random.choice(["viisnurk", "ruut", "ring"])
        if kujundsuv == "viisnurk":
            kujundviis(kujundid, korrad)
        elif kujundsuv == "ruut":
            kujundruut(kujundid, korrad)
        elif kujundsuv == "ring":
            kujundring(kujundid, korrad)

def keha(tegevus, korrad):
    if tegevus == "viisnurk":
        kujundviis(kujundid, korrad)
    elif tegevus == "ruut":
        kujundruut(kujundid, korrad)
    elif tegevus == "ring":
        kujundring(kujundid, korrad)
    elif tegevus == "suvaline":
        kujundsuv(kujundid, korrad)

keha(tegevus, korrad)
turtle.done()


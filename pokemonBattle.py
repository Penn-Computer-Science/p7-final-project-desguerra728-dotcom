import random
import tkinter as tk

root = tk.Tk()
root.title("Pokemon Battle")

WIDTH = 1920
HEIGHT = 1080

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "white")
canvas.pack()

pika_img = "C:\Users\desguerra728\Documents\p7-final-project-desguerra728-dotcom\pika.png"

def make_img(image):
    img = tk.PhotoImage(file = image)
    return img

def spawn(x, y, image):
    
    


root.mainloop()
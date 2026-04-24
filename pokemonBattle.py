import random
import tkinter as tk

root = tk.Tk()
root.title("Pokemon Battle")

WIDTH = 1920
HEIGHT = 1080
img_dict = {}
pokemon = []

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "white")
canvas.pack()

def make_img(sprite_name, img_file, zoom):
    img = tk.PhotoImage(file = img_file)
    resized_img = img.subsample(zoom, zoom)
    img_dict[sprite_name] = resized_img

def spawn_sprite(sprite_name, img_file, zoom, x, y):
    make_img(sprite_name, img_file, zoom)
    p = canvas.create_image(x, y, image = img_dict[sprite_name], anchor = "sw")
    pokemon.append(p)

def gameloop():
        
    root.after(10, gameloop)

spawn_sprite("pikachu", "spriteImages\pika.png", 1, -100, HEIGHT)
spawn_sprite("pikachu2", "spriteImages\pikaFront.png", 2, 1200, 600)
gameloop()
root.mainloop()
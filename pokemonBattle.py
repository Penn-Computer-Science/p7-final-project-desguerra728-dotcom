import random
import tkinter as tk

root = tk.Tk()
root.title("Pokemon Battle")

WIDTH = 1920
HEIGHT = 1080
img_dict = {}
pokemon = []
background = []
option_count = []
x=0
y=1

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "white")
canvas.pack()

def make_img(sprite_name, img_file, zoom):
    global img_dict
    img = tk.PhotoImage(file = img_file)
    resized_img = img.subsample(zoom, zoom)
    img_dict[sprite_name] = resized_img

def spawn_sprite(sprite_name, img_file, zoom, x, y):
    make_img(sprite_name, img_file, zoom)
    p = canvas.create_image(x, y, image = img_dict[sprite_name], anchor = "sw")
    pokemon.append(p)

def place_img(img_name, img_file, zoom, x, y):
    make_img(img_name, img_file, zoom)
    bg = canvas.create_image(x, y, image = img_dict[img_name], anchor = "sw")
    background.append(bg)

def choose4(img_name, index, file0, file1, file2, file3):
    if x==0:
        if y==0:
            make_img(img_name, file0, 1)
        else:
            make_img(img_name, file1, 1)
    else:
        if y==0:
            make_img(img_name, file2, 1)
        else:
            make_img(img_name, file3, 1)
    background[index].config(img_dict[img_name])


def gameloop():
    choose4("options", 1, "spriteImages\Options\pokeOptions.png",
            "spriteImages\Options\FightOptions.png",
            "spriteImages\Options\RunOptions.png",
            "spriteImages\Options\RunOptions.png")
    root.after(10, gameloop)

def right_left(event):
    global x
    if x==0:
        x=+1
    else:
        x-=1
    return x

def up_down(event):
    global y
    if y==0:
        y+=1
    else:
        y-=1
    return y


root.bind("<Left>", right_left)
root.bind("<Right>", right_left)
root.bind("<Up>", up_down)
root.bind("<Down>", up_down)


spawn_sprite("pikachu", "spriteImages\pokemon\pika.png", 1, -100, HEIGHT-200)
spawn_sprite("pikachu2", "spriteImages\pokemon\pikafront.png", 2, 1300, 400)
place_img("dialogue bar", "spriteImages\dialogueBar.png", 1, 0, HEIGHT)
place_img("options", "spriteImages/Options/options.png", 1, 0, HEIGHT)

print(img_dict)
gameloop()
root.mainloop()
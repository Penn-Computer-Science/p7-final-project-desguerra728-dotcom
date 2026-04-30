import random
import tkinter as tk

root = tk.Tk()
root.title("Pokemon Battle")

WIDTH = 1920
HEIGHT = 1080
img_dict = {}
pokemon_list = []
background_list = []
option_count = []
next = False
x=0
y=1
choice = []
pokemon = False
fight = False
run = False
bag = False
choice = []

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
    pokemon_list.append(p)

def place_img(img_name, img_file, zoom, x, y):
    make_img(img_name, img_file, zoom)
    bg = canvas.create_image(x, y, image = img_dict[img_name], anchor = "sw")
    background_list.append(bg)

def choose4(img_name, index, file0, file1, file2, file3):
    global next, choice, x, y
    b = background_list[index]
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
    canvas.itemconfig(b, image = img_dict[img_name])
    choice = [x, y]


def gameloop():
    global next, pokemon, fight, run, bag, choice
    if not next:
        choose4("options", 1, "spriteImages\Options\pokeOptions.png",
                "spriteImages\Options\FightOptions.png",
                "spriteImages\Options\RunOptions.png",
                "spriteImages\Options\BagOptions.png")
    if next:
        x = choice[0]
        y = choice[1]
        if x==0:
            if y==0:
                pokemon = True
                fight = run = bag = False
            else:
                fight = True
                pokemon = run = bag = False
        else:
            if y==0:
                run = True
                pokemon = fight = bag = False
            else:
                bag = True
                pokemon = run = fight = False
    
    if pokemon:
        pass

    if fight:
        pass
    
    if run:
        pass
    if bag:
        pass

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

def enter(event):
    global next
    next = True

root.bind("<Left>", right_left)
root.bind("<Right>", right_left)
root.bind("<Up>", up_down)
root.bind("<Down>", up_down)
root.bind("<Return>", enter)

spawn_sprite("pikachu", "spriteImages\pokemon\pika.png", 1, -100, HEIGHT-200)
spawn_sprite("pikachu2", "spriteImages\pokemon\pikafront.png", 2, 1300, 400)
place_img("dialogue bar", "spriteImages\dialogueBar.png", 1, 0, HEIGHT)
place_img("options", "spriteImages/Options/options.png", 1, 0, HEIGHT)
canvas.create_text(400, HEIGHT-200, text="What will pikachu do?", fill = "#ffffff", font=("Arial", 40))

print(img_dict)
gameloop()
root.mainloop()
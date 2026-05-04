import random
import tkinter as tk

root = tk.Tk()
root.title("Pokemon Battle")

WIDTH = 1920
HEIGHT = 1080
img_dict = {}
p_item_list = []
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
player_pokemon = []

move_dict = {"Growl": [40, None], "ThunderShock": [30, 40], "Tail Whip": [30, None], "Thunder Wave": [20, None]}
# move name: [pp, power]
move_item_list = []

pokemon_dict = {"pikachu": [35, 
                            [35, 55, 40, 50, 50, 90], 
                            [move_dict["Growl"], 
                             move_dict["ThunderShock"], 
                             move_dict["Tail Whip"], 
                             move_dict["Thunder Wave"]]]}
# name: hp, [stats], [moveset]

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
    p_item_list.append(p)

def place_img(img_name, img_file, zoom, x, y):
    make_img(img_name, img_file, zoom)
    bg = canvas.create_image(x, y, image = img_dict[img_name], anchor = "sw")
    background_list.append(bg)

def choose4(img_name, index, file0, file1, file2, file3):
    #file0: 00, file1: 01, file2: 10, file3: 11
    global choice, x, y
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
    if not (next or (pokemon or fight or run or bag)):
        choose4("options", 1, "spriteImages\Options\pokeOptions.png",
                "spriteImages\Options\FightOptions.png",
                "spriteImages\Options\RunOptions.png",
                "spriteImages\Options\BagOptions.png")
        
    if next and not (pokemon or fight or run or bag):
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


    if fight and next:
        global dialogue, player_pokemon, move_item_list
        # name: hp, [stats], [moveset]
        player_pokemon = pokemon_dict["pikachu"]
        canvas.delete(dialogue)
        place_img("move options", "spriteImages\MoveOptions\m01.png", 1, 0, HEIGHT)
        #file0: 00, file1: 01, file2: 10, file3: 11
        move_item_list.append(canvas.create_text(300, HEIGHT-210, text="Growl", fill = "#252527", font=("Arial", 40)))
        move_item_list.append(canvas.create_text(950, HEIGHT-210, text="ThunderShock", fill = "#252527", font=("Arial", 40)))
        move_item_list.append(canvas.create_text(300, HEIGHT-100, text="Tail Whip", fill = "#252527", font=("Arial", 40)))
        move_item_list.append(canvas.create_text(950, HEIGHT-100, text="Thunder Wave", fill = "#252527", font=("Arial", 40)))

        choose4("move options", 1, "spriteImages\MoveOptions\m00.png",
                "spriteImages\MoveOptions\m01.png",
                "spriteImages\MoveOptions\m10.png",
                "spriteImages\MoveOptions\m11.png")

    if fight and not next:
        canvas.delete(move_item_list[0])
        canvas.delete(move_item_list[1])
        canvas.delete(move_item_list[2])
        canvas.delete(move_item_list[3])
        mx = choice[0]
        my = choice[1]
        if mx==0:
            if my==0:
                move0 = True
                move1 = move2 = move3 = False
            else:
                move1 = True
                move2 = move3 = move0 = False
        else:
            if my==0:
                move2 = True
                move1 = move3 = move0 = False
            else:
                move3 = True
                move0 = move1 = move2 = False
        
        

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
    next = not next

root.bind("<Left>", right_left)
root.bind("<Right>", right_left)
root.bind("<Up>", up_down)
root.bind("<Down>", up_down)
root.bind("<Return>", enter)

spawn_sprite("pikachu", "spriteImages\pokemon\pika.png", 1, -100, HEIGHT-200)
spawn_sprite("pikachu2", "spriteImages\pokemon\pikafront.png", 2, 1300, 400)
place_img("dialogue bar", "spriteImages\dialogueBar.png", 1, 0, HEIGHT)
place_img("options", "spriteImages/Options/options.png", 1, 0, HEIGHT)
dialogue = canvas.create_text(400, HEIGHT-200, text="What will pikachu do?", fill = "#ffffff", font=("Arial", 40))

print(img_dict)
gameloop()
root.mainloop()
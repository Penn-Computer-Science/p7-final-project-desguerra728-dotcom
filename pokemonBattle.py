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

stage = "start"

class Moves:
    def __init__(self, name, pp, effect, power):
        self.name =  name
        self.pp = pp
        self.effect = effect
        self.power = power

class Pokemon:
    def __init__(self, name, stats, moveset):
        self.name = name
        self.stats = stats
        self.moveset = moveset

    def use_move(self, opponent, move):
        move.pp -= 1

        # damage = ((((2*level*critical)/5)*power*a/d)/50+2)*STAB*type1*type2*rand
        rand=random.randint(217,255)
        d=opponent.stats[2]
        a=self.stats[1]
        power=move.power

        damage = ((((2)/5)*power*a/d)/50+2)*rand/225

        print(opponent.stats[0])
        opponent.stats[0] -= damage
        print(opponent.stats[0])


growl = Moves("Growl", 40, "neg att", 0)
thundershock = Moves("Thundershock", 30, None, 40)
tail_whip = Moves("Tail Whip", 30, "neg def", 0)
thunder_wave = Moves("Thunder Wave", 20, "paralyze", 0)
pikachu_moveset = [growl, thundershock, thunder_wave, tail_whip]

pikachu = Pokemon("Pikachu", [35, 55, 40, 50, 50, 90], pikachu_moveset)
pikachu2 = Pokemon("Pikachu2", [35, 55, 40, 50, 50, 90], pikachu_moveset)
# stats: hp attk def spattk, spdef, speed

canvas = tk.Canvas(root, width = WIDTH, height = HEIGHT, bg = "white")
canvas.pack()

move_item_list = []

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
    global next, choice, stage, move_item_list
    if stage == "start" and not next:
        choose4("options", 1, "spriteImages\Options\pokeOptions.png",
                "spriteImages\Options\FightOptions.png",
                "spriteImages\Options\RunOptions.png",
                "spriteImages\Options\BagOptions.png")
        
    if next and stage == "start":
        x = choice[0]
        y = choice[1]
        if x==0:
            if y==0:
                stage = "pokemon"
            else:
                stage = "fight"
        else:
            if y==0:
                stage = "run"
            else:
                stage = "bag"

        next = False
    
    if stage == "pokemon":
        pass

    if stage == "fight" and not next:
        global dialogue, player_pokemon, move_item_list
        # name: hp, [stats], [moveset]
        # canvas.delete(dialogue)
        canvas.itemconfig(dialogue, text="")
        place_img("move options", "spriteImages\MoveOptions\m01.png", 1, 0, HEIGHT)
        #file0: 00, file1: 01, file2: 10, file3: 11

        a=0
        for i in range(3):
            if i<2:
                move_item_list.append(canvas.create_text(300+a, HEIGHT-210, text=pikachu.moveset[i].name, fill = "#252527", font=("Arial", 40)))
                a=650
            else:
                move_item_list.append(canvas.create_text(300+a, HEIGHT-100, text=pikachu.moveset[i].name, fill = "#252527", font=("Arial", 40)))
                move_item_list.append(canvas.create_text(300, HEIGHT-100, text=pikachu.moveset[i+1].name, fill = "#252527", font=("Arial", 40)))

        choose4("move options", 1, "spriteImages\MoveOptions\m00.png",
                "spriteImages\MoveOptions\m01.png",
                "spriteImages\MoveOptions\m10.png",
                "spriteImages\MoveOptions\m11.png")

    if stage == "fight" and next:
        for item in move_item_list:
            canvas.delete(item)
            move_item_list.remove(item)
        canvas.delete(background_list[1])
        x = choice[0]
        y = choice[1]
        if x==0:
            if y==0:
                canvas.itemconfig(dialogue, text="Pikachu used " + pikachu.moveset[3].name + "!")
                move = pikachu.moveset[3]

            else:
                canvas.itemconfig(dialogue, text="Pikachu used " + pikachu.moveset[0].name + "!")
                move = pikachu.moveset[0]
        else:
            if y==0:
                canvas.itemconfig(dialogue, text="Pikachu used " + pikachu.moveset[2].name + "!")
                move = pikachu.moveset[2]
            else:
                canvas.itemconfig(dialogue, text="Pikachu used " + pikachu.moveset[1].name + "!")
                move = pikachu.moveset[1]

        pikachu.use_move(pikachu2, move)

        r = random.randint(0,3)

        canvas.itemconfig(dialogue, text="Pikachu2 used " + pikachu2.moveset[r] + "!")
        pikachu2.use_move(pikachu, pikachu2.moveset[r])

        next = False

    if stage == "run":
        pass
    if stage =="bag":
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
dialogue = canvas.create_text(400, HEIGHT-200, text="What will pikachu do?", fill = "#ffffff", font=("Arial", 40))

print(img_dict)
gameloop()
root.mainloop()
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
substage = ""
move = None
move2 = None
white = None
hh = None
pp_text = None
type = None
count = 0

def max(num, numTwo):
    if num >= numTwo:
        return num
    else:
        return numTwo
    
def multiplier(stat_stage):
    return (max(2, 2+stat_stage)/max(2, 2-stat_stage))

class Moves:
    def __init__(self, name, pp, effect, power, type, original_pp):
        self.name =  name
        self.pp = pp
        self.effect = effect
        self.power = power
        self.type = type
        self.original_pp = original_pp


# thunder_wave = Moves("Thunder Wave", 20, "paralyze", 0)

class Pokemon:
    def __init__(self, name, hp, stats, moveset, stat_stage):
        self.name = name
        self.hp = hp
        self.stats = stats
        self.moveset = moveset
        self.stat_stage = stat_stage

    def use_move(self, opponent, move):
        global next
        if move == None:
            return
        
        if move.pp == 0: 
            next = not next
            return
        
        move.pp -= 1

        if move.effect != None:
            if move.effect == "neg att":
                if opponent.stat_stage[1] > -6:
                    opponent.stat_stage[1] -= 1
                    opponent.stats[1] *= multiplier(opponent.stat_stage[1])

            if move.effect == "neg def":
                if opponent.stat_stage[2] > -6:
                    opponent.stat_stage[2] -= 1
                    opponent.stats[2] *= multiplier(opponent.stat_stage[2])

        # damage = ((((2*level*critical)/5)*power*a/d)/50+2)*STAB*type1*type2*rand
        rand=random.randint(217,255)
        d=opponent.stats[2]
        a=self.stats[1]
        power=move.power

        if power == 0:
            damage =0
        else:
            damage = (((2/5)*power*a/d)/50+2)*rand/225

        opponent.stats[0] -= damage
        if opponent.stats[0] <0:
            opponent.stats[0] = 0

        print(self.name + ": " + str(self.stat_stage))
        print(self.stats)
        print()

growl = Moves("Growl", 40, "neg att", 0, "Normal", 40)
thundershock = Moves("Thundershock", 30, None, 40, "Electric", 30)
tail_whip = Moves("Tail Whip", 30, "neg def", 0, "Normal", 20)
thunder_wave = Moves("Thunder Wave", 20, "paralyze", 0, "Electric", 20)
pikachu_moveset = [growl, thundershock, thunder_wave, tail_whip]

pikachu = Pokemon("Pikachu", 35, [35, 55, 40, 50, 50, 90], pikachu_moveset, [0,0,0,0,0,0])
pikachu2 = Pokemon("Pikachu2", 35, [35, 55, 40, 50, 50, 90], pikachu_moveset, [0,0,0,0,0,0])
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

def choose4move(img_name, index, file0, file1, file2, file3):
    #file0: 00, file1: 01, file2: 10, file3: 11
    global choice, x, y, opp_text, pp_text, type
    b = background_list[index]
    if x==0:
        if y==0:
            make_img(img_name, file0, 1)
            canvas.itemconfig(opp_text, text=tail_whip.original_pp)
            canvas.itemconfig(pp_text, text=tail_whip.pp)
            canvas.itemconfig(type, text=tail_whip.type)
        else:
            make_img(img_name, file1, 1)
            canvas.itemconfig(opp_text, text=growl.original_pp)
            canvas.itemconfig(pp_text, text=growl.pp)
            canvas.itemconfig(type, text=growl.type)
    else:
        if y==0:
            make_img(img_name, file2, 1)
            canvas.itemconfig(opp_text, text=thunder_wave.original_pp)
            canvas.itemconfig(pp_text, text=thunder_wave.pp)
            canvas.itemconfig(type, text=thunder_wave.type)
        else:
            make_img(img_name, file3, 1)
            canvas.itemconfig(opp_text, text=thundershock.original_pp)
            canvas.itemconfig(pp_text, text=thundershock.pp)
            canvas.itemconfig(type, text=thundershock.type)
    canvas.itemconfig(b, image = img_dict[img_name])
    choice = [x, y]

def choose4(img_name, index, file0, file1, file2, file3):
    #file0: 00, file1: 01, file2: 10, file3: 11
    global choice, x, y, opp_text, pp_text, type
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
    global next, choice, stage, move_item_list, substage, move, dialogue, move2, sec_dialogue, white, hh, pp_text, type, opp_text, count
    count+=1
    if substage != "aftermath":
        if count%2==0:
            canvas.move(p_item_list[0], 0, -5)
        else:
            canvas.move(p_item_list[0], 0, 5)

    if substage == "aftermath":
        if count%2==0:
            canvas.move(p_item_list[1], 0, -5)
        else:
            canvas.move(p_item_list[1], 0, 5)


    if stage == "start" and not next:
        canvas.itemconfig(hh, text = "")
        canvas.tag_raise(background_list[1], background_list[0])
        canvas.tag_lower(white)

        choose4("options", 1, "spriteImages/Options/pokeOptions.png",
                "spriteImages/Options/FightOptions.png",
                "spriteImages/Options/RunOptions.png",
                "spriteImages/Options/BagOptions.png")
        substage = ""
        
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
    
    if stage == "pokemon":
        canvas.tag_raise(white)
        canvas.itemconfig(hh, text = "You only have pikachu")
        canvas.tag_raise(hh)
        stage = "start"

    if stage == "fight" and next and substage != "aftermath":
        canvas.itemconfig(sec_dialogue, text = "")
        canvas.itemconfig(dialogue, text="")
        place_img("move options", "spriteImages/MoveOptions/m01.png", 1, 0, HEIGHT)
        #file0: 00, file1: 01, file2: 10, file3: 11

        a=0
        for i in range(3):
            if i<2:
                
                move_item_list.append(canvas.create_text(300+a, HEIGHT-210, text=pikachu.moveset[i].name, fill = "#252527", font=("Arial", 40)))
                a=650
            else:
                move_item_list.append(canvas.create_text(300+a, HEIGHT-100, text=pikachu.moveset[i].name, fill = "#252527", font=("Arial", 40)))
                move_item_list.append(canvas.create_text(300, HEIGHT-100, text=pikachu.moveset[i+1].name, fill = "#252527", font=("Arial", 40)))

        choose4move("move options", 1, "spriteImages/MoveOptions/m00.png",
                "spriteImages/MoveOptions/m01.png",
                "spriteImages/MoveOptions/m10.png",
                "spriteImages/MoveOptions/m11.png")

    if stage == "fight" and not next:
        canvas.itemconfig(pp_text, text = "")
        canvas.itemconfig(opp_text, text = "")
        canvas.itemconfig(type, text = "")
        for item in move_item_list:
            canvas.delete(item)
        move_item_list.clear()
        if background_list:
            canvas.tag_raise(background_list[0], background_list[1])
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

        if move.effect != None:
            if move.effect == "neg att":
                canvas.itemconfig(sec_dialogue, text="pikachu2's attack fell!")
            if move.effect == "neg def":
                canvas.itemconfig(sec_dialogue, text="pikachu2's def fell!")
            if move.effect == "paralyze":
                canvas.itemconfig(sec_dialogue, text="Nothing happened!")

        move2 = random.choice(pikachu2.moveset)

        substage = "aftermath"

    if substage == "aftermath" and next:
        canvas.itemconfig(sec_dialogue, text = "")

        stage = "start"
        next = False
        substage = ""

        pikachu.use_move(pikachu2, move)
        move = None
        change = (pikachu.hp-pikachu.stats[0])/pikachu.hp*350
        canvas.coords(hp1, 250, 195, 600-change, 225)
        
        if pikachu.stats[0] == 0:
            canvas.itemconfig(dialogue, text = "pikachu fainted")
            canvas.itemconfig(sec_dialogue, text="")
            stage = "end"

        else:
            pikachu2.use_move(pikachu, move2)
            if move2 != None:
                canvas.itemconfig(dialogue, text="Pikachu2 used " + move2.name + "!")
                if move2.effect != None:
                    if move2.effect == "neg att":
                        canvas.itemconfig(sec_dialogue, text="pikachu's attack fell!")
                    if move2.effect == "neg def":
                        canvas.itemconfig(sec_dialogue, text="pikachu's def fell!")
                    if move2.effect == "paralyze":
                        canvas.itemconfig(sec_dialogue, tex= "Nothing happened!")
            move2 = None
            change = (pikachu2.hp-pikachu2.stats[0])/pikachu2.hp*350
            canvas.coords(hp2, 1430, 670, 1780-change, 700)

            if pikachu2.stats[0] == 0:
                canvas.itemconfig(dialogue, text = "pikachu2 fainted")
                canvas.itemconfig(sec_dialogue, text="")
                stage = "end"

    if stage == "run" and next:
        canvas.tag_raise(background_list[0], background_list[1])
        canvas.itemconfig(dialogue, text="Pikachu can't escape!")
        canvas.itemconfig(sec_dialogue, text="")
        move2 = random.choice(pikachu2.moveset)
        
    if stage == "run" and not next:
        substage = "aftermath"
        next = True

    if stage == "bag" and next:
        canvas.tag_raise(white)
        canvas.itemconfig(hh, text = "Your bag is empty.")
        canvas.tag_raise(hh)
        stage = "start"
    
    if stage == "end" and next:
        canvas.delete("all")
        if pikachu.stats[0]==0:
            canvas.create_text(400, HEIGHT-200, text="You lost the battle",font=("Arial", 60))
        else:
            canvas.create_text(400, HEIGHT-200, text="You won the battle",font=("Arial", 60))
            
        return


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
root.bind("<space>", enter)


white=canvas.create_rectangle(0,0,WIDTH, HEIGHT, fill="white")
hh=canvas.create_text(200, 200, text="",font=("Arial", 30))
spawn_sprite("pikachu", "spriteImages/pokemon/pika.png", 1, -100, HEIGHT-200)
spawn_sprite("pikachu2", "spriteImages/pokemon/pikafront.png", 2, 1300, 400)
place_img("dialogue bar", "spriteImages/dialogueBar.png", 1, 0, HEIGHT)
place_img("options", "spriteImages/Options/options.png", 1, 0, HEIGHT)
hp1 = canvas.create_rectangle(250, 195, 600, 225, fill = "#09963F", width=0)
hp2 = canvas.create_rectangle(1430, 670, 1780, 700, fill = "#09963F", width =0)
dialogue = canvas.create_text(400, HEIGHT-200, text="What will pikachu do?", fill = "#ffffff", font=("Arial", 40))
sec_dialogue = canvas.create_text(400, HEIGHT-150, text="", fill = "#ffffff", font=("Arial", 40))
type =canvas.create_text(1750, 1000, text = "", fill = "black", font=("Arial", 50))
pp_text =canvas.create_text(1650, 880, text = "", fill = "black", font=("Arial", 50))
opp_text =canvas.create_text(1790, 880, text = "", fill = "black", font=("Arial", 50))
print(img_dict)
gameloop()
root.mainloop()
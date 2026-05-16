import readchar
import os
from random import randint
from datetime import datetime

print("Use as flechas ← → para jogar ou q para sair:")

lines = []

start = datetime.now()

def addlines(lines, start=False):
    if(randint(0, 10) > 7):
        lin = "="*5 + "|" + " "*5
    elif(randint(0, 10) < 3):
        lin = " "*5 + "|" + "="*5
    else:
        lin = " "*5 + "|" + " "*5
    if(start):
        return [lin] + lines
    else:
        return lines + [lin]
  
def endgame():
    print("score: " + str(score))
    print("tempo: " + str(datetime.now()-start))
    if not(os.path.exists("highscore.txt")):
        with open("highscore.txt", "w") as f:
    	    f.write("0")
    with open("highscore.txt", "r") as f:
        c = f.read()
        if(c):
            hs = int(c)
        else:
    	    hs = 0
    if(score > hs):
        print("novo recorde!")
        with open("highscore.txt", "w") as f:
    	    f.write(str(score))
    else:
    	print("recorde: " + str(hs))

for i in range(10):
    lines = addlines(lines, start=False)

score = 0

while True:
    for line in lines:
        print(line)
    keypress = readchar.readkey()
    os.system("clear")
    
    if keypress == readchar.key.LEFT:
        if not(line.startswith("=")):
            del lines[-1]
            lines = addlines(lines, start=True)
            score += 1
        else:
            endgame()
            break
    elif keypress == readchar.key.RIGHT:
        if not(line.endswith("=")):
            del lines[-1]
            lines = addlines(lines, start=True)
            score += 1
        else:
            endgame()
            break
    elif keypress in ('q', readchar.key.CR, readchar.key.CTRL_C): # CR is Enter
            endgame()
            break


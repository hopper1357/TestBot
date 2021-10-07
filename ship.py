from os.path import exists

power = 500
fuel = 1000
shield = 100
money = 3000
locx = 5
locy = 5


def buyFuel(buy):
    x = buy
    global fuel
    global money
    if money < 50:
        x = False
        return x
    else:
        x = True
        fuel += 300
        money -=50
   
    return x

def initSave():
    file_exists = exists("ship.txt")
    global power
    global fuel
    global shield
    global money
    global locx
    global locy
    if file_exists:
        print("file exists") 
        f = open("ship.txt", "r")
        power = int(f.readline())
        fuel = int(f.readline())
        shield = int(f.readline())
        money = int(f.readline())
        locx = int(f.readline())
        locy = int(f.readline())
        f.close()
        return

    else:
        f = open("ship.txt", "w")
        f.write(str(power) + "\n")
        f.write(str(fuel) + "\n")
        f.write(str(shield) + "\n")
        f.write(str(money) + "\n")
        f.write(str(locx) + "\n")
        f.write(str(locy) + "\n")
        f.close()

    return

def save():
   f = open("ship.txt", "w")
   f.write(str(power) + " \n")
   f.write(str(fuel) + " \n")
   f.write(str(shield) + " \n")
   f.write(str(money) + " \n")
   f.write(str(locx) + " \n")
   f.write(str(locy) + " \n")
   f.close()
   return

from random import randint
from time import sleep

def main():
    d = input('Enter a dice: ')

    #\Determine if there is a numerical first digit, if not, make it 1 (one)
    if d[0] == "d":
        a = 1
        d=str(a)+str(d)
    #/
            
    #\Determine if there is a modifier, if not add modifier of 0 (zero)
    if d.find("+") != -1:
        dmod = d.split("+")
    else:
        d = d + "+0"
        dmod = d.split("+")
    #/
        
    #\Splits the numbers before and after "d"
    d = dmod[0].split("d")
    d_qty = int(d[0])
    d_val = int(d[1])
    #/

    #\Initialize variables
    x = 1
    dtot = 0
    #/

    #print("Rolling Dice...")

    #\Roll dice, print results, add results
    while x <= d_qty:
        #sleep(.1)
        dx =int(randint(1,d_val))
        if dx/d_val <.3:
            print (str(x)+"d:", dx, "Bad Roll!")
        elif dx/d_val >=.8:
            print (str(x)+"d:", dx, "Great Roll!")
        else:
            print (str(x)+"d:", dx)
        dtot = dx + dtot
        x +=1
    #/

    #\Print modifier, add and print total   
    #print("Mod:",dmod[1])
    #print("Average:", (dtot/d_qty))
    #print("Expected Avg:",d_val/2+.5)
    #print("Delta:",round((dtot/d_qty)-(d_val/2+.5),4))
    dtot = int(dtot) + int(dmod[1])
    print("Total:", str(dtot),"\n---------\n")
    #/

while True:
    try:
        main()
    except Exception:
        print("Invalid format","\n---------\n")
        continue

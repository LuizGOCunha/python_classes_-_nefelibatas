#OBJETIVO: output tem que ser numero de 0 a 10000
def dezmil():
    x = 0
    while x < 10000:
        x = x + 1
        print(x)

def oitomil():
    x = 0
    while True:
        print(x)
        x += 1
        if x == 10001:
            break

def amogus():
    AMOGUS = "AMOGUS"
    print(AMOGUS)
    while True:
        while AMOGUS != "AMOGUS"*5:
            print(AMOGUS)
            AMOGUS = AMOGUS + "AMOGUS"
        while AMOGUS != "AMOGUS":
            print(AMOGUS)
            AMOGUS = AMOGUS[:-6]

def tavao():
    print ("Dê bom dia ao Tavão.")
    V = input(">")
    if "bom" in V.lower() and "dia" in V.lower():
        print("Vai tomar no cu!")    
    else:
        print(":)")
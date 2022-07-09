#Mesma coisa de antes mas usando while() = true 
'''x = 0
while True:
    if x < 10000:
        x += 1
        print(x)
    else:
        break'''

x = 0
while True:
    print(x)
    x += 1
    if x == 10001:
        break
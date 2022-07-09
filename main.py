from func import dezmil, oitomil, tavao, amogus
print("Qual função você quer executar?")
print("d = dezmil")
print("o = oitomil")
print('t = tavao')
print('a = amogus')
V = input(">")


dict = {
    'd' : dezmil,
    'o' : oitomil,
    't' : tavao,
    'a' : amogus
}

dict[V]()
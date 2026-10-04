n_train=input()

city=input()
time=input()
cena=float(input())
marshrut=city.replace(" ","-")
marshrut=city.replace(";","-")
print(f'Поезд:{n_train}\nМаршрут:{marshrut}\nОтправление:{time}\nЦена:{cena:.2f}')

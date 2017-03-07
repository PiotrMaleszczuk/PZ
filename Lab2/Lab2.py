#Lab2 07.03.2017

#klasa do rysowania wykresow
#import nazwa as alias

import matplotlib.pyplot as plt
#odwołujac się do biblioteki używamy aliasu ply.funkcja

def load_data(filename):
    X = []
    for line in open(filename):
        tokens = line.split()
        X.append([float(tokens[0]), float(tokens[1]), float(tokens[2])])
    return(X)

#tworzymy funkcje rysujaca dane
def draw_data(X):
    maxX = 0
    maxY = 0
    minX = 0
    minY = 0

    x1 = []
    x2 = []
    x3 = []
    y1 = []
    y2 = []
    y3 = []
    for [x,y,c] in X:
        if c == 1:
            x1.append(x)
            y1.append(y)
        if c == 0:
            x2.append(x)
            y2.append(y)
        if c == -1:
            x3.append(x)
            y3.append(y)
        if x < minX:
            minX = x
        if x > maxX:
            maxX = x
        if y < minY:
            minY = y
        if y > maxY:
            maxY = y

    ##ustawienie pola widzenia na diagramie
    plt.axis([minX - 1, maxX + 1, minY - 1, maxY + 1])
    ##stworzenie diagramu wszystkich punktów
    ##plt.plot(xy , ygreki, kształt, color = kolor
    plt.plot(x1, y1, 'ro', color='black')
    plt.plot(x2, y2, 'ro', color='red')
    plt.plot(x3, y3, 'ro', color='lightGrey')

    ##wyświetlenie diagramu
    plt.show()


#ala main, czyli wywołanie stworzonych funckji
dane = load_data('Lab2PrzykladXYZ')
draw_data(dane)
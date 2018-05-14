from cardgame import *
import random


def main():

    win = GraphWin("CardGame", 1500,800)
    imageNames = ("ace.png", "CardFaces.png", "face02.png", "face03.png")
    imageIndex = 0
    cardList = []
    for x in range(5, 400, 110):
        cardList.append(Card(x,10,imageNames[imageIndex], imageIndex))
        imageIndex += 1
    imageNames = ("CardFaces.png", "ace.png", "face03.png", "face02.png")
    imageIndex = 0
    for x in range(5, 400, 110):
        cardList.append(Card(x, 210,imageNames[imageIndex], imageIndex))
        imageIndex += 1

    for card in cardList:
        card.drawCard(win)
    while not win.closed:
        clicked = win.getMouse()
        for card in cardList:
            card.flipCard(clicked, win)
        while id(imageIndex) == id(imageIndex):
            card.unDrawCard(win)







    




main()



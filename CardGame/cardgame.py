from graphics import *
import random

class Card(object):
    "this creates the card"
    def __init__(self,x,y,whatImage:str):
        self.x= x
        self.y= y
        self.card = RoundedRectangle(Point(x,y),Point(x+100,y+150))
        self.card.setFill("red")
        self.cardImage = Image(Point(x + 50, y + 75), whatImage)
        self.life = 0







    def drawCard(self, win):
        self.card.draw(win)
        self.card.setActiveFill("blue")



    def flipCard(self,clicked:Point, win):
        """flips the card to show the face"""
        if clicked.getX()>= self.x and clicked.getX()<= self.x +100 and clicked.getY()>=self.y and clicked.getY()<self.y + 150:  #finds if the user cliked inside the object to undraw and than draw new face
            self.card.undraw()
            self.cardImage.draw(win)









    def unDrawCard(self,win):
        self.card.undraw()
        self.cardImage.undraw()











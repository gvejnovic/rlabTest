__author__ = 'Goran Vejnovic'
import re


def removeblankparagraf(html):
    return re.sub("<p>\s*</p>", "", html) #pomoću regexp zamjeni s praznim stringom


def main():
    with open("test2.html", "r") as htmlfile:
        htmldata = htmlfile.read()

    f = open("test2removed.html", "w")
    f.write(removeblankparagraf(htmldata))
    f.close()


main()

#print(removeblankparagraf("<html><p>Adadad</p><p>    </p><p> sddad </p><p> </p></html>"))
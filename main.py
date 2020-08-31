# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from tkinter import *
import tkinter.filedialog
import file
import folder
import os

import docx

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    def str_append_list_join(s, n):
        l1 = []
        i = 0
        while i < n:
            l1.append(s)
            i += 1
        return ''.join(l1)

    def firstchar(s):
        return s[:1]

    gui = Tk(className='Renpy convertor')
    gui.iconbitmap('E:/Documents/GitHub/Repos/DTR/icon.ico')
    # set window size
    gui.geometry("300x200")

    def alert_popup(title, message, path):
        """Generate a pop-up window for special messages."""
        root = Tk()
        root.title(title)
        w = 300  # popup window width
        h = 200  # popup window height
        sw = root.winfo_screenwidth()
        sh = root.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        root.geometry('%dx%d+%d+%d' % (w, h, x, y))
        m = message
        m += '\n'
        m += path
        w = Label(root, text=m, width=120, height=10)
        w.pack()
        b = Button(root, text="OK", command=root.destroy, width=10)
        b.pack()
        mainloop()

    file = file
    savefolder = folder

    def docfilename():
        filename = tkinter.filedialog.askopenfilename(filetypes=[("Word Documents","*.docx")])
        file.setfilelocation(filename)
        file.setfilename(filename)


    def savelocation():
        folder.setfolderlocation(tkinter.filedialog.askdirectory())


    def renpyconversion():
        name = os.path.join(folder.getfolderlocation(),file.getfilename()+".rpy")
        file1 = open(name, "w")
        doc = docx.Document(file.getfilelocation())
        lines = doc.paragraphs
        inmenu = False
        for x in lines:
            if x.text == "":
                file1.write("\n")
                continue
            else:
                var = x.text
                spacecheck = " "
                if spacecheck in var:
                    (shortcut, input) = var.split(None, 1)
                else:
                    shortcut = var
            if shortcut == "T" or shortcut == "t":
                (cname, cline) = input.split(None, 1)
                if inmenu == False:
                    file1.write("   " + cname + " \"" + cline + "\"")
                    file1.write("\n")
                elif inmenu == True:
                    file1.write("           " + cname + " \"" + cline + "\"")
                    file1.write("\n")
            elif shortcut == "U" or shortcut == "u":
                (cname, cline) = input.split(None, 1)
                if inmenu == False:
                    file1.write("   " + "\"" + cname + "\"" + " \"" + cline + "\"")
                    file1.write("\n")
                elif inmenu == True:
                    file1.write("           " + "\"" + cname + "\"" + " \"" + cline + "\"")
                    file1.write("\n")

            elif shortcut == "L" or shortcut == "l":
                file1.write("label " + input + ":")
                file1.write("\n")

            elif shortcut == "I" or shortcut == "i":
                if inmenu == False:
                    file1.write("   show bg " + input + " with dissolve")
                    file1.write("\n")
                elif inmenu == True:
                    file1.write("           show bg " + input + " with dissolve")
                    file1.write("\n")

            elif shortcut == "N" or shortcut == "n":
                (iname, image) = input.split(None, 1)
                file1.write("image bg " + iname + " = " + "\"" + image + "\"")
                file1.write("\n")

            elif shortcut == "J" or shortcut == "j":
                if inmenu == False:
                    file1.write("   jump " + input)
                    file1.write("\n")
                if inmenu == True:
                    file1.write("           jump " + input)
                    file1.write("\n")
            elif shortcut == "M" or shortcut == "m":
                inmenu = True
                file1.write("   menu:")
                file1.write("\n")
            elif shortcut == "E" or shortcut == "e":
                inmenu = False
            elif shortcut == "C" or shortcut == "c":
                file1.write("       \"" + input + "\":")
                file1.write("\n")
            elif shortcut == "A" or shortcut == "a":
                if inmenu == False:
                    file1.write("   play music " + input)
                    file1.write("\n")
                if inmenu == True:
                    file1.write("           play music " + input)
                    file1.write("\n")
            elif shortcut == "AS" or shortcut == "As" or shortcut == "as":
                if inmenu == False:
                    file1.write("   play sound " + input)
                    file1.write("\n")
                if inmenu == True:
                    file1.write("           play sound " + input)
                    file1.write("\n")
            elif shortcut == "$":
                if inmenu == False:
                    file1.write("   $ " + input)
                    file1.write("\n")
                if inmenu == True:
                    file1.write("           $ " + input)
                    file1.write("\n")
            elif shortcut == "V" or shortcut == "v":
                (vname, video) = input.split(None, 1)
                file1.write("image bg " + vname + " = Movie(play=" + "\"" + video + "\")")
            elif shortcut == "#" or shortcut == "#":
                file1.write("#" + input)


        file1.close()
        alert_popup("Conversion Complete", "Your docx to rpy conversion is complete.", folder.getfolderlocation())

    B = tkinter.Button(gui, text="Open Word Doc (.docx)", command=docfilename)
    B.pack()
    B2 = tkinter.Button(gui, text="Select Save Location", command=savelocation)
    B2.pack()
    B3 = tkinter.Button(gui, text="Convert", command=renpyconversion)
    B3.pack()
    # Code to add widgets will go here...

    gui.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

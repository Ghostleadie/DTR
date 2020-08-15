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



    gui = Tk(className='Renpy convertor')
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
            if x.runs[0].text == "T " or x.runs[0].text == "T" or x.runs[0].text == "t" or x.runs[0].text == "t ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "T ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "T":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "t ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "t":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                (cname, cline) = var.split(None, 1)
                if inmenu == False:
                    file1.write("   " + cname + " \"" + cline + "\"")
                    file1.write("\n")
                elif inmenu == True:
                    file1.write("           " + cname + " \"" + cline + "\"")
                    file1.write("\n")

            elif x.runs[0].text == "U " or x.runs[0].text == "U" or x.runs[0].text == "u" or x.runs[0].text == "u ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "U ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "U":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "u ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "u":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                (cname, cline) = var.split(None, 1)
                if inmenu == False:
                    file1.write("   " + "\"" + cname + "\"" + " \"" + cline + "\"")
                    file1.write("\n")
                elif inmenu == True:
                    file1.write("           " + "\"" + cname + "\"" + " \"" + cline + "\"")
                    file1.write("\n")

            elif x.runs[0].text == "L " or x.runs[0].text == "L" or x.runs[0].text == "l" or x.runs[0].text == "l ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "L ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "L":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "l ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "l":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                file1.write("label " + var + ":")
                file1.write("\n")

            elif x.runs[0].text == "I " or x.runs[0].text == "I" or x.runs[0].text == "i" or x.runs[0].text == "i ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "I ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "I":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "i ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "i":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                if inmenu == False:
                    file1.write("   show bg " + var + " with dissolve")
                    file1.write("\n")
                elif inmenu == True:
                    file1.write("           show bg " + var + " with dissolve")
                    file1.write("\n")
                
            elif x.runs[0].text == "II " or x.runs[0].text == "II" or x.runs[0].text == "ii" or x.runs[0].text == "ii " or x.runs[0].text == "Ii" or x.runs[0].text == "Ii ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "II ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "II":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "ii ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "ii":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "Ii":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "Ii ":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                (iname, image) = var.split(None, 1)
                file1.write("image bg " + iname + " = " + "\"" + image + "\"")
                file1.write("\n")
            elif x.runs[0].text == "J " or x.runs[0].text == "J" or x.runs[0].text == "j" or x.runs[0].text == "j ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "J ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "J":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "j ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "j":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                newvar = var.replace(" ", "", 1)
                if inmenu == False:
                    file1.write("   jump " + newvar)
                    file1.write("\n")
                if inmenu == True:
                    file1.write("           jump " + newvar)
                    file1.write("\n")
            elif x.runs[0].text == "M " or x.runs[0].text == "M" or x.runs[0].text == "m" or x.runs[0].text == "m ":
                inmenu = True
                file1.write("   menu:")
                file1.write("\n")
            elif x.runs[0].text == "E " or x.runs[0].text == "E" or x.runs[0].text == "e" or x.runs[0].text == "e ":
                inmenu = False
            elif x.runs[0].text == "C " or x.runs[0].text == "C" or x.runs[0].text == "c" or x.runs[0].text == "c ":
                rl = len(x.runs)
                ii = 0
                var = ""
                while ii < rl:

                    if x.runs[ii].text == "C ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "C":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "c ":
                        ii += 1
                        continue
                    elif x.runs[ii].text == "c":
                        ii += 1
                        continue
                    var = var + x.runs[ii].text
                    ii += 1
                newvar = var.replace(" ", "",1)
                file1.write("       \"" + newvar + "\":")
                file1.write("\n")
        else:
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

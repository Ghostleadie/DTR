# DtR
Word Document (.docx) to renpy script file (.rpy)

## Usage
1. Click the open word doc button
2. Find your word document and select it
3. Click the select save location button
4. Select a folder to save your .rpy file to
5. Click the convert button
6. Done

## **IMPORTANT INFO**
1. Each line must contain a line otherwise it will throw an error.
2. Each line must start with one of the shortcuts below
3. Indentations are automatically added so don't add them yourself
4. If a line doesn't show in the .rpy file make the shortcut **bold** and delete then readd the following space
5. If you have any custom python code you will have to add that yourself to the .rpy file
6. Once you have finished putting everythig you need into a menu you must use the end menu short cut

## Shortcuts
Shortcut | Name | Usage | Output
------------ | ------------- | ------------- | -------------
T | Character text (with defined caracter) | T N hello there. | N "hello there."
U | Character text (with undefined caracter) | T boy hello there. | "boy" "hello there."
L | Label | L Scene1 | label Scene1: 
I | shows an image with dissolve | I image1 | show bg image1 with dissolve
N | loads the image | N act1image image1 | image bg act1image = "image1"
J | jump to another lable | J Scene2 | jump scene2
M | Starts a menu | M | menu:
C | Menu Choice | C Look | "Look":
E | End menu | E | 

This a demo of what your word document should look like.

```
Ii act1 act1titlecard
L stair
I act1
T J hello!
U Girl hi.
M
C Look
U boy hey there
J Act2
C Look away
U Girl Bye dude
T D asdasdasda!
T N asdasdasd?
J act3
E
J act1
```
This is what will get outputted in your desired location.
```
image bg act1 = "act1titlecard"
label stair:
   show bg act1 with dissolve
   J "hello!"
   "Girl" "hi."
   menu:
       "Look":
           "boy" "hey there"
           jump Act2
       "Look away":
           D "asdasdasda!"
           N "asdasdasd?"
           jump act3
   jump act1
```

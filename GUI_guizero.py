from guizero import App, Text, TextBox, PushButton, Picture, ButtonGroup

#Appends pressed button numbers to the textbox field
def input_to_textbox(input):
    text_box.append(input)

#Clears the textbox
def clear_textbox():
    text_box.clear()

#Sends the data in the textbox.(Currently just prints the data)
def send_data():
    print(text_box.value)
    text_box.clear()

app = App(title = "NUTIKAPP", width= 1280, height = 720, layout = "grid")

welcome_message = Text(app, text = "SISESTA KOOD", font = "Times New Roman", grid = [1,0])

text_box = TextBox(app, grid = [1,1], width=25)

#Buttons, command = function to be called when pressed, args = passed argument into function when pressed
button1 = PushButton(app, text="1", grid=[0,2], align = "right", width=15, command=input_to_textbox, args=['1'])
button2 = PushButton(app, text="2", grid=[1,2], width=15, command=input_to_textbox, args=['2'])
button3 = PushButton(app, text="3", grid=[2,2], width=15, command=input_to_textbox, args=['3'])
button4 = PushButton(app, text="4", grid=[0,3], align = "right", width=15, command=input_to_textbox, args=['4'])
button5 = PushButton(app, text="5", grid=[1,3], width=15, command=input_to_textbox, args=['5'])
button6 = PushButton(app, text="6", grid=[2,3], width=15, command=input_to_textbox, args=['6'])
button7 = PushButton(app, text="7", grid=[0,4], align = "right", width=15, command=input_to_textbox, args=['7'])
button8 = PushButton(app, text="8", grid=[1,4], width=15, command=input_to_textbox, args=['8'])
button9 = PushButton(app, text="9", grid=[2,4], width=15, command=input_to_textbox, args=['9'])
buttonD = PushButton(app, text="DEL", grid=[0,5], align = "right", width=15, command=clear_textbox)
button0 = PushButton(app, text="0", grid=[1,5], width=15, command=input_to_textbox, args=['0'])
buttonE = PushButton(app, text="ENT", grid=[2,5], width=15,command=send_data)

picture = Picture(app, image = "logotest.gif", grid = [1,6])

app.display()

from guizero import App, Text, TextBox, PushButton, Picture, ButtonGroup
import random
import os

#Appends pressed button numbers to the textbox field
def input_to_textbox(user_input):
    text_box.append(user_input)

#Clears the textbox
def clear_textbox():
    text_box.clear()

#Sends the data in the textbox.(Currently just prints the data)
def send_data():
    entered_code = text_box.value
    used_codes = load_used_codes()
    if entered_code in used_codes:
        print("Processing code:", entered_code)
    else:
        print("Wrong code:", entered_code)
        
    text_box.clear()
    
#Generate a random 6-digit code
def generate_code():
    random_code = str(random.randint(100000, 999999))

    #Check if the code has been used before generating a new one
    while random_code in used_codes:
        random_code = str(random.randint(100000, 999999))

    text_box.value = random_code
    used_codes.add(random_code)
    save_used_codes()

#Check if the user input matches the generated code
def check_code():
    user_input = self.user_input_var.get()
    generated_code = self.generated_code_var.get()

    if generated_code in self.used_codes:
        messagebox.showerror("Error", "Code has already been used. Generate a new one.")
    elif user_input == generated_code:
        messagebox.showinfo("Success", "Box opened successfully!")
        self.used_codes.add(generated_code)
        self.save_used_codes()
    else:
        messagebox.showerror("Error", "Incorrect code. Try again.")

#Load used codes from a file
def load_used_codes():
    filename = "codes.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return set(line.strip() for line in file)
    return set()

#Save used codes to a file
def save_used_codes():
    filename = "codes.txt"
    with open(filename, "a") as file:
        file.write(text_box.value + "\n")

app = App(title = "NUTIKAPP", width= 1280, height = 720, layout = "grid")

welcome_message = Text(app, text = "SISESTA KOOD", font = "Times New Roman", grid = [1,0])

text_box = TextBox(app, grid = [1,1], width=25)

used_codes = set()

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

generate_button = PushButton(app, text="Generate Code", grid=[0, 6], align="right", width=15, command=generate_code)

picture = Picture(app, image = "logotest.gif", grid = [1,6])

app.display()

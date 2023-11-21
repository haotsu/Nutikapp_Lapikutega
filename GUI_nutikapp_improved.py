#GUI imports
from guizero import App, Text, TextBox, PushButton, Picture, ButtonGroup, Box, Window, info
#Time and other imports
import random
import os
from datetime import datetime, timedelta
#I2C imports
import smbus

#Appends pressed button numbers to the textbox field
def input_to_textbox(user_input):
    text_box.append(user_input)

#Function to clear the textbox
def clear_textbox():
    text_box.clear()

#Removes the code once it has been used
def remove_code_from_file(code):
    filename = "codes.txt"
    with open(filename, "r") as file:
        lines = file.readlines()
        with open(filename, "w") as file:
            for line in lines:
                if line.strip() != code:
                    file.write(line)

#Sends the data in the textbox
def send_data():
    entered_code = text_box.value.strip()
    used_codes = load_used_codes()
    check_code(entered_code)
    if entered_code == "":
        print("Entered code is empty.")
    elif entered_code in used_codes:
        if code_expired(entered_code):
            print("Code has expired:", entered_code)
            remove_code_from_file(entered_code)
        else:
            print("Processing code:", entered_code)
            timestamp = generate_timestamp()
            code_timestamps[entered_code] = timestamp
    else:
        print("Wrong code:", entered_code)
        
    text_box.clear()

#Generate a random 6-digit code
def generate_code():
    random_code = str(random.randint(100000, 999999))

    #Check if the code has been used before generating a new one
    while random_code in used_codes:
        random_code = str(random.randint(100000, 999999))

    save_used_codes(random_code)

#Load used codes from a file
def load_used_codes():
    filename = "codes.txt"
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return set(line.strip() for line in file)
    return set()

#Save used codes to a file
def save_used_codes(code):
    filename = "codes.txt"
    with open(filename, "a") as file:
        file.write(code + "\n")

#Generate a timestamp for a code
def generate_timestamp():
    return datetime.now()

#Check if a code has expired
def code_expired(code):
    if code in code_timestamps:
        expiration_time = code_timestamps[code] + timedelta(minutes=1)
        return datetime.now() > expiration_time
    return False

#Function to change the screen when admin code is entered
def check_code(code):
    #Function that opens the selected box
    def open_box():
        radioBoxValue = radioBoxes.value
        adminWindow.info("AVA KAPP", "Avasid kapi {}".format(radioBoxValue))
    
    if code == '1337':
        adminWindow = Window(app, title = "ADMINI KAPP", width= 1024, height = 600)
        window_box = Box(adminWindow, layout = "grid")
        generate_button = PushButton(window_box, text="Generate Code", grid=[0, 6], align="right", width=15, command=generate_code)
        i2c_button = PushButton(window_box, text="I2C", grid=[1, 6], align="right", width=15, command=i2c_code)
        radioBoxes = ButtonGroup(window_box, options=[["KAPP 1", "1"], ["KAPP 2", "2"], ["KAPP 3", "3"], ["KAPP 4", "4"]], grid=[0,1], align = "left")
        buttonOpenBox = PushButton(window_box, text="AVA KAPP", grid=[0,0], align = "top", width=15, command=open_box)
    if code == '0000':
        exit()

def i2c_code():
    #Send the command to the STM32
    bus.write_i2c_block_data(DEVICE_ADDR, 0x00, data)
    
    #To read info from the STM32
    #read_info = bus.read_i2c_block_data(DEVICE_ADDR,99,3)
    #print(b)

app = App(title = "NUTIKAPP", width= 1920, height = 1080)
#Used for creating empty space at the top of the screen
center_pad = Box(app, align="top", height=150, width="fill")
#Used for putting all the buttons, picture etc. to a container
center_box = Box(app, layout = "grid")

welcome_message = Text(center_box, text = "SISESTA KOOD", font = "Times New Roman", grid = [1,0])

text_box = TextBox(center_box, grid = [1,1], width=25)

used_codes = set()

code_timestamps = {}

#Initialize the I2C bus
DEVICE_BUS = 1

#STM32 Nucleo's I2C address
#(will be left shifted to add the read write bit)
DEVICE_ADDR =12
bus = smbus.SMBus(DEVICE_BUS)
data = [1,2,3,4,5,6,7,8,9]

#When a button is pressed the function in 'command' is executed and arguments given is in 'args'
button1 = PushButton(center_box, text="1", grid=[0,2], align = "right", width=45,height=5, command=input_to_textbox, args=['1'])
button2 = PushButton(center_box, text="2", grid=[1,2], width=45,height=5,  command=input_to_textbox, args=['2'])
button3 = PushButton(center_box, text="3", grid=[2,2], width=45,height=5,  command=input_to_textbox, args=['3'])
button4 = PushButton(center_box, text="4", grid=[0,3], align = "right", width=45,height=5,  command=input_to_textbox, args=['4'])
button5 = PushButton(center_box, text="5", grid=[1,3], width=45, height=5, command=input_to_textbox, args=['5'])
button6 = PushButton(center_box, text="6", grid=[2,3], width=45,height=5,  command=input_to_textbox, args=['6'])
button7 = PushButton(center_box, text="7", grid=[0,4], align = "right", width=45, height=5, command=input_to_textbox, args=['7'])
button8 = PushButton(center_box, text="8", grid=[1,4], width=45,height=5,  command=input_to_textbox, args=['8'])
button9 = PushButton(center_box, text="9", grid=[2,4], width=45,height=5,  command=input_to_textbox, args=['9'])
buttonD = PushButton(center_box, text="DEL", grid=[0,5], align = "right", width=45,height=5,  command=clear_textbox)
button0 = PushButton(center_box, text="0", grid=[1,5], width=45,height=5,  command=input_to_textbox, args=['0'])
buttonE = PushButton(center_box, text="ENT", grid=[2,5], width=45,height=5, command=send_data)

picture = Picture(center_box, image = "logo.gif", grid = [1,6])

app.full_screen = True
app.display()

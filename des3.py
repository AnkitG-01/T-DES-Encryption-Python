from tkinter import *  #tkinter v8.6
from tkinter import ttk,filedialog
from tkinter.filedialog import askopenfile
import os
from Crypto.Cipher import DES3  # pycryptodome v3.15.0
from hashlib import md5

#Create an instance of Tkinter frame
win= Tk()

#Set the geometry of Tkinter frame
win.geometry("750x500")

file_path=""

#Function to open the File Browser
def open_file():
   file = filedialog.askopenfile(mode='r', filetypes=[('image Files', '*.jpeg *.png'),('Text Files','*.txt'),('Python Files','*.py')])
   if file:
      global file_path
      file_path = os.path.abspath(file.name)
      print(file_path)

#Function to encrypt the selected file
def encrypt():
    key=entry1.get()
    key_hash = md5(key.encode("ascii")).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b"0")

    #read file
    with open(file_path, "rb") as input_file:
        file_bytes = input_file.read()
    
    new_file_bytes = cipher.encrypt(file_bytes)
    with open(file_path, "wb") as output_file:
        output_file.write(new_file_bytes)
    print("file encrypted");

#Function to decrypt the selected file
def decrypt():
    key=entry1.get()
    key_hash = md5(key.encode("ascii")).digest()
    tdes_key = DES3.adjust_key_parity(key_hash)
    cipher = DES3.new(tdes_key, DES3.MODE_EAX, nonce=b"0")

    #read file
    with open(file_path, "rb") as input_file:
        file_bytes = input_file.read()

    new_file_bytes = cipher.decrypt(file_bytes)
    with open(file_path, "wb") as output_file:
        output_file.write(new_file_bytes)
    print("file decrypted")

#Initialize a Label to Browse Files
label = Label(win, text="Click the Button to browse the Files", font=('Georgia 13'))
label.pack(pady=10)

# Create a Button
ttk.Button(win, text="Browse", command=open_file).pack(pady=20)

#Initialize a Label to Enter the Key
label1=Label(win, text="enter key", font=("Courier 22 bold"))
label1.pack()

#Create an Entry widget to accept User Input
entry1= Entry(win, width= 40)
entry1.focus_set()
entry1.pack()

#Create the Encrypt and Decrypt Buttons
ttk.Button(win, text= "Encrypt",width= 20, command= encrypt).pack(pady=20)
ttk.Button(win, text= "Decrypt",width= 20, command= decrypt).pack(pady=20)

#Run the main loop
win.mainloop()
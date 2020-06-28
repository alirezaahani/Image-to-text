#You need to install pytesseract on your system
from pytesseract import*
from tkinter import*
from tkinter import filedialog,messagebox
#ItS : Image to String
def ItS():
	try:
		#opening a file
		User_input = filedialog.askopenfile()
		#Converting image to text
		Content = pytesseract.image_to_string(User_input.name)
		#Showing user output
		if not Content == "":
			User_content.configure(text="Your text is :{0}".format(Content))
		else :
			User_content.configure(text="I can't see anything.")
	except:
		messagebox.showwarning(title='error',message="Please open a corrcet image")
#Making a window
mainWindow = Tk()
#Window title
mainWindow.title("Image to text")
#Window background color
mainWindow.configure(background="white")
#Window size
mainWindow.minsize(300,250)
#Font,Size and background for label
User_content = Label(mainWindow,background="white",font=("Arial",14))
#Packing the label
User_content.pack()
#Create a new button
Go_button = Button(mainWindow,text="Go",command=ItS,background="gray",font=("Arial",10))
Go_button.pack()
#Looping the window and program
mainWindow.mainloop()

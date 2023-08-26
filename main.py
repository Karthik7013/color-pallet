from tkinter import *
import random


class ColorPallet:
	rgb = ['a','b','c','d','e','f','1','2','3','4','5','6','7','8','9','0']

	def colorGenerator(self):# generates a random HexCode
		self.color = "#"
		for i in range(6):
			self.color+=random.choice(ColorPallet.rgb)
		self.color_label.config(text = self.color,bg = self.color)
		self.f1.config(bg = self.color)
		self.hex_entry.delete(0,END)
		self.hex_entry.insert(0,self.color)
		self.hex_entry.focus()
		return self.color # return the code to the function

	def colorFind(self): # find the color with HexCode input
		try:
			self.f1.config(bg =self.hex_entry.get())
			self.color_label.config(text = self.hex_entry.get(),bg = self.hex_entry.get())
		except:

			self.fali.config(text = "Invalid Color Code...", fg = 'red')
			self.fali.after(900,lambda:self.fali.config(text = ''))


	def __init__(self,root):
		self.root = root
		self.root.config(bg = 'grey')
		self.root.title('Cool Colors')
		self.root.geometry('500x500')
		self.root.resizable(height = False,width = False)
		Label(root,text = 'Cool ColorPallet',font = ('rockwell',20,'bold'),bg = 'grey', fg = 'snow').pack(pady = (20,0))
		# self.root.iconbitmap(r'./pallet.ico')
		self.color = '#000000'
		self.f1 = Frame(self.root,background = self.color)
		self.f1.pack(pady = 30,ipadx = 200,ipady = 100)
		self.color_label = Label(self.f1,text = self.color,fg = 'white',bg = 'black')
		self.color_label.pack(side = 'bottom')
		
		self.f2 = Frame(self.root)
		self.f2.pack()
		self.hex_entry = Entry(self.f2,font = ('',15,'bold'),width = 10,justify = 'center')
		self.hex_entry.pack()
		self.hex_entry.insert(0,self.color)

		self.f3 = Frame(self.root, bg = 'grey')
		self.f3.pack(pady= 30)
		self.generate_btn = Button(self.f3,text = 'Generate',command = self.colorGenerator,fg = 'white',bg = 'green')
		self.generate_btn.pack(side = 'right', padx= (25,0))
		self.search_btn = Button(self.f3,text = 'Search',command = self.colorFind,fg = 'white',bg = 'orange')
		self.search_btn.pack(side = 'left',padx=(0,40))
		self.fali = Label(self.root,text = '',bg = 'grey',font = ('',15,'italic','bold'), fg= "white")
		self.fali.pack()
		self.color = self.colorGenerator()
		self.root.mainloop()

if __name__ == "__main__":
	root = Tk() # create instance for the class Tk()
	ColorPallet(root)
from tkinter import *
import random
import time
from tkinter import messagebox
colours=['blue','red','yellow','green','red','pink','red','black','green','cyan']
global i
i=0
global redcount
redcount=0
global greencount
greencount=0
global canvas
def startgame1():
	global canvas
	global redcount
	global greencount
	x=startclick(22)
	if x==1:
		time.sleep(5)
	messagebox.showinfo("Answer","number of red balls ="+str(redcount)+" number of green balls ="+str(greencount))
	redcount=0
	greencount=0
	canvas.delete("all")

def startgame2():
	global canvas
	global redcount
	global greencount
	x=startclick(35)
	if x==1:
		time.sleep(5)
	messagebox.showinfo("Answer","number of red balls ="+str(redcount)+" number of green balls ="+str(greencount))
	canvas.delete('all')
	redcount=0
	greencount=0

def startgame3():
	global canvas
	global greencount
	global redcount
	x=startclick(45)
	if x==1:
		time.sleep(5)
	messagebox.showinfo("Answer","number of red balls ="+str(redcount)+" number of green balls ="+str(greencount))
	canvas.delete('all')
	redcount=0
	greencount=0

def startclick(k):
	global i
	global canvas
	global redcount
	global greencount
	for i in range(0,int(k)):
		m=random.randint(0,9)
		if m==1 or m==4 or m==6:
			redcount=redcount+1
		if m==3 or m==8:
			greencount=greencount+1
		try:
			a=random.randint(50,400)
			b=random.randint(50,400)
			c=random.randint(25,50)
			canvas.create_oval(a,b,a+c,b+c,outline='white',fill=colours[m],width=2)
			canvas.update()
		except:
			print()
	return(1)

root=Tk()
root.title("Count The Colors")
root.geometry("800x700+20+20")
root.configure(bg='yellow')
canvas=Canvas(width=500,height=500,bg='#87ceeb')
canvas.place(x=20,y=20)
w=Label(root,text='Can you count the number of red and green coloured balls?',bg='black',fg='yellow')
w.place(x=20,y=500)
y=Label(root,text='you have 10 seconds to answer press the start button to play!!',bg='white',fg='blue')
y.place(x=20,y=550)
#b=Button(root,text='START',bg='#e79700',width=10,height=1,font=('Open Sans',13,'bold'),fg='white',command=startgame)
#b.place(x=20,y=600)
b1=Button(root,text='LEVEL 1',bg='green',width=10,height=1,font=('Open Sans',13,'bold'),fg='white',command=startgame1)
b1.place(x=600,y=60)
b2=Button(root,text='LEVEL 2',bg='red',width=10,height=1,font=('Open Sans',13,'bold'),fg='white',command=startgame2)
b2.place(x=600,y=160)
b3=Button(root,text='LEVEL 3',bg='blue',width=10,height=1,font=('Open Sans',13,'bold'),fg='white',command=startgame3)
b3.place(x=600,y=260)
root.mainloop()
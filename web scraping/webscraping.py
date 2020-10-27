from tkinter.ttk import Combobox
from tkinter import Button, Label
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
from matplotlib import pyplot as plt
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

global url
url = " "
root = Tk()
root.title("Web Scraping Instagram Data")
root.geometry('{}x{}'.format(600, 500))
df = pd.DataFrame()
for f in ['socialhandles.xlsx',]:
    data = pd.read_excel(f, 'Sheet1')
    df = df.append(data)
    df_name = df[['person_name']]
    df_name = df_name.values.tolist()  # converting data frame to list
    # print(df_name)
    df_handle = df[['insta_handle']]  # column names
    df_handle = df_handle.values.tolist()


# print(df_handle)
def parse_data(s):
    # creating a dictionary
    data = {}
    # splittting the content
    # then taking the first part
    s = s.split("-")[0]
    # again splitting the content
    s = s.split(" ")
    # assigning the values
    data['Followers'] = s[0]
    data['Following'] = s[2]
    data['Posts'] = s[4]
    #lblfollowers = Label(root, width=30, font=('arial', 15, "bold"), fg='#922B21')
    lblfollowers.configure(text="Number Of Followers : " + s[0])
    lblfollowers.place(x=100, y=210)
    #lblfollowing = Label(root, width=30, font=('arial', 15, "bold"), fg='#922B21')
    lblfollowing.configure(text="Number Following : " + s[2])
    lblfollowing.place(x=100, y=240)
    #lblposts = Label(root, width=30, font=('arial', 15, "bold"), fg='#922B21')
    lblposts.configure(text="Number of posts : " + s[4])
    lblposts.place(x=100, y=270)


# print(data)
def scrape_data(name):
    global url,uname
    uname=name
    url = "https://www.instagram.com/" + dictionary[name] + "/"
    # getting the request from url
    #print("SCRAPE URL", url)
    r = requests.get(url)
    # converting the text
    s = bs(r.text, "html.parser")
    # finding meta info
    meta = s.find("meta", property="og:description")
    # calling parse method
    return parse_data(meta.attrs['content'])


def openinsta():
    url = "https://www.instagram.com/" + dictionary[uname] + "/"
    chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open(url)


def openface():
    webbrowser.open('https://www.facebook.com/FacebookIndia/?brand_redir=108824017345866')


def opentwit():
    webbrowser.open('https://twitter.com/explore')

def Compare():
    global final_names
    followers=[]
    following=[]
    posts=[]
    for n in final_names:
        url = "https://www.instagram.com/" + dictionary[n] + "/"
        # getting the request from url
        #print("SCRAPE URL", url)
        r = requests.get(url)
        # converting the text
        s = bs(r.text, "html.parser")
        # finding meta info
        meta = s.find("meta", property="og:description")
        s=meta.attrs['content']
        s = s.split("-")[0]
    # again splitting the content
        s = s.split(" ")
        # assigning the values
        #data['Followers'] = s[0]
        #data['Following'] = s[2]
        #data['Posts'] = s[4]
        z=s[0]
        ch=z[len(z)-1]
        if ch=='m':
            z=z[0:-1]
            z=float(z)*1000000
        elif ch=='k':
            z=z[0:-1]
            z=float(z)*1000
        elif len(z)==5 and z[1]==',':
            l=""
            l+=z[0]
            l+=z[2]
            l+=z[3]
            l+=z[4]
            z=int(l)
        else:
            z=int(z)

        followers.append(z)
        z=s[2]
        ch=z[len(z)-1]
        if ch=='m':
            z=z[0:-1]
            z=float(z)*1000000
        elif ch=='k':
            z=z[0:-1]
            z=float(z)*1000
        elif len(z)==5 and z[1]==',':
            l=""
            l+=z[0]
            l+=z[2]
            l+=z[3]
            l+=z[4]
            z=int(l)
        else:
            z=int(z)
        following.append(z)
        z=s[4]
        ch=z[len(z)-1]
        if ch=='m':
            z=z[0:-1]
            z=float(z)*1000000
        elif ch=='k':
            z=z[0:-1]
            z=float(z)*1000
        elif len(z)==5 and z[1]==',':
            l=""
            l+=z[0]
            l+=z[2]
            l+=z[3]
            l+=z[4]
            z=int(l)
        else:
            z=int(z)
        posts.append(z)
    x=0.25
    l1=[]
    l2=[]
    l3=[]
    for i in range(len(final_names)):
        l1.append(x)
        l2.append(x+0.15)
        l3.append(x+0.3)
        x=x+0.75
    plt.bar(l1,posts,label='Posts',color='g',width=0.35)
    plt.bar(l2,followers, label='Followers', width=0.35)
    plt.bar(l3,following,label='Following',color='r',width=0.35)
    plt.legend()
    plt.xlabel('Usernames')
    plt.xticks(l2,final_names)
    plt.show()

def Back():
    cb.place_forget()
    lblinsta.pack_forget()
    back1.place_forget()
    compare.place_forget()
    binsta.place_forget()
    lblopen.place_forget()
    lblname.place_forget()
    lblfollowers.place_forget()
    lblfollowing.place_forget()
    lblposts.place_forget()
    lblusernames.place(x=-100,y=160)
    usernameentry.place(x=40,y=220)
    startbutton.place(x=180,y=270)
    usernameentry.delete(0,'end')

def start():
    lblusernames.place_forget()
    usernameentry.place_forget()
    startbutton.place_forget()
    global uname
    name=usernames.get()
    global final_names,dictionary
    final_names = name.split(',')
    final_handles = final_names
    dictionary = {}
    for i in range(len(final_names)):
        dictionary.update({final_names[i]: final_handles[i]})
    uname=cb.get()
    cb['values']=final_names
    cb.current(0)
    cb.bind("<<ComboboxSelected>>", lambda event:scrape_data(cb.get()))
    lblinsta.pack()
    back1.place(x=500,y=10)
    compare.place(x=260,y=126)
    lblname.place(x=25, y=90)
    cb.place(x=50, y=130)
    binsta.place(x=320, y=370)
    lblopen.place(x=50, y=410)

lblusernames=Label(root,text="Enter Instagram Usernames seperated by ','",width=50,font=('arial', 19, "bold"),fg='#922B21')
lblusernames.place(x=-100,y=160)
usernames=StringVar()
fon=('arial',15)
usernameentry=Entry(root,width=45,textvariable=usernames,font=fon)
usernameentry.place(x=40,y=220)
startbutton=Button(root,width=20,text="Start",font=('arial',12,'bold'),foreground='#922B21',command=start)
startbutton.place(x=180,y=270)
lblinsta = Label(root, text="Instagram Data", width=40, font=('arial', 30, "bold"), fg='#922B21')
cb = Combobox(root, width=18, font=('Times new roman', 12, "bold"))
#lblinsta.pack()
lblname = Label(root, text="Select Name", width=15, font=('arial', 12, "bold"), fg='#922B21')
#lblname.place(x=25, y=90)
"""
When we assign a Data frame and convert it to list, the values inside will
be enclosed in
[' at beginning and at end by ']. these need to be eliminates. hence we
use repr function to convert
object to normal string and then use slicing to eliminate these
characters from beginning and end """

# print(dict)
lblfollowers = Label(root, width=30, font=('arial', 15, "bold"), fg='#922B21')
lblfollowing = Label(root, width=30, font=('arial', 15, "bold"), fg='#922B21')
lblposts = Label(root, width=30, font=('arial', 15, "bold"), fg='#922B21')
#cb.place(x=50, y=130)
img=Image.open('insta.ico')
img=img.resize((80,80),Image.ANTIALIAS)
imginsta = ImageTk.PhotoImage(img)
img=Image.open('home.png')
img=img.resize((40,40),Image.ANTIALIAS)
back=ImageTk.PhotoImage(img)
binsta = Button(root, image=imginsta, command=openinsta)
back1=Button(root, image=back, command=Back)
compare=Button(root,width=18,text="Compare",font=('arial',12,'bold'),foreground='#922B21',command=Compare)
#binsta.place(x=220, y=400)
lblopen = Label(root, width=25, text="To Visit Profile, Click here==>", font=('arial', 12, "bold"), fg='#922B21')
#lblopen.place(x=-20, y=450)
root.mainloop()

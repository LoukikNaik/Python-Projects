from tkinter.ttk import Combobox
from tkinter import Button, Label
from tkinter import *
from PIL import ImageTk, Image
import webbrowser
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

global url
url = " "
root = Tk()
root.title("Welcome to Web")
root.geometry('{}x{}'.format(600, 500))
df = pd.DataFrame()
for f in ['C:\\Users\\Loukik\\Desktop\\khateeb python\\web scraping\\socialhandles.xlsx',]:
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
    lblfollowers = Label(root, width=30, font=('arial', 12, "bold"), fg='#922B21')
    lblfollowers.configure(text="Number Of Followers : " + s[0])
    lblfollowers.place(x=25, y=200)
    lblfollowing = Label(root, width=30, font=('arial', 12, "bold"), fg='#922B21')
    lblfollowing.configure(text="Number Following : " + s[2])
    lblfollowing.place(x=25, y=230)
    lblposts = Label(root, width=30, font=('arial', 12, "bold"), fg='#922B21')
    lblposts.configure(text="Number of posts : " + s[4])
    lblposts.place(x=25, y=260)


# print(data)
def scrape_data(self):
    global url
    url = "https://www.instagram.com/" + dictionary[cb.get()] + "/"
    # getting the request from url
    print("SCRAPE URL", url)
    r = requests.get(url)
    # converting the text
    s = bs(r.text, "html.parser")
    # finding meta info
    meta = s.find("meta", property="og:description")
    # calling parse method
    return parse_data(meta.attrs['content'])


def openinsta():
    url = "https://www.instagram.com/" + dictionary[cb.get()] + "/"
    chromedir = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"
    webbrowser.get(chromedir).open(url)


def openface():
    webbrowser.open('https://www.facebook.com/FacebookIndia/?brand_redir=108824017345866')


def opentwit():
    webbrowser.open('https://twitter.com/explore')


lblinsta = Label(root, text="Explore The Web", width=40, font=('arial', 30, "bold"), fg='#922B21')

lblinsta.pack()
lblname = Label(root, text="Select Name", width=15, font=('arial', 12, "bold"), fg='#922B21')
lblname.place(x=25, y=90)
"""
When we assign a Data frame and convert it to list, the values inside will
be enclosed in
[' at beginning and at end by ']. these need to be eliminates. hence we
use repr function to convert
object to normal string and then use slicing to eliminate these
characters from beginning and end """
final_names = []
for i in df_name:
    final_names.append(repr(i)[2:-2])
final_handles = []
for i in df_handle:
    final_handles.append(repr(i)[2:-2])
dictionary = {}
for i in range(len(final_names)):
    dictionary.update({final_names[i]: final_handles[i]})
# print(dict)
cb = Combobox(root, width=18, values=final_names, font=('Times new roman', 12, "bold"))
cb.current(0)
cb.bind("<<ComboboxSelected>>", scrape_data)
cb.place(x=50, y=130)
imginsta = ImageTk.PhotoImage(Image.open('C:\\Users\\Loukik\\Desktop\\khateeb python\\web scraping\\insta.ico'))
binsta = Button(root, image=imginsta, command=openinsta)
binsta.place(x=220, y=400)
lblopen = Label(root, width=30, text="To Visit Profile, Click here==>", font=('arial', 10, "bold"), fg='#922B21')
lblopen.place(x=-20, y=450)
root.mainloop()
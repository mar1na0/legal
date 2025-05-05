import requests 
from tkinter import *


url=requests.get('https://api.openweathermap.org')
print(url)
conversao=url.json()
print(conversao)

tela1=Tk()
tela1.title("convertor")
tela1.geometry('350x200')
tela1.wm_resizable(width=False, height=False)

tela1.mainloop()
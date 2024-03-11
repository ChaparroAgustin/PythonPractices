import tkinter as tk
import tkinter.messagebox as tkmsg

root = tk.Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Descarga videos de YouTube con Sandreke")
root.configure(bg='#AACDE2')

tk.Label(root,text = 'Descarga videos de YouTube\n con Sandreke', font ='arial 20 bold', bg='#AACDE2').pack()

link = tk.StringVar()
tk.Label(root, text = 'Pega el link aquí:', font = 'arial 15', bg='#AACDE2').place(x= 160 , y = 90)
link_enter = tk.Entry(root, width = 70,textvariable = link).place(x = 32, y = 120)

def Downloader():     
#     url =YouTube(str(link.get()))
# #     video = url.streams.first()
#     video = url.streams.get_highest_resolution()
#     video.download()
    # tk.Message(root, text = 'desea descargar?', font = 'arieal 15 bold', bg='green').place(x=180, y = 240)
    ask = tkmsg.askquestion(title="Si o No", message="Quiere descargar el archivo?")
    tk.Label(root, text = f'{ask}', font = 'arial 15 bold', bg='#AACDE2', fg='#B57199').place(x= 180 , y = 240)  
    if (ask == "no"): root.destroy()
    
tk.Button(root,text = 'DESCARGAR', font = 'arial 15 bold', bg = '#B57199', padx = 2, command = Downloader).place(x=180 ,y = 180)
root.mainloop()
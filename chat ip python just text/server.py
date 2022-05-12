import socket
import finde_open_port
import threading
import tkinter

server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=(socket.gethostbyname(socket.gethostname()),finde_open_port.ports())
print(host)
server.bind(host)
server.listen(2)
con,addr=server.accept()

window=tkinter.Tk()
window.geometry('300x400')

input_send=tkinter.Entry()
input_send.pack(fill='x')

def send ():
    con.send(input_send.get().encode())
    if input_send.get() != '':
        tkinter.Label(window,text=input_send.get(),bg='green').pack(fill='x')

def show():
    while True:
        data=str(con.recv(1024))
        data=data[2:][::-1][1:][::-1]
        if data != '':
            tkinter.Label(window,text=data,bg="white").pack(fill='x')

threading.Thread(target=show).start()

tkinter.Button(window,text='ارسال',command=send).pack()


window.mainloop()
import firebase_admin
from firebase_admin import credentials, firestore, messaging
from tkinter import *
from tkinter import scrolledtext

my_credentials = credentials.Certificate("C:/Users/Bogdan/Desktop/config.json")
app = firebase_admin.initialize_app(my_credentials)

window = Tk()
window.title("DebateTracker Notification Admin")
window.geometry('350x400')
topic_label = Label(window, text="Topic:", font=("Arial Bold", 15))
topic_label.grid(column = 0, row = 0)

topic_entry = Entry(window, width=30, font=("Arial Bold", 15))
topic_entry.grid(column=0, row = 1)


title_label = Label(window, text="Title:", font=("Arial Bold", 15))
title_label.grid(column=0, row = 2)

title_entry = Entry(window, width=30, font=("Arial Bold", 15))
title_entry.grid(column=0, row = 3)

body_label = Label(window, text="Content:", font=("Arial Bold", 15))
body_label.grid(column=0, row=4)

topic_label2 = Label(window, text="\n", font=("Arial Bold", 15))
topic_label2.grid(column = 0, row = 5)

topic_label3 = Label(window, text="\n", font=("Arial Bold", 15))
topic_label3.grid(column = 0, row = 6)

body_entry = scrolledtext.ScrolledText(window, width=30, height=4, font=("Arial Bold", 15))
body_entry.grid(column=0, row=5)

def send_notification(topic, title, body):
    message = messaging.Message(
        data = {
            'title': title,
            'body': body,
        },
        topic="/topics/" + topic,
    )

    messaging.send(message)

def submit():
    topic = topic_entry.get()
    title = title_entry.get()
    body = body_entry.get("1.0", END)
    send_notification(topic, title, body)

notify_button = Button(window, text="Notify", command=submit, font=("Arial Bold", 15))
notify_button.grid(column = 0, row = 10)




window.mainloop()




# while True:
#     print("1. text body -> send notification to user")
#     print("2. exit")

#     x = int(input())

#     if x == 2:
#         exit()
#     else:
#         title = input()
#         body = input()
#         send_notification(title, body)
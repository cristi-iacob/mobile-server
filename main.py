import firebase_admin
from firebase_admin import credentials, firestore, messaging

my_credentials = credentials.Certificate('D:\proiect mobile\server\debatetracker-75c01-firebase-adminsdk-c5xjv-e3cea6825a.json')
app = firebase_admin.initialize_app(my_credentials)

def send_notification(title, body):
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        topic="/topics/topic_name",
    )

    messaging.send(message)

while True:
    print("1. text body -> send notification to user")
    print("2. exit")

    x = int(input())

    if x == 2:
        exit()
    else:
        title = input()
        body = input()
        send_notification(title, body)
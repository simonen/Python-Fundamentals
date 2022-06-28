class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


mails = []
command = input()

while command != "Stop":
    mail_info = command.split()
    mail_obj = Email(mail_info[0], mail_info[1], mail_info[2])
    mails.append(mail_obj)
    command = input()

indices = list(map(int, input().split(", ")))

for i, mail in enumerate(mails):
    if i in indices:
        mail.send()
    print(mail.get_info())


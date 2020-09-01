from mail_app import email_send
from threading import Timer
import time

_TASKS = []
TASKS_NUMBER = 10


def worker(reciever, subject, message):
    email_send(reciever, subject, message)


def add_task(reciever, subject, message, timer):
    _TASKS.append({"reciever": reciever, "subject": subject,
                   "message": message, "timer": timer})
    t = Timer(timer, worker, args=(reciever, subject, message))
    t.start()


def show_last_emails():
    return _TASKS[-TASKS_NUMBER:]

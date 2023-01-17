from win10toast import ToastNotifier
import schedule
import time

toaster = ToastNotifier()


def notif():
    toaster.show_toast(
        "Honey, it's 11:45!",
        "Time for lunch and genocide!",
        duration=5,
        icon_path="pain.ico",
        threaded=True)

schedule.every().day.at("11:45").do(notif)

while True:
    schedule.run_pending()
    time.sleep(1)


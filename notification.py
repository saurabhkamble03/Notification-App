import time
from plyer import notification

if __name__ == "__main__":
    while(True):
        notification.notify(
            title = "Drink Water" ,
            message = "Please drink water now to keep yourself hydrated"  ,
            app_icon = "D:\Python project\icon.ico" ,
            timeout = 10 ,
        )
        time.sleep(60*60)
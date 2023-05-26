import datetime
import time

while True:
    zaman = datetime.datetime.now()
    saat = zaman.strftime("%H:%M:%S")

    print("\r", saat, end="")
    time.sleep(1)

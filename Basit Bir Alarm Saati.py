import datetime
import time

alarm_saati = input("Alarm saati (HH:MM) formatında girin: ")

while True:
    zaman = datetime.datetime.now()
    suanki_zaman = zaman.strftime("%H:%M")

    if suanki_zaman == alarm_saati:
        print("Alarm çalıyor!")
        break

    time.sleep(1)

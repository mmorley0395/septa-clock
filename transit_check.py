import requests
from datetime import datetime, timedelta, timezone
from RPLCD.i2c import CharLCD

lcd = CharLCD("PCF8574", 0x27)
lcd.clear()
bus_num = 47
bus_stop_no = 18508

schedule_url = f"https://www3.septa.org/api/BusSchedules/?req1={bus_stop_no}"
r = requests.get(schedule_url)
r = r.json()

next_three_busses = r.get(f"{bus_num}")
next_bus = next_three_busses[0]
now = datetime.now()
next_bus_time = next_bus["DateCalender"]
datetime_object = datetime.strptime(next_bus_time, "%d/%m/%y %I:%M %p")
arrives_in = datetime_object - now
minutes = str(arrives_in)[:4]

lcd.write_string(f"the {bus_num} comes\n\rin {minutes} minutes")

import requests

bus_num = 47
bus_stop_no = 18508

schedule_url = f"https://www3.septa.org/api/BusSchedules/?req1={bus_stop_no}"

r = requests.get(schedule_url)
r = r.json()

next_three = r.get(f"{bus_num}")

next_bus = next_three[0]
second_bus = next_three[1]
third_bus = next_three[2]

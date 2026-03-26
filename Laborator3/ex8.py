import datetime

data = datetime.datetime(2023, 4, 24, 9, 33, 32, 744178)
print(data)

print("Anul: ", data.year)
print("Luna: ", data.month)
print("Ziua: ", data.day)
print(f"Ora: {data.hour}:{data.minute}:{data.second}.{data.microsecond}")
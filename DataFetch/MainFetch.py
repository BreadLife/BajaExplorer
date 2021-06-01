import Fetcher as Ft

#Ft.Lora_setup()

while(1):
    raw_data = Ft.COM15_fetch()
    print(raw_data)
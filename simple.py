from netmiko import ConnectHandler

kapcsolo = {
    "device_type" : "cisco_ios",
    "host" : "192.168.40.57",
    "username" : "oli",
    "password" : "wsw",
}

kapcsolat = ConnectHandler(**kapcsolo)

print(kapcsolat.find_prompt())

print(dir(kapcsolat))

print(kapcsolat.disconnect())

from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.57",
    "username": "oli",
    "password": "wsw"
}

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
        tftp_ip = input("Add meg a TFTP szerver IP címét: ")
        fajl_nev = input("Add meg a mentendő fájlnevet: ")
        
        mentes_sorok = "copy running tftp", tftp_ip, fajl_nev

        print(kapcsolat.send_multiline_timing(mentes_sorok))


except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")

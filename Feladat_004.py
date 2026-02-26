from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.57",
    "username": "oli",
    "password": "wsw"
}

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
        kapcsolat.send_config_set(["login block-for 600 attempts 3 within 180"])
        print(kapcsolat.send_command("show run | include password"))
        
        jelszavak = []
        
        ena = kapcsolat.send_command("show run")
        if "enable password" in ena:
            if len(kapcsolat.send_command("show run | include enable password").split(' ')[-1]) < 8:
                print("A privilegizált jelszó nem megfelelő hosszúságú.")
                enajelszo = input("ADj meg egy legalább 8 karakter hosszú jelszót: ")
                kapcsolat.send_config_set(f"enable password {enajelszo}")
        
        ena = kapcsolat.send_command("show run")
        if "username" in ena:
            val = kapcsolat.send_command("show run | include username").split('\n')
            print(val)
            
            for felh in val:
                if len(felh.split(' ')[-1]) < 8:
                    print(f"A {felh.split(' ')[1]} felhasználó jelszava nem megfelelő hosszúságú.")
                    usejelszo = input("Adj meg egy legalább 8 karakter hosszú jelszót: ")
                    while len(usejelszo) < 8:
                        usejelszo = input("Adj meg egy legalább 8 KARAKTER HOSSZÚ jelszót!: ")
                    osszerakott = ''
                    for szo in felh.split(' ')[:-2]:
                        osszerakott += szo + ' '
                    kapcsolat.send_config_set(f"{osszerakott}{usejelszo}")
                    print("A jelszó beállítása megtörtént.(°_,°)")
            
                    
            
                
            

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")
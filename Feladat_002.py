from netmiko import ConnectHandler

login_adatok = {
    "device_type": "cisco_ios",
    "host": "192.168.40.57",
    "username": "oli",
    "password": "wsw"
}

vlanparancsok = [
    "vlan 10",
    "name Tanulo",
    "vlan 20",
    "name Oktato",
    "vlan 30",
    "name Pedagogus",
    "vlan 100",
    "name Ugyvitel"
]

def vlanok(sshkapcs):
    sshkapcs.send_config_set(vlanparancsok)
    

# ---------------------------
# PROGRAM
# ---------------------------

try:
    with ConnectHandler(**login_adatok) as kapcsolat:
        
       
       
        # 1. feladat
       
        vlanok(kapcsolat)
        print(kapcsolat.send_command("show vlan brief"))
       
        # 2. feladat
       
        """ if  "password konzolPass" in kapcsolat.send_command("sh run | section line con 0"):
            if "login" in kapcsolat.send_command("sh run | section line con 0"):
                print("Be van állítva a jelszó és jó helyen.")
            else:
                print("NIncs login de egyébként be van állítva a jelszó és jó helyen.")
        elif "password konzolPass" in kapcsolat.send_command("sh run"):
                print("Be van állítva a jelszó de nem a megfelelő helyen!")
        else:
                print("Nincs beállítva a jó jelszó!")
             """
             
        if  "password" in kapcsolat.send_command("sh run | section line con 0"):
            if kapcsolat.send_command("sh run | section line con 0").endswith("login"):
                print("Konzol jelszó és hitelesítés beállítása OK!")
            else:
                print("NIncs login !")
        else:
                print("Nincs beállítva jelszó!")
    
        # 3. feladat
        
        kapcsolat.send_config_set(("line con 0 ", "password konJelszo")) 
        print(kapcsolat.send_command("show run | section line con 0"))
        
        # 4. feladat
        
        #print(len(kapcsolat.send_command("show ip int br").split('\n')[2::]),kapcsolat.send_command("show ip int br").split('\n')[2].split()[0].split('1')[0],"interfész található a szviccsen")
        
        interface_lista = kapcsolat.send_command("show ip interface brief | include Ethernet").split('\n')
        print(len(interface_lista))
        
        for i in range(len(interface_lista)):
            interface_lista[i] = interface_lista[i].split('/')[0]
            interface_lista[i] = interface_lista[i][:-1]
        
        print(interface_lista)
        
        fajtak_lista = []
        
        for interface in interface_lista:
            if interface not in fajtak_lista:
                fajtak_lista.append(interface)
        
        print(fajtak_lista)
        
        for fajta in fajtak_lista:
            db = 0
            for interface in interface_lista:
                if interface == fajta:
                    db += 1
            print(db,"darab",fajta,"interfész található a szviccsen.")
                    

except Exception as ex:
    print(f"Csatlakozási hiba: {ex}")

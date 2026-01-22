from netmiko import ConnectHandler

def netmikoshooversion():
    kapcsolo = {
            "device_type" : "cisco_ios",
            "host" : "192.168.40.169",
            "username" : "admin",
            "password" : "oli",
        }

    kimenet = ''

    try:
        with ConnectHandler(**kapcsolo) as kapcsolat:
        
            kimenet = kapcsolat.send_command("show version")
        
    except Exception as hb:
        print(hb)

    print(kimenet)
    
def fajlbeolvas():
    try:
        
        with open("showversion.txt") as fajl:
            kimenet = fajl.read()
            
    except IOError as hib:
        print(hib)
    
    return kimenet

def ethernetinterfeszszama(verzzinfo):
    pass

def milyeniosverzio(verzzinfo):
    
    elsosor = verzzinfo.split('\n')[0]
    
    sormintlista = elsosor.split(",")
    
    ver = sormintlista[1].strip().split(' ')[2].rstrip(')').lstrip('(')
    zio = sormintlista[2].strip().split(' ')[1]
    print("IOS verzió:",ver,zio)
    
# HÁNY ETHERNET INTERFACE VAN A KAPCSOLÓN?


""" 
    PROGRAM
"""
verzzinfo = fajlbeolvas()
milyeniosverzio(verzzinfo)
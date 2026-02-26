def konzoljelszoell():
    valasz = "line con 0\n password Jelszo123\n logging synchronous\n login"
    sorlista = valasz.split('\n')
    kellista = []
    
    for i in range(len(sorlista)):
        sor = sorlista[i].strip()
        if "password" in sor or sor == "login":
            kellista.append(sor)
        
    if len(kellista) == 2:
        print("Jól be van állítva a konzol jelszóvédelme.")
    elif len(kellista) == 0:
        print("Nincs beállítva jelszóvédelem!")
    elif kellista[0] == "login":
        print("A login paracs ki van adva de nincs beállítva jelszó!")
    else:
        print("A jelszó be van állítva de nincs kiadva a login parancs!")


konzoljelszoell()
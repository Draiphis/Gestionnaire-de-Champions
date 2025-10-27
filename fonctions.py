def ajouter_un_champion():
    Nom=str(input("Quel est le Nom du Champion ? : "))
    Roles={1:"Toplane",2:"Jungle",3:"Midlane",4:"ADC",5:"Support"} 
    Classes={1:"Tank",2:"Mage",3:"Tireur",4:"Juggernaut",5:"Bruiser",6:"Assassin"}
    Degats={1:"Physique",2:"Magique",3:"Mixed"}
    while True:
        print(Roles)
        numero_role=int(input(f"Indiquez le numéro correspondant au role de {Nom} (appuyez sur q pour quitter)"))
        if numero_role.lower()=="q":
            break
        if numero_role not in Roles:
            print("votre choix n'est pas dans les roles disponibles")
            continue
        else:
            Role=Roles[numero_role]
            break
    while True:
        print(Classes)
        numero_classe=int(input(f"Indiquez le numéro correspondant à la classe de {Nom} (appuyez sur q pour quitter)"))
        if numero_classe.lower()=="q":
            break
        if numero_classe not in Classes:
            print("votre choix n'est pas dans les classes disponibles")
            continue
        else:
            Classe=Classes[numero_classe]
            break
    while True:
        print(Degats)
        numero_degat=int(input(f"Indiquez le numéro correspondant au type de dégats de {Nom} (appuyez sur q pour quitter)"))
        if numero_degat.lower()=="q":
            break
        if numero_degat not in Degats:
            print("votre choix n'est pas dans les classes disponibles")
            continue
        else:
            Degat=Degats[numero_degat]
            break
    
        

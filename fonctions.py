import csv
  



def ajouter_un_champion():
    nom_existant=set()
    with open("champions.csv", 'r', encoding='utf-8', newline='') as f:
        reader=csv.DictReader(f)
        for lign in reader:
            nom_existant.add(lign["Nom"])
    while True:
        Nom=str(input("Quel est le Nom du Champion ? (q pour quitter) : "))
        if Nom.strip().lower()=="q":
            break

        if Nom.strip().capitalize() in nom_existant:
            print("Champions déjà dans la liste")
            continue
        else:
            break
    

    Roles={"1":"Toplane","2":"Jungle","3":"Midlane","4":"ADC","5":"Support"} 
    Classes={"1":"Tank","2":"Mage","3":"Tireur","4":"Juggernaut","5":"Bruiser","6":"Assassin"}
    Degats={"1":"Physique","2":"Magique","3":"Mixed"}
    while Nom.strip().lower()!="q":
        print(Roles)
        numero_role=input(f"Indiquez le numéro correspondant au role de {Nom} (appuyez sur q pour quitter) : ")
        if numero_role.strip().lower()=="q":
            break
        if numero_role not in Roles:
            print("votre choix n'est pas dans les roles disponibles")
            continue
        else:
            Role=Roles[numero_role]


        print(Classes)
        numero_classe=input(f"Indiquez le numéro correspondant à la classe de {Nom} (appuyez sur q pour quitter) : ")
        if numero_classe.strip().lower()=="q":
            break
        if numero_classe not in Classes:
            print("votre choix n'est pas dans les classes disponibles")
            continue
        else:
            Classe=Classes[numero_classe]
        print(Degats)
        numero_degat=input(f"Indiquez le numéro correspondant au type de dégats de {Nom} (appuyez sur q pour quitter) : ")
        if numero_degat.strip().lower()=="q":
            break
        if numero_degat not in Degats:
            print("votre choix n'est pas dans les classes disponibles")
            continue
        else:
            Degat=Degats[numero_degat]
        
        
        played=input(f"Avez-vous déjà joué {Nom} (Oui ou non //  appuyez sur q pour quitter) : ")
        if played.strip().lower()=="q":
            break
        if played.strip().lower()!= ("oui" or "non"):
            print("choix invalide")
            continue
        else:
            play=played
        with open("champions.csv", 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([Nom.strip().capitalize(), Classe, Role, Degat,play.strip().capitalize()])
        break
    


        
def afficher_champions():
    with open("champions.csv", 'r', encoding='utf-8', newline='') as f:
        reader=csv.DictReader(f)
        for ligne in reader:
            affichage = f"Nom => {ligne['Nom']} | Role => {ligne['Role']} | Classe => {ligne['Classe']} | Type_de_Dégats => {ligne['Type_de_Dégats']} | {ligne["Déjà_Joué"]}"
            print(f"{affichage}\n")



def rechercher_un_champion():
    with open("champions.csv", "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        champions = list(reader)
        recherche=input("Entrez la suite de lettre à rechercher : ").strip().lower()
        for champion in champions :
            if recherche in champion['Nom'].lower():
                affichage = f"Nom => {champion['Nom']} | Role => {champion['Role']} | Classe => {champion['Classe']} | Type_de_Dégats => {champion['Type_de_Dégats']}"
                print(f"\n{affichage}\n")

def supprimer_un_champion():
    
    with open("champions.csv", "r", encoding="utf-8") as f:
        reader = list(csv.DictReader(f))
        fieldnames = reader[0].keys()

    
    suppression = input("Entrez le nom du champion : ").strip()

    
    count = -1
    for i, ligne in enumerate(reader):
        if ligne["Nom"].lower() == suppression.lower():
            count = i
            break

    if count == -1:
        print(f"Le champion '{suppression}' n'a pas été trouvé.")
        return

    
    del reader[count]

    
    with open("champions.csv", "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(reader)

    print(f"Le champion '{suppression}' a été supprimé avec succès.")



def menu():
    while True :
        menus={"1":"Afficher les champions","2":"Ajouter des champions","3":"Rechercher des champions","4":"Supprimer un champion" ,"q":"Quitter"}
        for cle, valeur in menus.items():
            print(f"{cle} : {valeur}")
        choix=input("Que voulez vous faire ? (Entrez le numéro correspondant ou q) : ")
        if choix.strip().lower()=="q":
            confirmation=input("Voulez-vous Quitter le menu ? (Oui ou Non) : ")
            if confirmation.strip().lower()=="oui":
                print("vous avez quitté le menu")
                break
            elif confirmation.strip().lower()=="non":
                print("retour au menu principal")
                continue
            else:
                print("choix invalide, retour au menu principal")
                continue
        if choix.strip().lower() == "1":
            afficher_champions()
            continue
        if choix.strip().lower()== "2":
            ajouter_un_champion()
            continue
        if choix.strip().lower()== "3":
            rechercher_un_champion()
            continue
        if choix.strip().lower()== "4":
            supprimer_un_champion()
            continue





menu()


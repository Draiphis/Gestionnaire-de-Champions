import csv
  

def ajouter_un_champion():
    nom_existant=set()
    with open("champions.csv", 'r', encoding='utf-8', newline='') as f:
        reader=csv.DictReader(f)
        for lign in reader:
            nom_existant.add(lign["Nom"])
    while True:
        Nom=str(input("Quel est le Nom du Champion ? : "))
        if Nom.strip().lower()=="q":
            break

        if Nom in nom_existant:
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
        with open("champions.csv", 'a', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([Nom, Classe, Role, Degat])
        break
    
        
def afficher_champions():
     with open("champions.csv", 'r', encoding='utf-8', newline='') as f:
        reader=csv.DictReader(f)
        for ligne in reader:
            affichage = f"Nom => {ligne['Nom']} | Role => {ligne['Role']} | Classe => {ligne['Classe']} | Type_de_Dégats => {ligne['Type_de_Dégats']}"
            print(f"{affichage}\n")

afficher_champions()
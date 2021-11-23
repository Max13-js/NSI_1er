def AjouterUnNuméro(name,n):
    """Ecrire dans le fichier text un nom et un numéro"""
    with open("tel.txt", "a") as f:
        f.write(name + " " + str(n) + "\n")
        return print("Le numéro de {0} a bien été ajouté".format(name))


def TrouverUnNumero(name):
    """Trouver un numéro par le nom"""
    with open("tel.txt", "r") as f:
        for line in f:
            if name in line:
                return print(line.split()[1])
        return print("Le nom n'existe pas")

def TrouverUnNom(num):
    """Trouver un nom par le numéro"""
    with open("tel.txt", "r") as f:
        for line in f:
            if num in line:
                return print(line.split()[0])
        return print("Le numéro n'existe pas")

def SupprimerUnNumero(name):
    """Supprimer un numero par le nom"""
    with open("tel.txt", "r") as f:
        lines = f.readlines()
    with open("tel.txt", "w") as f:
        for line in lines:
            if name not in line:
                f.write(line)
    return print("Le numéro a bien été supprimé")

def ModifierUnNuméro(name,n):
    """Modifier un numéro par le nom"""
    with open("tel.txt", "r") as f:
        lines = f.readlines()
    with open("tel.txt", "w") as f:
        for line in lines:
            if name in line:
                f.write(name + " " + str(n) + "\n")
            else:
                f.write(line)
    return print("Le numéro a bien été modifié")

def afficher():
    with open("tel.txt", "r") as f:
        for line in f:
            print(line)
def existedeja(name):
    with open("tel.txt", "r") as f:
        for line in f:
            if name in line:
                return True
    return False
def numexistedeja(num):
    with open("tel.txt", "r") as f:
        for line in f:
            if num in line:
                return True
    return False

def sauvegarde():
    """Copie colle le fichier tel.txt dans un nouveau fichier pour faire une sauvegarde avec la date de celle-ci"""
    import datetime
    now = datetime.datetime.now()
    with open("tel.txt", "r") as f:
        lines = f.readlines()
    with open("save_{0}-A-{1}h-{2}.txt".format(now.strftime("%Y-%m-%d"), now.strftime("%H"), now.strftime("%M")), "w") as f:
        for line in lines:
            f.write(line)
    return print("Sauvegarde effectuée")

def trier():
    with open("tel.txt", "r") as f:
        lines = f.readlines()
    with open("tel.txt", "w") as f:
        lines.sort()
        for line in lines:
            f.write(line)
    return print("Trie du répertoire en cours...")

def carnet():
    print("""

[0] Quitter le programme
[1] Ecrire dans le répertoire
[2] Chercher dans le répertoire un numéro
[3] Chercher dans le répertoire un nom
[4] Supprimer un numéro
[5] Modifier un numéro
[6] Afficher le contenu du répertoire
[7] Sauvegarder le contenu du répertoire
\n""")
    choice = int(input("Veuillez entrer votre choix : "))
    while choice != 0:
        if choice == 1:
            name = input("Entrez le nom : ")
            if(name == "retour"):
                carnet()
            elif(existedeja(name)):
                print("Le nom existe déjà")
                carnet()
            else:
                num = input("Entrez le numéro : ")
                if(num == "retour"):
                    carnet()
                elif(numexistedeja(num)):
                    print("Le numéro existe déjà")
                    carnet()
                else:
                    AjouterUnNuméro(name,num)
                    carnet()
        elif choice == 2:
            name = input("Entrez le nom : ")
            if (name == "retour"):
                carnet()
            elif(existedeja(name)):
                print("Le nom n'existe pas")
                carnet()
            else:
                TrouverUnNumero(name)
                carnet()
        elif choice == 3:
            num = input("Entrez le numéro : ")
            if(num == "retour"):
                carnet()
            else:
                TrouverUnNom(num)
                carnet()
        elif choice == 4:
            name = input("Entrez le nom : ")
            if (name=="retour"):
                carnet()
            elif(existedeja(name)):
                SupprimerUnNumero(name)
                carnet()
            else:
                print("Le nom n'existe pas")
                carnet()
        elif choice == 5:
            name = input("Entrez le nom : ")
            if (name == "retour"):
                carnet()
            else:
                num = input("Entrez le numéro : ")
                if (num == "retour"):
                    carnet()
                elif(existedeja(name)):
                    ModifierUnNuméro(name,num)
                    carnet()
                else:
                    print("Le nom n'existe pas")
                    carnet()  
        elif choice == 6:
            trier()
            afficher()
            carnet()
        elif choice == 7:
            sauvegarde()
            carnet()
        else:
            print("Choix invalide")
            carnet()
        break
carnet()

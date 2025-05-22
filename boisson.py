
def afficher_menu():
    print("FICHE DE CHOIX")
    print("1.Café")
    print("2.Thé")
    print("3.Eau chaud")
    print("4. Quitter")

def traiter_choix(a):
    if   a == "1":
        print("Vous avez choisi Café.")
    elif a == "2":
        print("Vous avez choisi Thé.")
    elif a == "3":
        print("Vous avez choisi Eau chaud .")
    elif a == "4":
        print(" Aurevoire.")
        return False
    else:
        print("Choix invalide.")
    return True

def menu():
    continuer = True
    while continuer:
        afficher_menu()
        choix = input("Faites un choix : ")
        continuer = traiter_choix(choix)

menu()

from selenium import webdriver
import time

# Demander le code
code = input("Entrez le code: ")
if code != "kohscript":
    print("Code incorrect.")
    exit()

# Demander le choix de l'utilisateur
choix = input("Choisissez une option (1: View, 2: Follow): ")
if choix == "1":
    # Option View
    nb_vues = int(input("Entrez le nombre de vues souhaité: "))
    url = input("Entrez l'URL à ouvrir: ")

    for i in range(nb_vues):
        print(f"Ouverture de la vue {i + 1}")
        # Créer une nouvelle instance du navigateur à chaque itération
        driver = webdriver.Chrome()  # Assurez-vous que chromedriver est dans votre PATH
        driver.get(url)
        time.sleep(15)
        driver.quit()
        print(f"Fermeture de la vue {i + 1}")

else:
    print("Option non prise en charge pour le moment.")

print("Script terminé.")

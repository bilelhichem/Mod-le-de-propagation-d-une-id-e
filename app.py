import random

# Fonction de simulation d'une interaction entre deux joueurs
def interaction(joueur1, joueur2):
    if joueur1 == 'D' and joueur2 == 'D':
        return (0, 0)  # Les deux défecteurs ne coopèrent pas
    elif joueur1 == 'D' and joueur2 == 'C':
        return (3, -1)  # Le défecteur gagne 3, le coopérateur perd 1
    elif joueur1 == 'C' and joueur2 == 'D':
        return (-1, 3)  # Le coopérateur perd 1, le défecteur gagne 3
    elif joueur1 == 'C' and joueur2 == 'C':
        return (2, 2)  # Les deux coopérateurs se donnent 2 points chacun

# Fonction qui gère le jeu pour chaque joueur
def jouer_tour():
    # Simuler un jeu entre deux joueurs : joueur1 (toujours défecteur), joueur2 (peut être C ou D)
    joueur1 = 'D'  # Joueur défecteur
    joueur2 = random.choice(['C', 'D'])  # Joueur coopérateur ou défecteur au hasard
    
    # Interaction entre les deux joueurs
    score1, score2 = interaction(joueur1, joueur2)
    
    print(f"Joueur 1 (D) choisit: {joueur1} | Joueur 2 choisit: {joueur2}")
    print(f"Scores -> Joueur 1: {score1}, Joueur 2: {score2}")

# Simuler plusieurs tours du jeu
def simulation(n):
    for i in range(n):
        print(f"Tour {i + 1}:")
        jouer_tour()
        print("-" * 30)

# Exécution de la simulation pour 5 tours
simulation(5)

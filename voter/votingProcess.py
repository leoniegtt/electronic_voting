def vote():
    validvote = False
    while not validvote:
        print("Here are the candidates : ")
        # récup la liste des candidats à partir de la bdd
        candidates = {
            1 : "Alata",
            2 : "Migliore",
            3 : "Bit-Monnot",
            4 : "Nicomette"
        }
        print(candidates)
        vote=int(input("Enter your vote (number from 1 to 4) : "))
        
        if vote not in candidates:
            print("Invalid vote. Please enter a valid number from 1 to 4.")
        else:
            print("You voted for", candidates[vote] + ".")
            # à faire : vérifier que c'est bien la personne pour qui on veut voter
            validvote = True
    # cast vote avec protection => Pailler 

vote()
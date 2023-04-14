import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

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
            invalid = True
            while invalid:
                # vérifier que c'est bien la personne pour qui on veut voter
                yorn = input("Are you sure about you vote? yes (y) or no (n) ")
                if yorn == "y":
                    validvote = True
                    invalid = False
                elif yorn == "n":
                    validvote = False
                    invalid = False
                else: 
                    print("Invalid answer. Please enter y for yes and n for no.")
    print ("Your vote has been casted. Goodbye.")
    
    # chiffrer vote => Pailler
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    s.send(bytes(str(vote),"utf-8"))
    data = s.recv(BUFFER_SIZE)
    print( "received data:\n", data.decode("utf-8"))
    s.close()
                
     

import sqlite3
from gmpy2 import mpz
connect = sqlite3.connect("Serveur_Orga/dbb_orga.db")
cursor = connect.cursor()

#RECUPERE LES INFORMATIONS DES CANDIDATS DE LA BDD ET LES RETOURNE SOUS LA FORME D'UN DICTIONNAIRE

# return dictionnary with key : number, first_name last_name, election_number
def getCandidates() :
    m=[]
    m.append( mpz(10))
    m.append(mpz(1))
    #m.append(mpz(0))
    m.append(mpz(2000))
    m.append( mpz(4000))
    m.append( mpz(999))

    res = cursor.execute("SELECT * FROM Liste_candidats")
    connect.commit()
    res = list(res.fetchall())
    res_dict = {}
    res_dict[0]= ("blank_vote",mpz(1))

    for i in range(1,len(res)+1) :
        aux = res[i-1]
        res_dict[i]= (aux[0] + " " + aux[1],mpz (10**(i+2)))
    return res_dict

def transformCandidates(candidates_dico) :
    candidates = dict()
    candidates_num =[]
    for i in range(0, len(candidates_dico) ) :
        (name , numbers) = candidates_dico[i]
        candidates[i] = name
        candidates_num.append(numbers)
    return (candidates, candidates_num)

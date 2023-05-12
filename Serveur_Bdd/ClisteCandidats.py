import sqlite3
from gmpy2 import mpz
connect = sqlite3.connect("Serveur_Bdd/dbb_pir.db")
cursor = connect.cursor()

#RECUPERE LES INFORMATIONS VOTANTS DE LA BDD ET LES RETOURNE SOUS LA FORME D'UN DICTIONNAIRE



# return dictionnary with key : number, first_name last_name
def getCandidates() :
    res = cursor.execute("SELECT * FROM Liste_candidats")
    connect.commit()
    res = list(res.fetchall())
    res_dict = {}
    res_dict[0]= ("vote blanc",int(mpz(1)))
    for i in range(1,len(res)+1) :
        aux = res[i-1]
        res_dict[i]= (aux[0] + " " + aux[1],int(mpz(10**(i+2))))
    return res_dict

def main() :
    getCandidates()
    
if __name__ == "__main__" :
    main()

 
    
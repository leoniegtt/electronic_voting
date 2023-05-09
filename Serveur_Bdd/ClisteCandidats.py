import sqlite3

connect = sqlite3.connect("Serveur_Bdd/dbb_pir.db")
cursor = connect.cursor()

#RECUPERE LES INFORMATIONS VOTANTS DE LA BDD ET LES RETOURNE SOUS LA FORME D'UN DICTIONNAIRE


# return dictionnary with key : number, first_name last_name
def getCandidates() :
    res = cursor.execute("SELECT * FROM Liste_candidats")
    connect.commit()
    res = list(res.fetchall())
        
    res_dict = {}

    for i in range(len(res)) :
        aux = res[i]
        res_dict[i+1]= aux[0] + " " + aux[1]

    return res_dict
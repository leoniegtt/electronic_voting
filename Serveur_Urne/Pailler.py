from paillierlib import paillier
from gmpy2 import mpz


def initialize():
    #key generation (public/private)
    key_pair = paillier.keygen()

    #assign a number to each candidate, also to a blank vote
    nb_of_candidates = x

    #choose the number assigned to candidates depending on how many people vote
    for i in nb_of_candidates:
        candidate_i=mpz(pow(10,i+2)) # the number assigned to the candidate is 10^i+2
    blank_vote=mpz(1)

    #initialize the sum
    sum=paillier.encrypt(mpz(0), key_pair.public_key)


def cipher():
    #initialize number of votes counted
    nb_votes=0

    for candidate in votes:
        cipher=paillier.encrypt(mpz(candidate),key_pair.public_key)
        print("création du chiffré")
        #update sum by adding new vote
        sum+=cipher
        #update number of votes counted
        nb_votes+=1


def decipher():
#decryption (TO DO : move to different file later)
    results=paillier.decrypt(sum, key_pair.private_key)
    print("vote results:\n{0}".format(results))

    #modular division to reveal number of votes for each candidate
    for i in nb_of_candidates
        candidate_i_votes=gmpy2.f_divmod(results, candidate_i)
        print("Candidate i votes : {0}".format(candidate_i_votes))
#!/usr/bin/env python

from paillierlib import paillier
from gmpy2 import mpz

#key generation (public/private)
key_pair = paillier.keygen()
#initialize number of votes counted
nb_votes=0

def initialize():
  
    #assign a number to each candidate, also to a blank vote
    nb_of_candidates = 3

    #choose the number assigned to candidates depending on how many people vote
    candidate_1=mpz(1)
    candidate_2=mpz(100000)
    candidate_3=mpz(100000000000000) # the number assigned to the candidate is 10^i+2
    blank_vote=mpz(1)

    #initialize the sum
    sum=paillier.encrypt(mpz(0), key_pair.public_key)

def get_public_key ():
    return key_pair.public_key

def update_new_vote():
    #faire un udp en attente de vote Quad vote appel fonction pour mettre à jour
    #update sum by adding new vote
    sum+=cipher # todo revoir lib paillier
    #update number of votes counted
    nb_votes+=1


def decipher():
#decryption (TO DO : move to different file later)
    results=paillier.decrypt(sum, key_pair.private_key)
    print("vote results:\n{0}".format(results))

    #modular division to reveal number of votes for each candidate
    for i in  range(nb_of_candidates.__sizeof__):
        candidate_i_votes=gmpy2.f_divmod(results, candidate_i)
        print("Candidate i votes : {0}".format(candidate_i_votes))

def main():
    #test
    initialize()
    candidate_1=mpz(10)
    candidate_2=mpz(100000)
    candidate_3=mpz(100000000000000) # the number assigned to the candidate is 10^i+2
    blank_vote=mpz(1)
    votes=[('A',candidate_3), ('B',candidate_2),('C',candidate_3),
       ('D',candidate_2),('E',candidate_3),('F',candidate_1),
       ('G',candidate_3), ('H',candidate_2),('J',candidate_3),
      ('K',candidate_1),('L',candidate_2),('M',candidate_3)]
    for voter,candidate in votes:
        print("Voter: {0}".format(voter))
        print("Vote Ciphertext:\n\n{0}".format(ciphertext.c))
        update_new_vote()
    print("chiffre sum:  \n{0}".format(sum))
    decipher()


if __name__ == "__main__":
    main()
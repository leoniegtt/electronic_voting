#!/usr/bin/env python

from paillierlib import paillier
from gmpy2 import mpz
from gmpy2 import f_divmod

def get_public_key ():
    return key_pair.public_key

def main():
    nb_votes=0

    key_pair = paillier.keygen()

    #assign a number to each candidate, also to a blank vote
    nb_of_candidates = 3

    #choose the number assigned to candidates depending on how many people vote
    candidate_1=mpz(1)
    candidate_2=mpz(100000)
    candidate_3=mpz(100000000000000) # the number assigned to the candidate is 10^i+2
    blank_vote=mpz(1)

    #initialize the sum
    sum=paillier.encrypt(mpz(0), key_pair.public_key)

    #initialize anonymous votes
    anon_votes=[]
    #test
    sum=paillier.encrypt(mpz(0), key_pair.public_key)

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
        ciphertext=paillier.encrypt(mpz(candidate), key_pair.public_key)
        print("Vote Ciphertext:\n\n{0}".format(ciphertext.c))
        sum+=ciphertext
        anon_votes.append(ciphertext)
        nb_votes+=1
    print("chiffre sum:  \n{0}".format(sum))

    #decryption (TO DO : move to different file later)
    results=paillier.decrypt(sum, key_pair.private_key)
    print("vote results:\n{0}".format(results))

    #modular division to reveal number of votes for each candidate
    candidate_3_votes, _voting_results=f_divmod(results,candidate_3)
    print("Candidate 3 votes: {0}".format(candidate_3_votes))
    candidate_2_votes, candidate_1_votes=f_divmod(_voting_results,candidate_2)
    print("Candidate 2 votes: {0}".format(candidate_2_votes))
    print("Candidate 1 votes: {0}".format(candidate_1_votes))


if __name__ == "__main__":
    main()
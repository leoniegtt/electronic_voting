#!/usr/bin/env python


from gmpy2 import f_divmod
from gmpy2 import mpz
from paillierlib import paillier
from numpy import zeros,array
"""
print(type(sum))
print((sum.c))
x = str(sum.c) + "\n" + str(sum.n)
print(x)
sum = None
xc = mpz(x.split("\n")[0])
xn = mpz(x.split("\n")[1])
sum = paillier.PaillierCiphertext(xc, xn)
print("ooo", sum)
x = str(sum.c) + "\n" + str(sum.n)
print(x)
print(type(sum.c))
"""

def get_public_key (key_pair):
    return key_pair.public_key

def get_private_key (key_pair):
    return key_pair.private_key

def generate_key ():
    key_pair = paillier.keygen()
    return key_pair

def assign_num_candidate (nb_of_candidates):
    #assign a number to each candidate, also to a blank vote
    candidates = zeros(nb_of_candidates+1, int)
    candidates[0] = mpz(1)
    for i in range(1 , nb_of_candidates+1):
        candidates[i] = mpz (10**(i+2))
    return candidates


def chiffrement_vote( public_key, candidate) :
    ciphertext=paillier.encrypt(mpz(candidate), public_key)
    return ciphertext

def compteur (votes,key_pair):
    nb_votes=0
    #initialize the sum
    sum=paillier.encrypt(mpz(0), key_pair.public_key)
    #initialize anonymous votes
    anon_votes=[]
    for voter,candidate in votes:
        print("Voter: {0}".format(voter))
        ciphertext=paillier.encrypt(mpz(candidate), key_pair.public_key)
        print("Vote Ciphertext:\n\n{0}".format(ciphertext.c))
        sum+=ciphertext
        anon_votes.append(ciphertext)
        nb_votes+=1
    print("chiffre sum:  \n{0}".format(sum))
    return sum

def decipher (sum, key_pair) :
    #decryption (TO DO : move to different file later)
    results = paillier.decrypt(sum, key_pair.private_key)
    print("vote results:\n{0}".format(results))
    return results

def division(candidates, results, nb_of_candidates) :
    candidate_votes = zeros(nb_of_candidates+1, int)
    candidate_votes[nb_of_candidates], _voting_results=f_divmod(results,int(candidates[nb_of_candidates]))
    print("Candidate " + str(nb_of_candidates) +" votes: {0}".format(int(candidate_votes[nb_of_candidates])))
    for i in range(nb_of_candidates-1 ,0,-1):
        candidate_votes[i] , _voting_results = f_divmod(_voting_results,int(candidates[i]))
        print("Candidate " + str(i) +" votes: {0}".format(int(candidate_votes[i])))
    #modular division to reveal number of votes for each candidate

def create_list_vote(nb_of_candidates) :
    votes = zeros(nb_of_candidates, int)
    return votes
def vote_add_List( votant , vote, votes) :
    votes.add((votant,vote))

def main ():
    key_pair = paillier.keygen()
    get_public_key (key_pair)
    get_private_key (key_pair)
    nb_of_candidates = 3
    candidates = assign_num_candidate (nb_of_candidates)
    votes=[('A',candidates[3]), ('B',candidates[2]),('C',candidates[3]),
       ('D',candidates[2]),('E',candidates[3]),('F',candidates[1]),
       ('G',candidates[3]), ('H',candidates[2]),('J',candidates[3]),
       ('K',candidates[1]),('L',candidates[2]),('M',candidates[3])]
    sum = compteur (votes,key_pair)
    results = decipher(sum,key_pair)
    division(candidates , results, nb_of_candidates)


def example_votes() :
    key_pair = paillier.keygen()
    get_public_key (key_pair)
    get_private_key (key_pair)
    nb_of_candidates = 3
    candidates = assign_num_candidate (nb_of_candidates)
    votes=[candidates[3], candidates[2],candidates[3],candidates[2],candidates[3],candidates[1],candidates[3]
    ,candidates[2],candidates[3],candidates[1],candidates[2],candidates[3]]
    sum = compteur (votes,key_pair)
    results = decipher(sum,key_pair)
    division(candidates , results, nb_of_candidates)


def main1():
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

    votes=[('A',candidate_3), ('B',candidate_2),('C',candidate_3),
       ('D',candidate_2),('E',candidate_3),('F',candidate_1),
       ('G',candidate_3), ('H',candidate_2),('J',candidate_3),
      ('K',candidate_1),('L',candidate_2),('M',candidate_3)]
    for voter,candidate in votes:
        print("Voter: {0}".format(voter))
        ciphertext=paillier.encrypt(mpz(candidate), key_pair.public_key)
        print("Vote Ciphertext:\n\n{0}".format(ciphertext.c))
        sum+=(ciphertext)
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



from gmpy2 import mpz
def assign_num_candidate (nb_of_candidates):
    #assign a number to each candidate, also to a blank vote

    candidates = zeros(nb_of_candidates+1, int)
    candidates[0] = mpz(1)
    for i in range(1 , nb_of_candidates+1):
        candidates[i] = mpz(10**(i+2))
    return candidates

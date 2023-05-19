# Electronic voting system based on tokens and Paillier cryptosystem

Paper ballot voting has been the standard method regarding elections, being used in most countries around the world. Yet voting by paper ballot is not without its limitations: paper ballots can be lost, misread or miscounted leading to inaccurate vote counts and disputes over the election results.

We propose a Paillier cryptosystem and token based architecture to solve various issues that appear in the voting process.

Our implementation simply consists of a terminal interface to allow the user to cast a vote, we would like to include a web interface in the future to be more accessible.

## Architecture Diagram
Our system is composed of 3 main sub-systems. 
TO DO : ADD GRAPH


Firstly, the verification server generates the pair of Paillier cryptographic keys that will be used for an election. It will also retrieve the encrypted results, decrypt them and publish them. It is the only part of the system that contains the private key that allows to decrypt any message encrypted with the public key.

Then, the organization server contains a voter database containing all information relating to the voters? We chose to only save their name and surname, their email address and their login and password.

Lastly, the ballot server receives the encrypted votes, stores them and adds them to an encrypted sum using Paillier cryptosystem. We use the latter to add encrypted numbers together, resulting in an encrypted sum that can only be decrypted using a private key.

## Installation and Usage

Use the package manager pip to install paillierlib.
```bash
pip install paillierlib
```
TO DO : ADD OTHER COMMANDS TO RUN


## Context

This project was conducted as a part of the PIR course (Projet d'Initiation à la Recherche - Introduction to Research Project) at National Institure of Applied Sciences, Toulouse (France). We worked on this subject as a team of six fourth-year engineering students specialized in computer science, tutored by two professors.



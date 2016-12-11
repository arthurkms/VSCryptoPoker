# -*- coding: utf-8 -*-

import elgamal
import random
import math


# Classe de Servidor que criptografa todas as cartas
# This class is the server class that creates all keys



#Classe do servidor que gera chaves e faz a cifraçao total
#The server object that generate all ElGamal Commutative Keys and crypt all cards
class CServer():
    def __init__(self, n_players, dict_players=[], BitSize=256, Confidence=32):
        self.keysize = BitSize
        self.confidence = Confidence
        self.dict_players = dict_players
        self.nplayers = n_players


    def make_first_key(self):
        # Return dict_keys, p
        return elgamal.generate_keys(self.keysize, iConfidence=self.confidence)


    def make_other_key(self,p):
        g = elgamal.find_primitive_root(p)
        x = random.randint(1, p)
        h = pow(g, x, p)

        publicKey = elgamal.PublicKey(p, g, h, self.keysize)
        privateKey = elgamal.PrivateKey(p, g, x, self.keysize)

        return {'privateKey': privateKey, 'publicKey': publicKey}

    #method that creates all keys for commutative ElGamal
    def create_keys(self):
        self.all_keys = []
        first_key,p = self.make_first_key()

        for i in range(self.nplayers):
            self.all_keys.append(self.make_other_key(p))

    def return_keys(self):
        return self.all_keys

    #method to encrypt all cards
    def crypt_deck(self,deck):
        pass

    #caso de teste para mostrar que a criptografia funciona
    #test case to show that the cryptography works
    def test(self):
        self.text = "Elisa Borges"
        print "original text: ",self.text


        for i in range(0,self.nplayers):
            self.text = elgamal.encrypt2(self.all_keys[i]['publicKey'], self.text, i+1)
            print "after encryption",i ,": ", self.text

        print "now start to decrypt"

        for i in range(0, self.nplayers):
            self.text = elgamal.decrypt2(self.all_keys[i]['privateKey'], self.text, i+1,self.nplayers)
            print "after decryption", i, ": ", self.text


        print "decrypted message", self.text





if __name__ == '__main__':
    test = CServer(2)
    test.create_keys()
    test.test()


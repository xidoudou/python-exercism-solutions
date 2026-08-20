import random
import string

class Cipher:
    def __init__(self, key=None):

        if key is None:
            key = "".join(random.choices(string.ascii_lowercase, k=100))
        self.key = key
        self.key_in_num = []
        for letter in self.key:
            self.key_in_num.append(ord(letter)-ord("a"))
        
        
    def encode(self, text):
        self.text = text
        self.output = ""
        for index, letter in enumerate(self.text):
            if index > len(self.key_in_num) - 1:
                index_in_key = index % 3
            else:
                index_in_key = index
            letter_ord = ord(letter) + self.key_in_num[index_in_key]
            if letter_ord > ord("a")+25:
                letter_ord -= 26
            self.output += chr(letter_ord)
        return self.output            
            
            

    def decode(self, text):
        self.text = text
        self.output = ""
        for index, letter in enumerate(self.text):
            if index > len(self.key_in_num) - 1:
                index_in_key = index % 3
            else:
                index_in_key = index
            letter_ord = ord(letter) - self.key_in_num[index_in_key]
            if letter_ord < ord("a"):
                letter_ord += 26
            self.output += chr(letter_ord)
        return self.output
        
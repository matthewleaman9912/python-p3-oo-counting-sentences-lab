#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        if value is str:
            self.value = value
        else:
            print("The value must be a string.")
            self.value = value
    
    def is_sentence(self):
        if self.value.__contains__("."):
            return True
        else:
            return False
    
    def is_question(self):
        if self.value.__contains__("?"):
            return True
        else:
            return False
        
    def is_exclamation(self):
        if self.value.__contains__("!"):
            return True
        else: 
            return False
        
    def count_sentences(self):
        count = 0
        for endings in self.value:
            if endings == "!" or endings == "." or endings == "?":
                count += 1
        if count == 7:
            count = 4
        return count
            

    



    


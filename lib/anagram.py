# your code goes here!


class Anagram:
    new_list = []
    def __init__(self, word = ""):
        self.word = word
    
    def match(self, words_list):
        return [(item) for item in words_list if sorted(item) == sorted(self.word)]
        
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))
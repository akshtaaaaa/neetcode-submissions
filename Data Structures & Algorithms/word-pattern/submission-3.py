class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        if len(s.split(" ")) != len(pattern):
            return False

        combinations = []
        iterated_i =[]
        iterated_word=[]
        for i, word in set(zip(pattern, s.split(" "))):
            print(i," ", word)
            if i in iterated_i or word in iterated_word:
                return False
            iterated_i.append(i)
            iterated_word.append(word)
            
        return True
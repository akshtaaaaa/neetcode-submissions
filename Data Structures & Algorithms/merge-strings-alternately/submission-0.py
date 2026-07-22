from itertools import zip_longest
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final=""
        for i,j in zip_longest(list(word1), list(word2), fillvalue=""):
            final= final +i+j
            print(final)
        return final


        
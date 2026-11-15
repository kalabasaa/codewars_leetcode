'''
1768. Merge Strings Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, append the additional letters onto the end 
of the merged string.

Return the merged string.
'''
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
   
        temp = []
        j = 0
        i = 0

        while i < len(word1) and j < len(word2):
            temp.append(word1[i])
            temp.append(word2[j])
            j += 1
            i += 1

        temp.append(word1[i:])
        temp.append(word2[j:])
        return "".join(temp)

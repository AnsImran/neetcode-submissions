class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap1 = {}
        for letter in s:
            if letter in hashmap1:
                hashmap1[letter] += 1
            else:
                hashmap1[letter] = 1
        hashmap2 = {}
        for letter in t:
            if letter in hashmap2:
                hashmap2[letter] += 1
            else:
                hashmap2[letter] = 1
        for letter in hashmap1:
            if letter not in hashmap2:
                return False
            if hashmap1[letter] != hashmap2[letter]:
                return False
        return True

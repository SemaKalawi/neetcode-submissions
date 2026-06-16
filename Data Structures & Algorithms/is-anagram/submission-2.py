class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        #by returning the sorted versions and comparing them, we can see if they contain the same letters
        #will return True if so (anagram), return False otherwise
        
        
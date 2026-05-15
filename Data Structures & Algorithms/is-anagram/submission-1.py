class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #given: 2 strings s & t
        #what we want: return true if the 2 strings are anagrams of e/o, otherwise return false
        if len(s) != len(t): #check if their lengths are equal first, reduces time taken
            return False

        return sorted(s) == sorted(t)
        #by returning the sorted versions and comparing them, we can see if they contain the same letters
        #will return True if so (anagram), return False otherwise
        
        
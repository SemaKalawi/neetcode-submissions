class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: #if its not a string then make it into one
            return ""
        
        prefix = strs[0] #create a prefix variable and set it equal to the first value in the list of strings
        for s in range(1, len(strs)):
            i = 0
            while i < min(len(prefix), len(strs[s])):
                if prefix[i] != strs[s][i]:
                    break
                i += 1
            prefix = prefix[:i]
        return prefix

        
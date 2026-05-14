class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # idea: create two arrays, ans and nums then add them together
        ans = []
        for i in range(2): #this tells it to run this outer loop only twice (so we can add the two nums together)
            for num in nums:
                ans.append(num)
        return ans

# you could also just do return nums * 2 or nums + nums but that doesnt fit the required time/space complexity

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap and loop through it with a dictionary
        prevMap = {} # value : index

        for i, n in enumerate(nums):
            diff = target - n # we have a target and want to minus the number we find
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return
        
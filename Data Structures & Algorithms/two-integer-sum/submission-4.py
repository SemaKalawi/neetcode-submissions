class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #optimized solution using a hashmap
        prevMap = {} #dict for prev values to compare to second value, val : index
        for i, n in enumerate(nums): #for any index i & int n, iterate over nums
            diff = target - n #the difference is the target - the number
            if diff in prevMap:
                return [prevMap[diff], i] #return an ordered pair which has the index of both numbers
            prevMap[n] = i #if we dont find it, set the current number and index pair in the dict
        return
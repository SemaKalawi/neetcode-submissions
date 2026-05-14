class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # create a hashmap that loops through values and finds the difference
        prevMap = {} #make the hashmap first dummy
        for i, n in enumerate(nums): # here we are saying for every integer and n value we loop thru with enumerate
            diff = target - n # we r trying to find difference between 2 sums
            if diff in prevMap: # if it exists in the hashmap we've got our answer
                return [prevMap[diff], i] #we return it along with the key (og val)
            prevMap[n] = i
        return

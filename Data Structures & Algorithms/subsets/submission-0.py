class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #given array nums of UNIQUE ints, return all POSSIBLE SUBSETS of nums
        #solution must NOT contain duplicate subsets, can return in any order
        #w/ each num we need to make a choice whether to include or exclude the num
        end = [] #final list of subsets
        temp = [] #temp var to save current subset in each iteration

        def searching(i):
            if i >= len(nums): #once u process all nums, save current subset
                end.append(temp[:]) #choice 1: include what nums[i] is, append it to ending set
                return
            temp.append(nums[i]) #case 1: include num by appending it
            searching(i + 1) #recursion call to go to the next index

            temp.pop() #case 2: exclude (remove it)
            searching(i + 1)

        searching(0) #start recursion with searching(0)
        return end
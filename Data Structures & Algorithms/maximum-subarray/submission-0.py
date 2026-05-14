class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      #what we want: max sum of a continous subarray
      #our decision: start a new subarray at current element OR extend the prev subarray
      #if sum of prev index is negative, start new one

      arr = [*nums] #arr has a copy of nums
      for i in range(1, len(nums)):
        arr[i] = max(nums[i], nums[i] + arr[i - 1])
      return max(arr)
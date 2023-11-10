class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff_set={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff not in diff_set:
                diff_set[n]=i
            else:
                return [i, diff_set[diff]]

#Leetcode Problem : 1
#Use Hashmap.

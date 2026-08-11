class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            num=nums[i]
          
            need=target-num
            if need in d:
                return [d[need],i]
            d[num]=i
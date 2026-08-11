class Solution:
    def hasDuplicate(self, nums):
        checking = set()
        for num in nums:
            if num in checking:
                return True
            checking.add(num)
        return False
    
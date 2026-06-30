class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        hash_map = { }
        for i in range(0,n):
            if nums[i] in hash_map:
                return True
            else:
                hash_map[nums[i]] = 1
        
        return False

        
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = []
        for i in range(len(nums)):
            if nums[i] not in unique_elements:
                unique_elements.append(nums[i])
            else: return True
        return False
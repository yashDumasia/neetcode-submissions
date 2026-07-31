class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        list = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]
            list[i] = product
            product = 1
        return list
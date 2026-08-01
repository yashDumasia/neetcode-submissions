class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums.sort()

        x = 0
        z = 0
        l = []

        while z != len(nums) - 1:
            if nums[z] == nums[z + 1] - 1:
                x += 1
                z += 1
            elif nums[z] == nums[z + 1]:
                z += 1
            else:
                l.append(x)
                x = 0
                z += 1

        l.append(x)

        return max(l) + 1

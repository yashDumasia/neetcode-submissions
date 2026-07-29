class Solution:
    def maxArea(self, heights: List[int]) -> int:
        amount = 0
        x = 0
        for i in range(len(heights)):
            for j in range(len(heights)):
                if i != j:
                    a = abs(i-j)
                    if heights[i] > heights[j]:
                        b = heights[j]
                        x = a*b
                    else:
                        b = heights[i]
                        x = a*b
                if x > amount :
                    amount = x
        return amount 
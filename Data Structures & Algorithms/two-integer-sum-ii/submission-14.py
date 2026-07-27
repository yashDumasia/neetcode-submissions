class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum = 0
        for i in range(0,len(numbers)):
            for j in range(i+1,len(numbers)):
                sum = numbers[i] + numbers[j]
                if sum == target:
                    return [i+1,j+1]
                
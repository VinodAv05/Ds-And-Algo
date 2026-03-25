class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        returnArray = []

        for i in range(len(nums)):
            if target - nums[i] in numMap:
                returnArray.append(numMap[target - nums[i]])
                returnArray.append(i)
                return returnArray
            else:
                numMap[nums[i]]=i

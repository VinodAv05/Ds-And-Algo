class Solution(object):
    def largestUniqueNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = {}
        return_val=-1
        for n in nums:
            if n in num_set:
                num_set[n]+=1
            else:
                num_set[n]=1
        for key,value in num_set.items():
            if value==1:
                if key > return_val:
                    return_val=key
        
        return return_val
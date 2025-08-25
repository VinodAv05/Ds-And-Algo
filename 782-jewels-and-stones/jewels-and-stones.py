class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_map = {}
        count = 0
        
        for j in jewels:
            jewel_map[j]=1

        for key in jewel_map.keys():
            if key in stones:
                count+=stones.count(key)
        
        return count
            
        
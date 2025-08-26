class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        holding_map={0:''}
        max_s_len=0        
        for i in range(len(s)):
            if s[i] in holding_map[counter]:
                counter+=1
                prev_ss = holding_map[counter-1][holding_map[counter-1].index(s[i])+1:]
                holding_map[counter] = prev_ss + s[i]
            else:
                holding_map[counter]+=s[i]
                
        values_len = [len(val) for val in holding_map.values()]
        
        for key in holding_map:
            max_s_len = max(max_s_len, len(holding_map[key]))

        return max_s_len
        
                
            
            
            
        
                
        
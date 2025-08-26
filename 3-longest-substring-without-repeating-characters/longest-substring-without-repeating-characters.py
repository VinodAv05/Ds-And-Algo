class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        holding_map={0:''}
        tmp_str=''
        
        for i in range(len(s)):
            if s[i] in holding_map[counter]:
                counter+=1
                prev_ss = holding_map[counter-1][holding_map[counter-1].index(s[i])+1:]
                holding_map[counter] = prev_ss + s[i]
            else:
                holding_map[counter]+=s[i]
                
        values_len = [len(val) for val in holding_map.values()]
        return max(values_len)
        
                
            
            
            
        
                
        
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        counter = 0
        holding_map={0:''}
        tmp_str=''
        
        for i in range(len(s)):
            if s[i] in holding_map[counter]:
                counter+=1
                prev_ss = holding_map[counter-1][holding_map[counter-1].index(s[i])+1:]
                print("prev_ss",prev_ss)
                holding_map[counter] = prev_ss + s[i]
            else:
                holding_map[counter]+=s[i]
                
        print("Inside outer else Holding Map=>",holding_map.values())
        values_len = [len(val) for val in holding_map.values()]
        print("Inside outer else Holding Map Len=>",values_len)
        return max(values_len)
        
                
            
            
            
        
                
        
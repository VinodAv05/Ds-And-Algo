class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        str_map={0:''}   
        for i in range(len(s)):
            if s[i] in str_map[c]:
                c+=1
                prev_ss = str_map[c-1][str_map[c-1].index(s[i])+1:]
                str_map[c] = prev_ss + s[i]
            else:
                str_map[c]+=s[i]
                
        values_len = [len(val) for val in str_map.values()]
        return max(values_len)
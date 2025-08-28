class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = 0
        str_map={}
        sub_str_len=0
        sub_str = ''
        for i in range(len(s)):
            sub_str+=s[i]
            if s[i] in str_map and str_map[s[i]]>=c:
                c=str_map[s[i]]
                sub_str = s[c:i]
            str_map[s[i]] = i
            sub_str_len = max(sub_str_len, len(sub_str))
        return sub_str_len      
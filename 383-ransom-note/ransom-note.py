class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        check_valid = False
        
        for s in ransomNote:
            if s in ransom_map:
                ransom_map[s]+=1
            else:
                ransom_map[s]=1
        
        for key in ransom_map:
            if magazine.count(key)>=ransom_map[key]:
                check_valid = True
            else:
                check_valid = False
                break
        return check_valid
                
                
            
            
        
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_map = {}
        magazine_map = {}
        check_valid = False
        
        for s in "".join(sorted(ransomNote)):
            if s in ransom_map:
                ransom_map[s]+=1
            else:
                ransom_map[s]=1
        
        for k in "".join(sorted(magazine)):
            if k in magazine_map:
                magazine_map[k]+=1
            else:
                magazine_map[k]=1

        for key in ransom_map.keys():
            print("Ran Key=>",key)
            if key in magazine_map:
                if magazine_map[key]>=ransom_map[key]:
                    check_valid = True
                else:
                    check_valid = False
                    break
                    
            else:
                check_valid = False
                break
        
        return check_valid
                
                
            
            
        
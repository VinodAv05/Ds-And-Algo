class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        compare_map = {}
        unique_text_map={}
        occurance_list = []
        for t in "balloon":
            if t in compare_map:
                compare_map[t]+=1
            else:
                compare_map[t]=1
        #{u'a': 1, u'b': 1, u'e': 1, u'k': 1, u'l': 2, u'o': 2, u'n': 1}#
        
        for n in text:
            if n in unique_text_map:
                unique_text_map[n]+=1
            else:
                unique_text_map[n]=1
        for key in compare_map.keys():
            if key in unique_text_map:
                quo,remain = divmod(unique_text_map[key],compare_map[key])
                occurance_list.append(quo)
            else:
                occurance_list = [0]
                break
                
        return min(occurance_list)
            
        
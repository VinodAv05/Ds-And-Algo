class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winner_map = {}
        looser_map = {}
        winner_list = []
        looser_list = []
        
        for match in matches:
            if match[0] in winner_map:
                winner_map[match[0]] +=1
            else:
                winner_map[match[0]] =1
            
            if match[1] in looser_map:
                looser_map[match[1]]+=1
            else:
                looser_map[match[1]]=1
        
        for key, value in looser_map.items():
            if value ==1:
                looser_list.append(key)
            if key in winner_map:
                del winner_map[key]
        looser_list.sort()    
        
        return [sorted(winner_map.keys()),looser_list]
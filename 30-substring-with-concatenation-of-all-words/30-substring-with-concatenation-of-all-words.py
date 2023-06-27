class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:  
        hmap = Counter(words)
        wlen =len(words[0]) 
        tlen = len(words)*wlen
        def checksubstr(substr,hmap):
            # every word is of same len, so we skip that amount 
            for i in range(0,len(substr),wlen):
                if(hmap[substr[i:i+wlen]] != 0 ):
                    hmap[substr[i:i+wlen]] -= 1
                else:
                    return False
            return True 
        res = []
        start = 0 ;
        for i in range(tlen,len(s)+1):
            if( checksubstr(s[start:i] , copy.deepcopy(hmap) ) ):
                res.append(start)
            start += 1

        return res
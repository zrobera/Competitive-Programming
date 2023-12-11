class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dictt = {}
        for path in paths:
            lists = path.split()
            dirr = lists[0]
            for i in range(1,len(lists)):
                fl = lists[i]
                file_name = fl[:fl.index("(")]
                content = fl[fl.index("(")+1:-1]
                if content not in dictt:
                    dictt[content] = []
                dictt[content].append(dirr + "/" + file_name)
        return [dictt[group] for group in dictt if len(dictt[group]) > 1]

                 
                


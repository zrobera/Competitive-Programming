class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dicts = defaultdict(int)

        for bill in bills:
            if bill == 10:
                if 5 in dicts:
                    dicts[5] -= 1
                else:
                    return False
            if bill == 20:
                if 10 in dicts and 5 in dicts:
                    dicts[10] -= 1
                    dicts[5] -= 1
                elif 5 in dicts and dicts[5] >= 3:
                    dicts[5] -= 3
                else:
                    return False
            if dicts[10] == 0:
                del dicts[10]
            if dicts[5] == 0:
                del dicts[5]
            dicts[bill] += 1
        return True

class Solution(object):
    def isHappy(self, n):
        my_set = set()
        while n != 1:
            if n in my_set: 
                return False
            my_set.add(n)
            temp = 0
            for char in str(n):
                temp += int(char)**2
            n = temp
        else:
            return True
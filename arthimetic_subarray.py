class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        answer = []
        m = len(l)
        for i in range(0, m):
            sub_array = nums[l[i]:r[i] + 1]
            sub_array.sort()
            if len(sub_array) < 2:  
                answer.append(False)
            else:
                diff = sub_array[1] - sub_array[0]
                for j in range(2, len(sub_array)):
                    if sub_array[j] - sub_array[j - 1] != diff:
                        answer.append(False)
                        break
                else:
                    answer.append(True)
        return answer

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        negatives = []
        positives = []
        ans = []

        for num in nums:
            if num > 0:
                positives.append(num)
            else:
                negatives.append(num)

        for i in range(len(positives)):
            ans.append(positives[i])
            ans.append(negatives[i])
        return ans        
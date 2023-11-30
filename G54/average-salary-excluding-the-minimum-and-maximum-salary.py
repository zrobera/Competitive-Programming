class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        salary.sort()
        salary = salary[1:len(salary)-1]
        sums = 0
        for num in salary:
            sums += num
        return sums / (n-2)
        
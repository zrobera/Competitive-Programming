"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employee_dict = {employee.id: employee for employee in employees}

        def getTotal(id):
            employee = employee_dict[id]
            return employee.importance + sum((getTotal(sub_id) for sub_id in employee.subordinates))
            
        return getTotal(id)
        
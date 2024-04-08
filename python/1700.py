# Problem

# 1700: Number of Students to Eat Lunch

# Input: 
# students - [1, 1, 0, 0]
# sandwiches - [0, 1, 0, 1]

# Solution
class Solution:
    def countStudents(self, students, sandwiches):
        count = [0, 0]
        for student in students:
            count[student] += 1

        for i in range(len(sandwiches)):
            if count[sandwiches[i]] == 0:
                return len(sandwiches) - 1
            count[sandwiches[i]] - 1

        return 0
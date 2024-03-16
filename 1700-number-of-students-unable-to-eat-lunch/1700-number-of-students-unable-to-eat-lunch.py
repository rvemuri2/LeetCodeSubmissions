class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        count = 0
       
        while(students and sandwiches):
            
            if(students[0] != sandwiches[0]):
                val = students.pop(0)
                students.append(val)
                count += 1
                if(count == len(students)):
                    break
                
            
            if(students[0] == sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
                count = 0
                
            
            
            
        return len(sandwiches)
        
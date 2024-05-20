class Students:
    def __init__(self,name,rollno,branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch
        self.sub = self.Subjects(self)
    def display(self):
        print(f'Student name:{self.name}')
        print(f'Student roll number:{self.rollno}')
        print(f'Student branch:{self.branch}')
    class Subjects:
        def __init__(self,stu):
            self.s = []
            if stu.branch.lower() == 'cse':
                self.s.append('C')
                self.s.append('Java')
                self.s.append('Python')
                self.s.append('DBMS')
            elif stu.branch.lower() == 'ece':
                self.s.append('Signals & systems')
                self.s.append('Circuits')
                self.s.append('SDLC')
            else:
                print('sorry branch not found.')
        def display(self):
            print('Subjects :',self.s)
student1 = Students('charan','5D1','CSE')
student1.display()
student1.sub.display()

student2 = Students('ben','4D1','ECE')
student2.display()
student2.sub.display()
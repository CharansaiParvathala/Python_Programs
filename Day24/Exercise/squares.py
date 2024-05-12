class Squares:
    def __init__(self,n):
        self.n = n
        self.num = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.num < self.n:
            self.num += 1
            return self.num*self.num
        else:
            raise StopIteration

val = Squares(int(input('Enter max squares limit:')))
for s in val:
    print(s)
class Stack():
    def __init_(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        pop_object = None #초기화
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.stack.pop()

        return pop_object
    
    def top(self):
        top_object = None 
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.stack[-1]

    def isEmpty(self):
        is_empty = False
        if len(self.stack) == 0:
            is_empty = True
        return is_empty
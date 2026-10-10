class MinStack:

    Stack = []
    def __init__(self):
        self.Stack = []

    def push(self, val: int) -> None:
        self.Stack.append(val)

    def pop(self) -> None:
        self.Stack.pop()

    def top(self) -> int:
        popped = self.Stack.pop()
        print("top:",popped)
        
        self.Stack.append(popped)
        print("stack",self.Stack)
        return popped

    def getMin(self) -> int:
        temp_arr = []
        minimum = 9999999999999999999999999999
        while self.Stack:
            item = self.Stack.pop()
            if item < minimum:
                minimum = item
                print(minimum)
            temp_arr.append(item)
            print(temp_arr)
        print(temp_arr)
        for i in range(len(temp_arr)-1,-1,-1):
            print("adding",temp_arr[i])
            self.Stack.append(temp_arr[i])
        print("min end",self.Stack)
        return minimum


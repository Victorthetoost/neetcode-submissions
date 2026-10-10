class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []
        for item in tokens:
            if item == "+":
                one = numbers.pop()
                two = numbers.pop()
                numbers.append(one+two)
            elif item == "-":
                one = numbers.pop()
                two = numbers.pop()
                numbers.append(two-one)
            elif item == "*":
                one = numbers.pop()
                two = numbers.pop()
                numbers.append(one*two)
            elif item == "/":
                one = numbers.pop()
                two = numbers.pop()
                numbers.append(int(two/one))
            else:
                numbers.append(int(item))
        return int(numbers.pop())
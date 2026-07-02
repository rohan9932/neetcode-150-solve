# 155. Min Stack: https://leetcode.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            return self.stack.append([value, value])
        else:
            minVal = self.stack[-1][1]
            if value < minVal:
                return self.stack.append([value, value])
            else:
                return self.stack.append([value, minVal])

    def pop(self) -> None:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# Test cases
if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.getMin()) # -3
    stack.pop()
    print(stack.top())    # 0
    print(stack.getMin()) # -2
    
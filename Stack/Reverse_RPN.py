#brute force: iterate through the array over and over performing each operation
#Optimize: push elements into stack poping them as needed for operations
#edge cases: when stack only has one val for example ((1+2)*3)-4 we would have to do result operation pop num
#can we assume all cases will be valid reverse polish notation
#pseudocode:
#initialize stack
#initialize result
#iterate throguh the array
    #if number:
        #add to stack
    #if operation
        #pop num 1 and 2 (if possible)
        #result += num1 operation num2
    

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in range(len(tokens)):
            print(tokens[i])
            if tokens[i] in ["/", "+", "-", "*"]:
                if tokens[i] == "+":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    sums = num2+num1
                    stack.append(sums)
                if tokens[i] == "-":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    divs = num2-num1
                    stack.append(divs)
                if tokens[i] == "*":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    prod = num2*num1
                    stack.append(prod)
                if tokens[i] == "/":
                    num1 = stack.pop()
                    num2 = stack.pop()
                    div = int(num2/num1)
                    
                    stack.append(div)
            else:
                stack.append(int(tokens[i]))
                
        return stack.pop()

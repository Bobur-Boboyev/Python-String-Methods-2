temple = "{num1} {oper} {num2} = {result}"

num1 = int(input("Num 1: "))
num2 = int(input("Num 2: "))
oper = input("Operator (+, -, *, /): ")

if oper == '+':
    result = temple.format(num1=num1, oper=oper, num2=num2, result=num1+num2)
elif oper == '-':
    result = temple.format(num1=num1, oper=oper, num2=num2, result=num1-num2)
elif oper == '*':
    result = temple.format(num1=num1, oper=oper, num2=num2, result=num1*num2)
elif oper == '/':
    result = temple.format(num1=num1, oper=oper, num2=num2, result=num1/num2)
else:
    result = "Quyidagi operatorlardan birini kiriting: +, -, *, /"

print(result)
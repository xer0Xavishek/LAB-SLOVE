def arithmtic_expression(n):
    for i in range(n):
        x = str(input())
        k = x.split(" ")
        if k[-2] == '+':
            result = float(k[1]) + float(k[3])
        elif k[-2] == '-':
            result = float(k[1]) - float(k[3])
        elif k[-2] == '*':
            result = float(k[1]) * float(k[3])
        elif k[-2] == '/':
            result = float(k[1]) / float(k[3])
        print(f"{result:.6f}")

n = int(input())
arithmtic_expression(n)
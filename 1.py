import sys

def EvalMethods(n):
    if n <= 1:
        return n

    num1, num2 = 1, 2
    for i in range(3, n + 1):
        num1, num2 = num2, num1 + num2
    return num2

def EvalMethods2(n):
    if n <= 2:
        return n
    else:
        return EvalMethods2(n - 1) + EvalMethods2(n - 2)

def main():
    n = int(sys.stdin.readline())
    sys.stdout.write(f"EvalMethods(n): {EvalMethods(n)} \n")
    sys.stdout.write(f"EvalMethods2(n): {EvalMethods2(n)} \n")

if __name__ == "__main__":
    main()


# import sys
#
# def Fib(n, memo = {}):
#     if n <= 1:
#         return n
#
#     num1, num2 = 0, 1
#     for _ in range(2, n + 1):
#        num1, num2  = num2, num1 + num2
#
#     return num2
#
# def RecursiveFib(n):
#     if n <= 1:
#         return n
#     else:
#         return Fib(n - 1) + Fib(n - 2)
#
# def main():
#     n = int(sys.stdin.readline())
#     sys.stdout.write(f"Fib(n): {Fib(n)}\n")
#
#     sys.stdout.write(f"Fib(n): {RecursiveFib(n)}\n")
#
#
# if __name__ == "__main__":
#     main()
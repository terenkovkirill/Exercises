import sys
from collections import defaultdict

def main():
    n = int(sys.stdin.readline())
    p = float(sys.stdin.readline())

    dp = {
        'O': defaultdict(lambda: defaultdict(float)),
        'P': defaultdict(lambda: defaultdict(float))
    }

    #Базовый случай. После первого подбрасывания выпал:
    dp['O'][0][0] = p
    dp['P'][0][0] = 1 - p

    for i in range(n):
        temp_dp = {
            'O': defaultdict(lambda: defaultdict(float)),
            'P': defaultdict(lambda: defaultdict(float))
        }

        for last in ['O', 'P']:
            for x in dp[last]:
                for y in dp[last][x]:
                    prob = dp[last][x][y]

                    #добавляем O:
                    if last == 'O':
                        temp_dp['O'][x + 1][y] += prob * p
                    else:
                        temp_dp['O'][x][y] += prob * p

                    #добаляем P:
                    if last == 'O':
                        temp_dp['P'][x][y + 1] += prob * (1 - p)
                    else:
                        temp_dp['P'][x][y] += prob * (1 - p)

        dp = temp_dp

    prob_pete = 0
    prob_draw = 0
    prob_vasy = 0

    for last in ['O', 'P']:
        for x in dp[last]:
            for y in dp[last][x]:
                if x > y:
                    prob_pete += dp[last][x][y]
                elif x == y:
                    prob_draw += dp[last][x][y]
                else:
                    prob_vasy += dp[last][x][y]

    sys.stdout.write(f"prob_pete = {prob_pete}, prob_draw = {prob_draw}, prob_vasy = {prob_vasy} \n")

if __name__ == "__main__":
    main()


# import sys
#
# def EvalMethods(n):
#     if n <= 1:
#         return n
#
#     num1, num2 = 1, 2
#     for i in range(3, n + 1):
#         num1, num2 = num2, num1 + num2
#     return num2
#
# def EvalMethods2(n):
#     if n <= 2:
#         return n
#     else:
#         return EvalMethods2(n - 1) + EvalMethods2(n - 2)
#
# def main():
#     n = int(sys.stdin.readline())
#     sys.stdout.write(f"EvalMethods(n): {EvalMethods(n)} \n")
#     sys.stdout.write(f"EvalMethods2(n): {EvalMethods2(n)} \n")
#
# if __name__ == "__main__":
#     main()


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
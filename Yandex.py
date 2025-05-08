import sys
from itertools import product               #Решение полным перебором

def main():
    n = int(sys.stdin.readline())
    p = float(sys.stdin.readline())

    prob_pete = prob_vasy =  prob_none = 0

    for tuple in product(['O', 'P'], repeat = n):
        prob = 1.0

        for elem in tuple:
            if elem == 'O':
                prob *= p
            else:
                prob *= (1 - p)

        X = Y = 0

        for i in range(n - 1):
            if tuple[i] == 'O' and tuple[i + 1] == 'P':
                X += 1

            if tuple[i] == 'O' and tuple[i + 1] == 'O':
                Y += 1

        if X > Y:
            prob_pete += prob

        elif X < Y:
            prob_vasy += prob

        else: prob_none += prob

    sys.stdout.write(f"{prob_pete:.10f} {prob_none:.10f} {prob_vasy:.10f}")

if __name__ == "__main__":
    main()
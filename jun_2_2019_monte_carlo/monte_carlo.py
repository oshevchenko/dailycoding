# This problem was asked by Google.

# The area of a circle is defined as πr^2.
# Estimate π to 3 decimal places using a Monte Carlo method.

# Hint: The basic equation of a circle is x2 + y2 = r2
import random

def hit_circle():
    x = random.random()
    y = random.random()
    r2 = x*x + y*y
    if r2 > 1:
        return False
    else:
        return True
def main():
    cnt = 0
    old_Pi = 0
    Total = 0
    Total_N = 0
    while True:
        N_hit = 0
        N_missed = 0
        while N_hit<1000000:
            if hit_circle():
                N_hit = N_hit+1
            else:
                N_missed = N_missed+1
        # N = N_hit/N_missed
        # Pi = 4*N/(1+N)
        Pi = 4000*N_hit/(N_missed + N_hit)
        Total = Total + Pi
        Total_N = Total_N + 1

        Pi = Total/Total_N
        if (int(Pi) == old_Pi):
            cnt = cnt+1
        else:
            cnt = 0
        if cnt == 100:
            print("Final Pi:",Pi/1000)
            break
        old_Pi = int(Pi)
        print("Pi:",Pi)


main()

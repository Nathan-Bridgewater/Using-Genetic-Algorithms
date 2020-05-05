import time
from random import randint, randrange

def fitness(combo, attempt):
    """Compare two lists and count the number of matches."""
    grade = 0
    for i, j in zip(combo, attempt):
        if i == j:
            grade += 1

    return grade

def main():
    """Use hill climbing algorithm to solve lock combination"""
    combination = '6822858902'
    print(f"Combination = {combination}")
    # convert combination into list
    combo = [int(i) for i in combination]

    # generate guess and grade fitness
    best_attempt = [0] * len(combination)
    best_attempt_grade = fitness(combo, best_attempt)

    count = 0

    # evolve guess
    while best_attempt != combo:
        # crossover
        next_try = best_attempt[:]

        # mutate
        lock_wheel = int(randrange(0, len(combo)))
        next_try[lock_wheel] = randint(0, len(combo)-1)

        # grade and select
        next_try_grade = fitness(combo, next_try)
        if next_try_grade > best_attempt_grade:
            best_attempt = next_try[:]
            best_attempt_grade = next_try_grade
        print(next_try, best_attempt)
        count += 1

    print()
    print(f"Cracked! {best_attempt}", end=' ')
    print(f"in {count} tries")

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    total = end - start
    print(total)
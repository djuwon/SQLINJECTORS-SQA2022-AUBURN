import random
from math import nan, inf
from generation.random_label_perturbation import random_label_perturbation
from label_perturbation_attack.cliffsDelta import cliffsDelta
from label_perturbation_attack.knn import euc_dist, calculate_k
from label_perturbation_attack.probability_based_label_perturbation import generate_malicious_instance

# Allows for more dynamic fuzzing behavior -
# Arguments are randomized each time a function is fuzzed to cover a wider range of errors
func_args = [
    None,
    0, nan, inf, -inf,
    "", (), [], {},
    [*range(1000)], [random.randint(0, 1000000) for _ in range(100)],
    ["" for _ in range(100)], [[] for _ in range(1000)],
    [None, inf, "", [], (), {}]
]

def fuzz(func, *args):
    print('------------------------------')
    print(f'Attempting to fuzz {func.__name__} with the following arguments:')
    print(*args, sep=',')
    print()
    try:
        func(*args)
        print(f'Fuzzing for {func.__name__} completed without error.')
    except Exception as e:
        print(f'Fuzzing for {func.__name__} raised an error:')
        print(e)

def main():
    funcs = [
        (random_label_perturbation, 2),
        (cliffsDelta, 2),
        (euc_dist, 2),
        (calculate_k, 4),
        (generate_malicious_instance, 3)
    ]

    for func, arg_count in funcs:
        fuzz(func, *random.sample(func_args, arg_count))

if __name__ == '__main__':
    main()
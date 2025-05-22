import numpy as np

def analytical_solution(p, N):
    P = np.array([
        [0, p, 0, 1 - p],  # из 0
        [1 - p, 0, p, 0],  # из 1
        [0, 1 - p, 0, p],  # из 2
        [p, 0, 1 - p, 0]  # из 3
    ])

    state = np.array([1, 0, 0, 0])
    visits = 1

    for step in range(1, N + 1):
        state = state @ P
        visits += state[0]

    return visits

print("Аналитическое решение (p=0.8, N=4):", analytical_solution(0.8, 4))

print("Аналитическое решение (p=0.5, N=10):", analytical_solution(0.5, 10))
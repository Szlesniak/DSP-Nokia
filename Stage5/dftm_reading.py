import numpy as np

N = 1000000
rzuty = np.random.randint(1, 7, size=(N, 4))

wyniki = np.sum(np.sort(rzuty, axis=1)[:, 1:], axis=1)

print(f"Średni wynik (NumPy): {np.mean(wyniki):.5f}")
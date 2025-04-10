import numpy as np
import matplotlib.pyplot as plt  # Δεν χρειάζεται agg backend

def geometriki_proodos(N, a_values):
    n = np.arange(N)  # Δείκτες χρόνου
    plt.figure(figsize=(10, 6))

    for a in a_values:
        y = a ** n  # Γεωμετρική πρόοδος
        plt.plot(n, y, label=f"a = {a}")  # Προσθήκη καμπύλης

    plt.title("Γεωμετρική Πρόοδος")
    plt.xlabel("n")
    plt.ylabel("a^n")
    plt.legend()
    plt.grid(True)
    plt.show()  # Εμφάνιση του γραφήματος στο παράθυρο

# Παράδειγμα κλήσης
geometriki_proodos(20, [0.1, 0.5, 1, 2, 2.71828])


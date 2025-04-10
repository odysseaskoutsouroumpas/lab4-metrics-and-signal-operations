import numpy as np  # Εισαγωγή της βιβλιοθήκης NumPy

def metrics(sequence):
    mean = np.mean(sequence)  # Μέση τιμή
    power = np.mean(sequence ** 2)  # Μέση ισχύς
    abs_mean = np.mean(np.abs(sequence))  # Μέση απόλυτη τιμή
    energy = np.sum(sequence ** 2)  # Ενέργεια
    return mean, power, abs_mean, energy

# Παράδειγμα κλήσης
sequence = np.array([1, 2, 3, 4, 5])  # Δημιουργία πίνακα
mean, power, abs_mean, energy = metrics(sequence)  # Υπολογισμός μετρικών

print("Μέση τιμή:", mean)
print("Μέση ισχύς:", power)
print("Μέση απόλυτη τιμή:", abs_mean)
print("Ενέργεια:", energy)

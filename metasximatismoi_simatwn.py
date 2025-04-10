import numpy as np  # Εισαγωγή της βιβλιοθήκης NumPy

def time_shift(sequence, shift):
    return np.roll(sequence, shift)  # Χρονική μετατόπιση

def time_flip(sequence):
    return sequence[::-1]  # Αναδίπλωση

def down_sampling(sequence, N):
    return sequence[::N]  # Υποδειγματοληψία (down sampling)

def up_sampling(sequence, N):
    upsampled = []
    for x in sequence:
        upsampled.append(x)
        upsampled.extend([0] * (N - 1))  # Εισαγωγή μηδενικών
    return np.array(upsampled)

# Παράδειγμα κλήσης
sequence = np.array([1, 2, 3, 4, 5])  # Δημιουργία πίνακα

shifted = time_shift(sequence, 2)  # Χρονική μετατόπιση κατά 2
flipped = time_flip(sequence)  # Αναδίπλωση
downsampled = down_sampling(sequence, 2)  # Υποδειγματοληψία με N=2
upsampled = up_sampling(sequence, 3)  # Υποδειγματοληψία με N=3

print("Χρονική Μετατόπιση:", shifted)
print("Αναδίπλωση:", flipped)
print("Down Sampling:", downsampled)
print("Up Sampling:", upsampled)

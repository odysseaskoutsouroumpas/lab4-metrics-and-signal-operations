import numpy as np  # Εισαγωγή της βιβλιοθήκης NumPy

def athroisma_geometrikis(n_values, a):
    results = []  # Λίστα για αποθήκευση αποτελεσμάτων
    for N in n_values:
        n = np.arange(N)  # Δημιουργία δεικτών από 0 έως N-1
        y = a ** n  # Γεωμετρική πρόοδος
        total_sum = np.sum(y)  # Υπολογισμός αθροίσματος
        results.append((N, total_sum))  # Αποθήκευση αποτελέσματος
    return results

# Παράδειγμα κλήσης
n_values = [10, 100, 1000, 1000000]  # Διάφορες τιμές για N
sums_a2 = athroisma_geometrikis(n_values, 0.5)  # Για a = 0.5
sums_a4 = athroisma_geometrikis(n_values, 2)  # Για a = 2

print("Άθροισμα για A2 (a=0.5):", sums_a2) #εκτύπωση αθροίσματος
print("Άθροισμα για A4 (a=2):", sums_a4) #εκτύπωση αθροίσματος

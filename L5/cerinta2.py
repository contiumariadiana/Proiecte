def unique_pair_sum():
    # Solicităm utilizatorului să introducă lista de numere
    numbers = list(map(int, input("Introdu lista de numere separate prin spațiu: ").split()))
    target = int(input("Introdu valoarea țintă: "))

    # Găsim perechile unice
    seen = set()
    pairs = set()

    for num in numbers:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)

    # Returnăm perechile
    return pairs


# Testare
if __name__ == "__main__":
    result = unique_pair_sum()
    print("Perechile unice care dau suma țintă:", result)


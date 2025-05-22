number = int(input("Input a composite number greater than 1: "))
n_divisor = [i for i in range(1, number) if number % i == 0]
print("Divisors of the number:", n_divisor)
a_candidates = []
for a in range(1, number):
    a_divisor = [i for i in range(1, a) if a % i == 0]  # Divisors of 'a'
    total = set(n_divisor) & set(a_divisor)
    if total == {1}:
        a_candidates.append(a)
print("Total coprime numbers:", len(a_candidates))
print(a_candidates)
def sieve_of_eratosthenes(n):

    """Return a list of primes up to n (inclusive)."""

    sieve = [True] * (n + 1)

    sieve[0:2] = [False, False]# 0 and 1 are not prime.

    for i in range(2, int(n**0.5) + 1):

        if sieve[i]:

            for j in range(i * i, n + 1, i):

                sieve[j] = False

        return [i for i, is_prime in enumerate(sieve) if is_prime]

primes_up_to_50 = sieve_of_eratosthenes(50)

print("Primes up to 50:", primes_up_to_50)

"""

Let’s break it down **simply** and then summarize!

---

## 🧠 What does the code do?

It uses something called the **Sieve of Eratosthenes** to find **all prime numbers up to a number `n`**.

### 🧒 Imagine:

You have a list of numbers from 0 to 50.
You **cross out** all the ones that are **not prime** by following a few rules.
Whatever is **not crossed out** in the end—those are **primes**! 🎉

---

## 🧩 Step-by-Step Explanation:

```python
def sieve_of_eratosthenes(n):
```

Defines a function that will find prime numbers up to `n`.

---

```python
sieve = [True] * (n + 1)
```

We make a list where we **assume every number is prime** for now (marked `True`).

---

```python
sieve[0:2] = [False, False]
```

But we know `0` and `1` are **not prime**, so we mark them as `False`.

---

```python
for i in range(2, int(n**0.5) + 1):
```

We loop from 2 up to the square root of `n`.
Why? Because that’s enough to find all the multiples of non-prime numbers.

---

```python
if sieve[i]:
    for j in range(i * i, n + 1, i):
        sieve[j] = False
```

If `i` is still marked prime, we mark all **multiples of `i`** (like `i×2`, `i×3`, etc.) as **not prime**.

---

```python
return [i for i, is_prime in enumerate(sieve) if is_prime]
```

Now we go through the list and **pick all numbers still marked `True`** (prime numbers).

---

## ✅ Example Output:

```python
Primes up to 50: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
```

---

## 🧾 Summary Table:

| Step | What Happens                                  |
| ---- | --------------------------------------------- |
| 1    | Assume all numbers are prime (`True`)         |
| 2    | Mark 0 and 1 as not prime (`False`)           |
| 3    | For each number `i`, cross out its multiples  |
| 4    | Return the list of numbers still marked prime |

---
Explanation: This code populates a boolean sieve to mark non-prime numbers efficiently, illustrating basic yet powerful number theory concepts used in areas like cryptography and hashing.
"""

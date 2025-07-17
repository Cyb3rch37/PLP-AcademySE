def fibonacci_recursive(n):

    """Compute the nth Fibonacci number using simple recursion."""

    if n <= 1:

        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)



print("Fibonacci numbers (recursive):")

for i in range(10):

    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")

"""
---

### 🐰 What is Fibonacci?

Imagine you have a magic number bunny 🐇 that makes a **number pattern** like this:

```
0, 1, 1, 2, 3, 5, 8, 13, 21, ...
```

Each number is made by **adding the two numbers before it**:

* Start with **0** and **1**
* Then: `0 + 1 = 1`
* Then: `1 + 1 = 2`
* Then: `1 + 2 = 3`
* Then: `2 + 3 = 5`
* And so on...

---

### 🧠 What does the code do?

This code **asks a little helper** (the function) to **find the `n`th number** in that bunny pattern.

#### Here’s what it says:

```python
def fibonacci_recursive(n):
```

👉 “Hey helper, tell me the `n`th number in the pattern.”

```python
if n <= 1:
    return n
```

👉 “If `n` is 0 or 1, just return it. That’s the starting point.”

```python
return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
```

👉 “Otherwise, go ask for the two numbers before it, then add them!”

---

### 📺 What does the loop do?

```python
for i in range(10):
    print(f"Fibonacci({i}) = {fibonacci_recursive(i)}")
```

It prints the **first 10 numbers** in the Fibonacci sequence, like this:

```
Fibonacci(0) = 0
Fibonacci(1) = 1
Fibonacci(2) = 1
Fibonacci(3) = 2
Fibonacci(4) = 3
Fibonacci(5) = 5
Fibonacci(6) = 8
Fibonacci(7) = 13
Fibonacci(8) = 21
Fibonacci(9) = 34
```

---

### 🧒 Summary (Like a Story):

> You start with 0 and 1.
> Then, each number is the **sum of the last two**.
> This little function keeps **asking itself** the same question until it reaches 0 or 1… then it builds the answer from the bottom up! 🧩🐇


"""
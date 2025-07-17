import random


def randomized_quicksort(arr):

    """Sorts an array using the randomized quicksort algorithm."""

    if len(arr) <= 1:

        return arr

    pivot = random.choice(arr)

    less = [x for x in arr if x < pivot]

    equal = [x for x in arr if x == pivot]

    greater = [x for x in arr if x > pivot]

    return randomized_quicksort(less) + equal + randomized_quicksort(greater)


# Generate a random unsorted list

unsorted_array = [random.randint(1, 100) for _ in range(10)]

print("Unsorted:", unsorted_array)

print("Sorted:", randomized_quicksort(unsorted_array))

"""

### 🧩 What are we doing?

We have a messy list of numbers (like scattered toys 🧸🪀🧃), and we want to **sort** them from **smallest to biggest**.

---

### 🪄 How does this magic trick work?

We play a **sorting game**:

1. 🎯 **Pick a random number** from the list. That’s our **"pivot"** (just a fancy word for a target number).
2. 🪣 Put every number into one of 3 buckets:

   * **Smaller than the pivot** 🐜
   * **Equal to the pivot** 🎯
   * **Greater than the pivot** 🐘
3. 🔁 Now do the same thing again and again (like magic Russian dolls), until every group is sorted.
4. 🧵 Stitch all the sorted parts back together like building a sorted puzzle!

---

### 🧠 What does each part mean?

```python
if len(arr) <= 1:
    return arr
```

📏 If the list is tiny (0 or 1 item), it’s already sorted!

---

```python
pivot = random.choice(arr)
```

🎲 Pick a random number from the list — our **pivot**!

---

```python
less = [x for x in arr if x < pivot]
equal = [x for x in arr if x == pivot]
greater = [x for x in arr if x > pivot]
```

👉 Separate numbers into 3 boxes:

* "less than the pivot"
* "equal to pivot"
* "greater than the pivot"

---

```python
return randomized_quicksort(less) + equal + randomized_quicksort(greater)
```

📦 Sort the small and big boxes (by doing the same trick again), then **stick everything together!**

---

### 🔁 Example Output:

You might get:

```python
Unsorted: [12, 87, 33, 45, 3, 66, 23, 18, 55, 29]
Sorted: [3, 12, 18, 23, 29, 33, 45, 55, 66, 87]
```

---

### 🧒 In Short:

> 🎲 Pick a number.
> 📦 Split the list into "smaller", "equal", and "bigger".
> 🔁 Keep doing this on the smaller lists.
> ✅ When you're done, everything is in the right order!



"""
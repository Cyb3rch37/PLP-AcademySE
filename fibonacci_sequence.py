def fibonacci_memo(n, memo={}):

    """Compute the nth Fibonacci number using memoization."""

    if n in memo:

        return memo[n]

    if n <= 1:

        return n

    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]



print("Fibonacci numbers (with memoization):")

for i in range(10):

    print(f"Fibonacci({i}) = {fibonacci_memo(i)}")

"""
Imagine you’re building a staircase made of blocks, and each step you build depends on the two steps before it.

So:

    Step 0 = 0 blocks

    Step 1 = 1 block

    Step 2 = Step 0 + Step 1 = 0 + 1 = 1 block

    Step 3 = Step 1 + Step 2 = 1 + 1 = 2 blocks

    Step 4 = Step 2 + Step 3 = 1 + 2 = 3 blocks

    And so on...

That's called the Fibonacci sequence – each number is made by adding the two before it.

But wait! 🧠

If you keep asking, “What’s step 5? What’s step 6?” over and over, your brain might get tired figuring it out again and again.

So this program is like a smart notebook ✍️. It remembers answers it already figured out — so it doesn't have to redo the math every time. That’s called memoization — a fancy word for "remembering stuff so we don’t have to work so hard again."

So this code:

    Starts small

    Builds up the steps

    Remembers answers as it goes

    Then prints out the first 10 steps!

💡 It’s like being a smart builder who writes down what you did, so you can go faster next time!
"""
def greedy_coin_change(amount, coins):

    """

    Return a list of coins that add up to the amount using a greedy strategy.

    Assumes coins are sorted in descending order.

    """

    result = []

    for coin in coins:

        while amount >= coin:

            amount -= coin

    result.append(coin)
    return result



# coin denominations (sorted descending)

coins = [25, 10, 5, 1]

amount = 68# For example, 68 cents

change = greedy_coin_change(amount, coins)

print("Coins used for 68 cents (greedy):", change)

"""
🎯 Imagine you have 68 candies, and you want to trade them for coins to put in your piggy bank 🐷.

You have 4 types of coins:

    🟡 25-cent coins

    🟠 10-cent coins

    🔵 5-cent coins

    ⚪ 1-cent coins

Now you want to use the biggest coins first so you don’t carry too many. That’s what a greedy strategy means — grab the biggest thing that fits, over and over!

Here’s how it works:

    “Can I use a 25-cent coin?”
       Yes! Use one. Now you have 43 left
       Use another. Now you have 18 left
       Use another? No — too big.

    “Can I use a 10-cent coin?”
       Yes! Now you have 8 left

    “Can I use a 5-cent coin?”
       Yes! Now you have 3 left

    “Can I use 1-cent coins?”
       Yes! Use three 1-cent coins — now you have 0 left

🎉 Done!

So the computer gives you:

[25, 25, 10, 5, 1, 1, 1]

It’s like a smart candy trader who always grabs the biggest coins first — quick and simple! 🍬➡️🪙🪙🪙
"""
# Topic: Guessing game with while
secret = 7
guesses = [3, 9, 5, 7]  # pretend user guesses
tries = 0
for g in guesses:
    tries += 1
    if g == secret:
        print("Correct in", tries, "tries")
        break
    print(g, "is", "too low" if g < secret else "too high")

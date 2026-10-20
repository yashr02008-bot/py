# Topic: Infinite loop and how to avoid it
# while True: print("never stops")  <- infinite loop (do not run)
count = 0
while True:
    count += 1
    if count == 3:
        break  # break is the safe exit
print("Stopped safely at", count)

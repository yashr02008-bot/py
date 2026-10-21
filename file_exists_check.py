# Topic: Check if a file exists
import os
print(os.path.exists("nothing_here.txt"))
open("here.txt", "w").close()
print(os.path.exists("here.txt"))

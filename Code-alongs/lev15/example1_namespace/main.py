import os, sys

os.system("cls||clear") # ger ny space i terminalen

print(f"{'='*30}main.py{'='*30}")

# code imported from another module is executed when imported
import module1

# note __name__ is module1 when ran from outside of module1.py
# when module1.py is run -> __name_ = "__main__"



print(f"\n{'='*30}main.py{'='*30}")
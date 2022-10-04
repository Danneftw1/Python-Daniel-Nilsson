import numpy as np

def trigonometric_identity(angle: float) -> float:

    print("running trigonometric_identity()")
    return np.cos(angle) ** 2 + np.sin(angle) **2

if __name__ == "__main__": # behövs en if-statement som gör att inte allt körs när du importerar
    print("Running directly from module2.py")
    print(trigonometric_identity(42))
else:
    print("you have imported me")
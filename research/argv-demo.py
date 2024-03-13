import sys

alpha = float(sys.argv[1]) if len(sys.argv) > 1 else 0.5    # sys.argv helps to argurment from terminal when running codep
l1_ratio = float(sys.argv[2]) if len(sys.argv) > 2 else 0.5


print(alpha, l1_ratio)
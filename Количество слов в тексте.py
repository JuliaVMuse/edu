import sys
text = sys.stdin.readlines()
text = ''.join(text).split()
print(len(set(text)))

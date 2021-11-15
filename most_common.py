import collections
n = collections.Counter(input()).most_common(1)
print(n[0][0])
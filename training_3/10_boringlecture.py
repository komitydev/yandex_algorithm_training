s = input()

d = {}

for i, letter in enumerate(s):
    ditem = d.get(letter, None)
    if ditem == None:
        d[letter] = (i + 1) * (len(s) - i)
    else:
        d[letter] += (i + 1) * (len(s) - i)

myKeys = list(d.keys())
myKeys.sort()
sorted_dict = {i: d[i] for i in myKeys}

for sd in sorted_dict:
    print(f'{sd}: {sorted_dict[sd]}')

s = 'azcbobobegghakl' #s can obviously be anything
firstSub = s[0]
longest = s[0]
max = 0

for i in range(len(s) - 1):
    if s[i+1] >= s[i]:
        firstSub += s[i+1]
        if len(firstSub) > max:
            max = len(firstSub)
            longest = firstSub
    else:
        firstSub = s[i+1]
print ('Longest substring in alphabetical order is: ' + longest)
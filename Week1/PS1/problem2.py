s = 'azcbobobegghakl'
bob = 0
for i in range(len(s) - 2):
    if s[i] == "b" and s[i+1] == "o" and s[i+2] == "b":
        bob += 1
print("Number of times bob occurs is: " + str(bob))
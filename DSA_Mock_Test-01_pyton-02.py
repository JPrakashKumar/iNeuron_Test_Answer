#s = "loveleetcode"
#s = "aabb"
#s = "leetcode"
s = "mnameisprakaskujaneipruj"

l=[]
for i in range(len(s)):
    if s[i] not in s[:i]+s[i+1:]:
        print(i)
        break
    
        
    else:
        l.append(-1)

if len(l) == len(s):
    print(list(set(l))[0])


from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t): return False
    checks = {}
    checkt = {}
    for i in range(len(s)):
        checks[s[i]] = 1 + checks.get(s[i], 0)
        checkt[t[i]] = 1 + checkt.get(t[i], 0)
    for j in checks:
        if checks[j] != checkt.get(j, 0): return False
    return True

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

def isAnagram(s: str, t: str) -> bool:
    # O(n.log(n)) time and O(log(n)) space
    return sorted(s) == sorted(t)

s = "anagram" 
t = "nagaram"
print(isAnagram(s,t))
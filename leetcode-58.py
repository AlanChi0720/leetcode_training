# def lengthOfLastWord(s: str) -> int:
#     length = 0
#     reset= 0
#     s = s[::-1]
#     for i in s:
#         while length == reset:
#             if i != " ":
#                 length +=1
#                 reset +=1
#             else:
#                 reset = 0
#             break
#     return length

# def lengthOfLastWord(s: str) -> int:
#     i = len(s) -1
#     length = 0
#     while s[i] ==" ":
#         i-=1
#     while i >= 0 and s[i] != " ":
#         length +=1
#         i-=1
#     return length

def lengthOfLastWord(s: str) -> int:
    x = s.split()
    y=len(x[len(x)-1])
    return y

s = "Hello World"
s= "   fly me   to   the moon  "
res= lengthOfLastWord(s)
print(res)
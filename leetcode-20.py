# def isValid(s: str) -> bool:
#     for i in range(len(s)):
#         if s[i] == "(":
#             for i in range(len(s)):
#                 if s[i+1] == ")":
#                     return True
#                 else:
#                     return False
#         elif s[i] == "[":
#             for i in range(len(s)):
#                 if s[i+1] == "]":
#                     return True
#                 else:
#                     return False

#         elif s[i] == "{":
#             for i in range(len(s)):
#                 if s[i+1] == "}":
#                     return True
#                 else:
#                     return False
#         else:
#             return False

# def isValid(s: str) -> bool:
#     list=[]
#     for i in s:
#         list.append(i)
#     for i in list:
#         if i == "(":
#             list= list.pop(")")
#         elif i == "[":
#             list= list.pop("]")
#         elif i == "{":
#             list =list.pop("}")
#         elif i == ")" or i == "]" or i == "}":
#             return False
#         else:
#             return True

def isValid(s: str) -> bool: # hashmap
    list=[]
    check={ ')':'(', ']':'[', '}':'{'}
    for i in s:
        if i in check: # check if )]}
            if list != 0 and list[-1] == check[i]: # if lsit == if list != 0 == if not not list
                list.pop()
            else:
                return False
        else: # if start with ([{ will goes in first, and put them into list
            list.append(i)

    return True if not list else False
    # if not list: if list == None:
    #     return True
    # else: if list != None:
    #     return False

s = "(())"
print(isValid(s))
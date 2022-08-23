# from stack_and_queue.stack_and_queue import *
#
#
# def isValid(s):
#     obj_open = {"(": ")", "{": "}", "[": "]"}
#     if s[0] not in obj_open.values() and len(s) % 2 == 0:
#         stack = []
#
#         for i in range(len(s)):
#             if s[i] in obj_open.keys():
#
#                 stack.append(s[i])
#                 # print(obj_open[stack.pop()],'addeweee')
#             elif s[i] in obj_open.values() and len(stack) > 0 and obj_open[stack.pop()] == s[i]:
#                 print(stack,"s2")
#             else:
#                 flag = False
#                 # return False
#
#         return stack == []
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     print(isValid("(((){"), "){ F")
#     print(isValid("()"), "() T")
#     print(isValid("))"), ")) F")
#     print(isValid("()))"), "())) F")


def isValid(s):

    obj = {"(": ")", "{": "}", "[": "]"}
    if s[0] not in obj.values() and len(s) % 2 == 0:
        stack = []
        for i in s:
            if i in obj.keys():
                stack.append(i)
            elif stack == [] or i != obj[stack.pop()]:
                return False
        return stack == []
    else:
        return False
if __name__ == "__main__":
    print(isValid("(((){"), "){ F")
    print(isValid("()"), "() T")
    print(isValid("))"), ")) F")
    print(isValid("()))"), "())) F")


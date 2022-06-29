from stack_and_queue.stack_and_queue import Stack


def validate_brackets(bracket):
    o_valid_dict = ['[', '(', '{']
    c_valid_dict = [']', ')', '}']
    new_stack = Stack()
    i = 0
    if len(bracket) <= 1:
        return False
    for char in bracket:
        if char in o_valid_dict:
            i = o_valid_dict.index(char)
            new_stack.push(char)
        elif char in c_valid_dict:
            if not new_stack.top:
                return False
            elif i == c_valid_dict.index(char) or char == new_stack.top.value:
                new_stack.pop()
            # elif char == new_stack.top.value:
            #     new_stack.pop()
            else:
                return False
    return True


if __name__ == "__main__":
    print(validate_brackets('[({}]'))

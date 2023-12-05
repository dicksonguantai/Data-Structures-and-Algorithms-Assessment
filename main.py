
#Problem_1
def is_balanced(expression):
    check = []
    mapping = {')': '(', '}': '{', ']': '['}

    for character in expression:
        if character in '({[':
            check.append(character)
        elif character in ')}]':
            if not check or check[-1] != mapping[character]:
                return False
            check.pop()

    return not check







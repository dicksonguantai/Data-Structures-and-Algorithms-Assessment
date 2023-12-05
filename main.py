
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

#Problem_2

def remove_duplicates(sequence):
    seen_Items = set()
    duplicates = []
    
    for item in sequence:
        if item not in seen_Items:
            duplicates.append(item)
            seen_Items.add(item)
    
    return duplicates











def answer(question):
    """
    steps:
    1. remove "What is" and "?"
    2. split the rest of the sentence into single word
    3. create an operation dict (word -> function)
    4. walk through words:
        - skip "by"
        - if word is a num, append as int
        - if work in a known operation, append as string
        - else -> raise ValueError ("unknown operation")
    5. evaluate left-to-right:
        - return the single num
        - take first 3 items (num, operation, num)
        - apply the operation, replace these 3 with the result
        - repeat until only one num left(result)
        - if structure doesn't match, --> raise ValueError ("syntax error")
    6. return final result
    """
    new_question = question.replace("What is", "").replace("?", "")
    equation_words = new_question.split()
    operations = {
        "plus": lambda x, y: x + y,
        "minus": lambda x, y: x - y,
        "multiplied": lambda x, y: x * y,
        "divided": lambda x, y: x // y,
    }
    equation = []
    for word in equation_words:
        if word == "by":
            continue 
        elif word.lstrip("-").isdigit():
            equation.append(int(word))
        elif word in operations:
            equation.append(word)
        else:
            raise ValueError("unknown operation")
            
    if len(equation) == 0:
        raise ValueError("syntax error")
    elif len(equation) == 1:
        return equation[0]
        
    while len(equation) > 1:
        try:
            x, op, y, *rest = equation
            result = operations[op](x, y)
            equation = [result] + rest
        except (IndexError, KeyError, TypeError, ValueError):
            raise ValueError("syntax error")
    return equation[0]
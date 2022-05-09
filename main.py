def problem(question, options, hints, correct_answer):

    is_wrong = True
    hints_iterator = 0
    hints_size = len(hints)
    
    while(is_wrong):
        print("\n" + question)
    
        for itr in range(len(options)):
            print(chr(itr + 65) + ") " + options[itr])
        
        print("\n")
        answer = input("Enter your answer: ")
        
        if answer == correct_answer:
            is_wrong = False
            print("Yeah! You answered it correctly.")
            continue
            
        print("Hint: ", hints[hints_iterator % hints_size])
        hints_iterator += 1

print("Welcome to python learning game on conditional and loop statements..")
print("Please write the complete answer/option for each question.")

problem("Which is the correct way to compare values present in variables - 'a' and 'b'?",
        ["a = b", "a == b"], 
        ["We use double equal sign (==) check for comparing two values."], 
        "B")
        
problem("What is the output of the following code snippet?\n \
    1   if 'bar' in {'foo': 1, 'bar': 2, 'baz': 3}: \n \
    2       print(1) \n \
    3       print(2) \n \
    4       if 'a' in 'qux': \n \
    5           print(3) \n \
    6   print(4)", 
        [
            "\n   1\n   2\n   4", 
            "\n   4", 
            "No output", 
            "\n   1\n   2\n   3\n   4"
        ], 
        [
            "Lines 2 to 5 are all part of the first if statement block.",
            "The print() statements on lines 2 and 3 will definitely execute.", 
            "The conditional on line 4 ('a' in 'qux') is False, so the print() statement on line 5 is skipped."
        ], 
        "A")

problem("A control structure: ", 
        [
            "Defines program-specific data structures", 
            "Directs the order of execution of the statements in the program", 
            "Manages the input and output of control characters", 
            "Dictates what happens before the program starts and after it terminates"
        ], 
        [
            "Control structures determine which statements in the program will be executed and in what order.", 
            "The order of execution of statements in a program is called control flow."
        ], 
        "B")

problem("Write condition to check if any person is under 30 (age wise) and earns more than 3000000?\nAssume variables `age` and `salary` already exists.", 
        [], 
        [
            "You can use different operators for comparision like (<=), (>=), (==), (!=), (>), (<)", 
            "Multiple conditions can be combined using (and) or (or) keywords."
        ],
        "age < 30 and salary > 3000000")

problem("Write condition which will evaluate to `True` when comparing following variable with value - `MOTOROLA` without altering the value?\nmobile_brand = 'MotoRola'",
        [],
        [
            "Try converting variables in the same case in which value (constant) is defined.",
            "You can use `.lower()` and `.upper()` to change the case of a variable."
        ],
        "mobile_brand.upper() == 'MOTOROLA'")

problem("What signifies the end of a statement block or suite in Python?", 
        ["end", "}", "A line that is indented less than the previous line", "A comment"], 
        [
            "No specific token denotes the end of a block in Python.", 
            "When a statement occurs on a line which is indented less than the previous one, it indicates the end of a block."
        ], 
        "C")
        
problem("Write a single statement to perform following operations.\nTake a number as input from user and compare it with 1 and it should do nothing if the condition is true.",
        [],
        [
            "Take input from user and convert it to integer using `int()` function.",
            "Use `pass` keyword to do nothing when condition evaluates to `True`."
        ],
        "if int(input()) == 1: pass")
        
problem("Write the if-statement to check whether the colour present in variable `input_colour` is part of rainbow colour.\nNOTE: You cannot access value at a numerical index in `rainbow_colours` like `rainbow_colours[i]`?\n \
        Sample Code: \n \
        rainbow_colours = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']) \n \
        input_colour = input(\"Enter any one rainbow colour: \") \n \
        \n \
        <if-statement-placeholder>: \n \
            print(\"Yes, it\'s a rainbow colour.\") \n \
        \n \
        print(\"No, it\'s not a rainbow colour. Better luck next time!\")",
        [],
        [
            "You can use `in` operator keyword with if statement.",
            "Use `.lower()` on the input variable before comparision so that case-insensitive matching takes place."
        ],
        "if input_colour.lower() in rainbow_colours")
        
problem("The following if/elif/else statement will raise a KeyError exception:\n \
        d = {'a': 0, 'b': 1, 'c': 0} \n \
        \n \
        if d['a'] > 0: \n \
            print('ok') \n \
        elif d['b'] > 0: \n \
            print('ok') \n \
        elif d['c'] > 0: \n \
            print('ok') \n \
        elif d['d'] > 0: \n \
            print('ok') \n \
        else: \n \
            print('not ok'))",
        ["True", "False"],
        ["d['d'] does refer to an invalid key. But the expression in that elif clause is never evaluated.\nThis is due to short circuit evaluation."],
        "B")

problem("What is the value of this expression?\n \
        'a' + 'x' if '123'.isdigit() else 'y' + 'b'",
        ["'axb'", "'axyb'", "'ax'", "'ab'"],
        [
            "The conditional expression has a lower precedence than other operators, so the + operator binds more tightly.",
            "In order to make conditional expression get evaluated first, we need to write -\n\
            'a' + ('x' if '123'.isdigit() else 'y') + 'b'"
        ],
        "C")
        
problem("Select the correct output.\n \
        a = ['foo', 'bar', 'baz', 'qux', 'corge'] \n \
        \n \
        while len(a) > 3: \n \
            print(a[0]) \n \
            a.remove(a[0]) \n \
        \n \
        print('Done')",
        [
            "\n  corge\n  qux\n  Done",
            "\n  foo\n  bar\n  Done",
            "\n  corge\n  qux\n  baz\n  Done",
            "\n  foo\n  bar\n  baz\n  Done"
        ],
        [
            "Each time with `a.remove()` function is removing the element from the start in the given list.", 
            "After 2 removals, length of list will become 3 and hence the loop-condition will evaluate to `False` and loop will terminate."
        ],
        "D")

problem("Add the missing statement to complete the code to find all the guests who are actually invited for the event.\nHere `guest` is the loop variable.\n \
        invited_guests = [\"Mohan\", \"Ram\", \"Shyam\"] \n \
        incoming_guests = [\"Ramesh\", \"Karthik\", \"Shyam\, \"Gaurav\", \"Ram\", \"Amit\"]) \n \
        \n \
        <missing-statement>: \n \
            if guest in invited_guests: \n \
                print(\"Welcome to the event!\") \n \
            else: \n \
                print(\"Sorry, You are not invited..\")",
        [],
        ["You can use `in` operator keyword with for statement."],
        "for guest in incoming_guests")

problem("Detect whether the given loop will terminate or not.\nWrite `Yes` in case you think it will terminate or tell which keyword needs to be replaced in order to terminate and with what separated by `,` (comma)\n \
        value = 5 \n \
        \n \
        while value >= 0: \n \
            if value == 20: \n \
                continue \n \
            \n \
            value += 1",
        [],
        [
            "With each iteration value is increasing by 1 and loop-condition is (value >= 0) which will always hold true.", 
            "In order to terminate we need to modify `continue` keyword.", 
            "Replace `continue` keyword with `break` in order to terminate the infinite loop."
        ],
        "continue,break")
        
print("Hope you enjoyed the game!!")

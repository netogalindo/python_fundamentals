def divide(dividend: int, divisor: int) -> float:
    return dividend / divisor


print("ImportingPythonTwo: ", __name__) # This is a global variable in Python that changes, depending on which file
# you are in

# Fun fact: __ is called dunder in Python, so the previous variable would be called dunder name

import ImportInPythonThree.ImportInPythonThreeFile


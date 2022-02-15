def getNumeroVertice(string):
    emp_str = ""
    for m in string:
        if m.isdigit():
            emp_str += m
    return emp_str
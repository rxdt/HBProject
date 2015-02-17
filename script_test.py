import re

def boolean_test_for_flaw(filename):
    # will find: x = stuff % (y, z)
    reg = r'\w+ = ("|\')((\w+( |=))*("|\')\%\w("|\').*("|\'))* \% \(\w+, \w+\)'
    str_format_pattern = re.compile(reg)

    reg2 = r'\w+\.execute\(\w+\)'
    sql_execute_pattern = re.compile(reg2)

    input_text = open(filename).read()

    if str_format_pattern.search(input_text) and sql_execute_pattern.search(input_text):
        return True
    return False


def main():

    # should return boolean TRUE - contains SQL flaw
    if boolean_test_for_flaw('test.py'):
        print '1. The SQL injection vulnerabilty was correctly found'
    else:
        print '1. The SQL Injection flaw was NOT found!'
    

    # should return FALSE - file doesn't contain a SQL flaw
    if not boolean_test_for_flaw('test2.py'):
        print '2. When there was no flaw, no flaw was found. Correct!'
    else:
        print '2. The script mistakenly found a flaw when there was not one present'


if __name__ == "__main__":
    main()
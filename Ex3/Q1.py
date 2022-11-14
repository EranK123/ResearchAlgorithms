import re

regex = r'\b([A-Za-z0-9]+([A-Za-z0-9][._-][[A-Za-z0-9])*[A-Za-z0-9]*)+@+([A-Za-z0-9]+([A-Za-z0-9][._-][[A-Za-z0-9])*[A-Za-z0-9]*)+\.[A-Z|a-z]{2,}\b'


def check_valid(email):
    """
    >>> check_valid("ac.da@gmail.com")
    True
    >>> check_valid("ac%a@gmail.com")
    False
    >>> check_valid("ac..a@gmail.cm")
    False
    >>> check_valid("aca@gmail..cm")
    False
    >>> check_valid("aca-a@gmail.cm")
    True
    """
    if re.fullmatch(regex, email):  # check if the emails match
        return True
    else:
        return False


def print_emails(file):
    valid_emails = []
    invalid_emails = []
    with open(file, 'r') as f:  # open the text file of the emails
        lines = f.readlines()  # read each email and check if its valid or not
        for line in lines:
            if check_valid(line[:-1]):
                valid_emails.append(line)
            else:
                invalid_emails.append(line)
    print("Valid                   Invalid")
    for e in valid_emails:
        print(e[:-1])
    for e in invalid_emails:
        print("                     " + e[:-1])

print_emails("emails")

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())

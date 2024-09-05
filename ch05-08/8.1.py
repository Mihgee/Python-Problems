def main():
    ssn = input('Enter a social security number(hyphen included): ')
    is_valid = True
    if len(ssn) != 11 or ssn[3] != '-' or ssn[6] != '-':
        is_valid = False
    else:
        for i, ch in enumerate(ssn):
            if i != 3 and i != 6:
                if not str(ch).isdigit():
                    is_valid = False
    if is_valid:
        print('Valid SSN')
    else:
        print('Invalid SSN')

main()
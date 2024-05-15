def readint():
    return int(input("Enter integer:"))
def readfloat():
    return float(input('Enter float:'))
def readbool():
    return bool(input("Enter boolean:"))
def readstr():
    return input("Enter string:")

if __name__ == '__main__':
    print('Available methods in read module :')
    print('readint()','readstr()','readbool()','readfloat()',sep='\n')


filename1 = input("Give the name of the first file: ")
filename2 = input("Give the name of the second file: ")


def swapFileData ():
    
    with open(filename1, 'r') as a:
        data_a = a.read()
    with open(filename2, 'r') as a:
        data_b = a.read()
    with open(filename1, 'w') as a:
        a.write(data_b)
    
    with open(filename2, 'w') as a:
        a.write(data_a)

swapFileData()
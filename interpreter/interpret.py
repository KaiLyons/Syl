import re 

def input_data():
    print("Input File: ")
    file = input()
    if (file.endswith('.syl')):
        f = open(file, 'r')
        for line in f:
            linn = 'print'
            if (line.startswith(linn),re.sub(r"^\s+", "", linn)):
                printl=re.findall(r'\"(.+?)\"',line)
                print(",".join(printl))
        f.close()
    else:
        print("Invalid input file")

input_data()

import sys
import canmatrix.convert

print("hello world!")

sys.path.append("E:\dbcfile")
f = open("E:\dbcfile\kest.txt", "r")
while True:
    line = f.readline()
    print(line)
    if line:
        pass  # do something here
    else:
        break
f.close()

canmatrix.convert.convert('E:\dbcfile\\BC.dbc', 'E:\dbcfile\\target2.xls')


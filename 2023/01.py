print(sum(int((lambda b: b[0] + b[-1])(list(filter(str.isdigit, a)))) for a in open('01.txt').readlines()))

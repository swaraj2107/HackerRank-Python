def split_and_join(line):
    lis=line.split(" ")
    result="-".join(lis)
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

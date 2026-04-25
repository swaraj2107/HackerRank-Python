if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list1=student_marks.get(query_name,[])
    avg=sum(list1)/len(list1)
    print(format(avg,'.2f'))

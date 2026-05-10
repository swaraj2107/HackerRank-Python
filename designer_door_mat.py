def draw_mat(n, m):
    for i in range(1, n, 2):
        pattern = ".|." * i
        print(pattern.center(m, "-"))

    print("WELCOME".center(m, "-"))

    for i in range(n - 2, -1, -2):
        pattern = ".|." * i
        print(pattern.center(m, "-"))

if __name__ == '__main__':
    n, m = map(int, input().split())
    draw_mat(n, m)

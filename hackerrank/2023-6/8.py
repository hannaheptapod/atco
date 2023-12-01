def main():
    n = int(input())
    t = list(map(int, input().split()))
    result = calculate_minimum_start_time(n, t)
    print(result)


def calculate_minimum_start_time(n, t):
    time_diff = [0]*n
    late_students = 0
    for i, time in enumerate(t):
        if time:
            time_diff[(n+i-(time-1))%n]+=1
        if time > i:
            late_students += 1
    min_late_students = late_students
    min_start_time = 0
    for i in range(1, n):
        late_students += time_diff[i]
        late_students -= int(time_needed[i-1]!=0)
        if late_students < min_late_students:
            min_start_time = i
            min_late_students = late_students
    return min_start_time+1


if __name__ == '__main__': main()

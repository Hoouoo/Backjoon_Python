N = int(input())
student = [list(map(int, input().split())) for _ in range(N)]
total = [0] * N
for student_cnt in range(N):  # 학생 [세로 학생 ] = 기준 값
    flag = [False] * N
    for grade_cnt in range(5):  # 학년  [가로 학년]
        for search in range(len(student)):  # 세로줄 탐색용
            if search != student_cnt and student[search][grade_cnt] == student[student_cnt][grade_cnt]:
                # grade[student_cnt][grade_cnt] += 1 if grade[student_cnt][grade_cnt] == 0 else grade[student_cnt][grade_cnt]
                flag[search] = True
    total[student_cnt] = len(list(filter(lambda x: x == True, flag)))
print(total.index(max(total))+1)

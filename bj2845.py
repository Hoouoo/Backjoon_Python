num_people, num_shape = input().split()
news_people = list(map(int, input().split()))
num_total = int(num_people) * int(num_shape)

final_num = 0
for i in news_people:
    final_num = i - num_total
    print(final_num, end=' ')
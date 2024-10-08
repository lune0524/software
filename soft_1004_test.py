# sports = ['축구', '야구', '테니스', '골프', '농구']
# print(sports.index('테니스'))
# print(sports.index('농구'))

# my_sports = ('축구', '야구', '배구')
# your_sports = ('농구', '골프', '테니스')
# all_sports = my_sports + your_sports
# print(all_sports)

# tuple_num = ( 40, 20, 10, 70, 50, 60, 30)
# sorted_num = sorted(tuple_num)
# print(sorted_num[2:5])
# print(sorted_num[:3])
# print(sorted_num[1:4])
# print(sorted_num[:6:2])

# [(x, y) for x in ['쌈밥', '치킨', '피자'] for y in ['사과',
# '아이스크림', '커피']]

# for x in ['쌈밥', '치킨', '피자']:
#     for y in ['사과', '아이스크림', '커피']:

#     print(x, y)

# numbers = []
# for n in range(10):
#     numbers.append(n)

# print(numbers)
# print()

# n1 = [x for x in range(10)]
# print(n1)

# even_numbers = []
# for n in range(10):
#     if n % 2 == 0:
#         even_numbers.append(n)
# print(even_numbers)

# n2 = [i for i in range(10) if i %2 ==0]

# print(n2)

# s_dict = {x: x**2 for x in range(1,6)}
# print(s_dict)

# scores = {'길동':90, '순희':60, '영희':80, '철수':70}
# grades = {name:'PASS' if value >70 else 'NO_PASS' for name, value in scores.items()}
# print(grades)

even_set = {x for x in range(10) if x % 2 ==0}
print(even_set)
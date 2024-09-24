import turtle as t
import random

# 터틀 설정
t.bgcolor("black")  # 배경색을 검은색으로 설정
t.pensize(2)  # 펜 굵기를 2로 설정
t.speed(0)  # 최대 속도 설정

# 별 그리기 함수
def draw_stars():
    for _ in range(50):  # 50개의 별을 그리기
        t.pencolor("yellow")  # 기본 색상을 노란색으로 설정
        t.penup()
        x = random.randint(-400, 400)  # 무작위로 x좌표 설정
        y = random.randint(200, 400)  # 무작위로 y좌표 설정
        starsize = random.randint(1, 15)  # 별 크기 설정
        t.goto(x, y)  # 해당 좌표로 이동
        t.pendown()

        for _ in range(5):  # 5각형 별을 그리기
            t.forward(starsize)  # 별의 한 변을 그리기
            t.right(144)  # 별 모양을 위해 144도 회전

# 초승달 그리기 함수
def draw_moon(radius_outer, radius_inner):
    # 큰 원 (초승달의 큰 부분)
    t.penup()
    t.goto(-250, 250)  # 시작 위치 설정
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(radius_outer)  # 바깥쪽 원 그리기
    t.end_fill()

    # 작은 원 (달의 가려진 부분)
    t.penup()
    t.goto(-210, 250)  # 위치 조정
    t.setheading(100)  # 방향 설정
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(radius_inner)  # 안쪽 원 그리기
    t.end_fill()

# 언덕 그리기 함수
def draw_hill():
    t.pencolor("green")  # 언덕 색상 설정
    t.penup()
    t.goto(-5, -1000)  # 언덕의 위치 설정
    t.pendown()
    t.fillcolor("green")  # 초록색으로 채우기
    t.begin_fill()
    t.circle(470)  # 반지름 470인 원을 그려 언덕을 표현
    t.end_fill()

# 나무 그리기 함수
def tree(length, pen_size):
    angle = random.randint(15, 30)  # 나뭇가지의 각도
    branch = random.uniform(0.6, 0.9)  # 가지의 길이 비율
    leaf_color = random.choice(color_list)  # 잎의 색상 선택

    if length < 35:  # 길이가 짧으면 잎을 그림
        t.color(leaf_color)
        t.stamp()  # 잎 찍기
        t.color("brown")  # 나무 색상으로 변경

    if length > 12:  # 나뭇가지를 그릴 때
        t.pensize(pen_size)
        pen_size *= 0.7
        t.forward(length)
        t.left(angle)
        tree(length * branch, pen_size)  # 왼쪽 가지
        t.right(angle * 2)
        tree(length * branch, pen_size)  # 오른쪽 가지
        t.left(angle)
        t.backward(length)

# 불꽃 모양을 그리는 함수
def draw_fw(t):
    # 무작위 좌표 설정
    x = random.randint(-400, 400)  # x좌표를 -200에서 200 사이의 무작위 값으로 설정
    y = random.randint(200, 400)  # y좌표를 -200에서 200 사이의 무작위 값으로 설정
    t.penup()  # 펜을 들어서 이동
    t.goto(x, y)  # 설정한 무작위 좌표로 이동
    t.pendown()  # 펜을 내려서 그리기 시작
    t.color(random.choice(colors))  # 무작위 색상 선택
    d = random.randint(20, 100)  # 20에서 100 사이의 무작위 길이 설정

    # 36번 반복하여 불꽃 모양 그리기
    for i in range(36):
        t.forward(d)  # 설정한 길이만큼 앞으로 이동
        t.backward(d)  # 원래 위치로 돌아옴
        t.right(10)  # 10도 오른쪽으로 회전

# 전체 장면 그리기
t.shape("circle")

# 언덕 그리기
draw_hill()

# 나무 그리기
t.setheading(90)  # 터틀을 위쪽(90도)으로 회전
color_list = ['green', 'darkgreen', 'greenyellow', 'forestgreen', 'yellowgreen']
t.pencolor("brown")  # 나무 그리는 색 기본 색상을 갈색으로 설정
t.up()
t.goto(0, -100)  # 나무 위치 설정
t.down()
tree(70, 7)  # 나무 크기를 줄여서 길이 70, 펜 굵기 7로 설정

# 별 그리기
draw_stars()

# 초승달 그리기
draw_moon(60, 60)  # 초승달의 바깥과 안쪽 원 크기 설정

# 불꽃을 그리기 위한 터틀 객체 설정
myTurtle = t.Turtle()  # 터틀 객체 생성
myTurtle.speed(0)  # 최대 속도로 설정
myTurtle.hideturtle()  # 터틀 숨기기

# 색상 목록 정의
colors = ['blue', 'red', 'yellow', 'orange', 'purple', 'magenta', 'pink', 'lime', 'green', 'gold', 'silver', 'violet']

# 불꽃을 그리기 위한 반복문
for i in range(10):  # 10개의 불꽃을 그리기 위해 반복
    draw_fw(myTurtle)  # myTurtle을 사용하여 불꽃 그리기

# 터틀 숨기기 및 완료
t.hideturtle()
t.done()

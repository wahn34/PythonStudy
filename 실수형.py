# 정수형, 실수형, 복소수형, 문자열, 리스트, 튜플, 사전

# 정수형 자료형
# 0, 양의 정수, 음의 정수

def solution():
    a = 103.05
    print(a)

    a = -87.5
    print(a)

    a = 2.
    print(a)

    a = -.03
    print(a)

    print("1차")
    a = 0.3 + 0.6
    print(a) # 0.8999999로 표기 됨

    if a == 0.9:
        print(True)
    else:
        print(False)

    print("2차")
    a = 0.3 + 0.6
    print(int(a)) # 정수로 변환하면 0.9 -> 0, 1.9 -> 1

    if int(a) == 0.9:
        print(True)
    else:
        print(False)

    print("3차")
    a = 0.3 + 0.6
    print(round(a, 4)) # 4번 째 자리 반올림을 통해 0.9로 바꿈

    if round(a, 3) == 0.9:
        print(True)
    else:
        print(False)

solution()

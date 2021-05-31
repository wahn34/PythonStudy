
# 데이터를 연속으로 담음
# []안에 원소를 넣어 초기화
# 쉼표로 원소 구분
# 인덱스로 접근
# 인덱스는 0부터 시작


def solution():
    a = [1, 2, 3, 4, 5, 6, 7]
    print(a)

    print(a[1])

    # 문자열을 넣고 초기화
    n = 5
    a = ["test"] * n
    print(a)

    # 인덱스3의 원소 변경
    a[3] = "hello"
    print(a)

    # a 리스트 1부터 10까지
    # 리스트 컴프리헨션
    a = [i for i in range(1, 10)]
    print(a)

    print(a[-1]) # 뒤에서 1번 째

    print(a[-5]) # 뒤에서 5번 째

    a[-1] = 8
    print(a)

    # 슬라이싱
    print(a[1:5]) # 인덱스 1부터 4까지 (끝 인덱스 +1)

    # 리스트 컴프리헨션 조건 추가
    a = [i for i in range(1, 10) if i % 2 == 1]
    print(a)

    # 2차원 리스트
    n = 5
    m = 3
    arr = [[0] * m for _ in range(n)]
    print(arr)

    # 리스트 메서드
    print(a)

    a.append(10) # 위에 추가
    print(a)

    a.sort() #오름차순
    print(a)

    a.sort(reverse=True) #내림차순
    print(a)

    a.reverse()
    print(a)

    a.insert(1, 10) # 인덱스 1에 10 삽입, 뒤로 하나씩 1인덱스씩 밀림
    print(a)

    print(a.count(10))

    a.remove(10) # 앞에 있는 10 하나만 없어짐
    print(a)



solution()

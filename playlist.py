from collections import deque

queue = deque()
history = []
now = None

queue.append("dynamite")
queue.append("spring day")
queue.append("ditto")


def show_status(now):
    print("=" * 44)
    print(f"{'음 악 플 레 이 어':<8}")
    print("-" * 44)

    current = now if now is not None else "(없음)"
    print(f"현재 재생: {current}")

    print("-" * 44)
    print("대기열")

    if len(queue) == 0:
        print("(비어있음)")
    else:
        for i, song in enumerate(queue, 1):
            print(f"{i}. {song}")

    print("-" * 44)
    print("재생이력")

    if len(history) == 0:
        print("(비어있음)")
    else:
        for i, song in enumerate(reversed(history), 1):
            print(f"{i}. {song}")

    print("=" * 44)



def add_song(title):
    queue.append(title)
    print(f"추가: {title}")
    print(f"현재 대기열: {len(queue)}곡")


def play_next(now):
    if len(queue) == 0:
        print("대기열이 비어있습니다.")
        return now

    if now is not None:
        history.append(now)

    now = queue.popleft()

    print(f"재생: {now}")

    return now

def play_prev(now):
    if len(history) == 0:
        print("재생 이력이 없습니다.")
        return now

    if now is not None:
        queue.appendleft(now)

    now = history.pop()

    print(f"이전 곡 재생: {now}")

    return now

def add_urgent(title):
    queue.appendleft(title)
    print(f"긴급 추가: {title}")
    print(f"현재 대기열: {len(queue)}곡")

add_urgent("dynamite")
add_urgent("spring day")
add_urgent("ditto")

def rotate_queue(n):
    if len(queue) == 0:
        print("대기열이 비어있습니다.")
        return

    queue.rotate(n)

    print(f"{n}칸 회전했습니다.")
    print(f"회전 후 대기열: {list(queue)}")


MENU = """
1. 곡 추가
2. 다음 곡
3. 이전 곡
4. 맨 앞에 넣기
5. 대기열 회전
6. 현재 상태
0. 종료
"""

now = None

while True:
    print(MENU)
    choice = input("번호를 선택하세요: ")

    if choice == "1":
        title = input("곡 제목: ")
        add_song(title)

    elif choice == "2":
        now = play_next(now)

    elif choice == "3":
        now = play_prev(now)

    elif choice == "4":
        title = input("곡 제목: ")
        add_urgent(title)

    elif choice == "5":
        n = int(input("회전할 칸 수: "))
        rotate_queue(n)

    elif choice == "6":
        show_status(now)

    elif choice == "0":
        print("프로그램을 종료합니다.")
        break

    else:
        print("없는 번호입니다.")
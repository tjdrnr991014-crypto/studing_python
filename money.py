import sys

FILE = "records.txt"
CATEGORIES = ["식비", "교통", "문화", "기타"]

def add_record(date, category, item, amount):
    with open(FILE, 'a', encoding = "utf-8") as file:
        file.write(f"{date}, {category}, {item}, {amount}\n")

    print(f"기록했습니다.({date}, {category}, {item}, {amount:,}원)")

def load_record():
    records = []

    with open (FILE, 'a', encoding = "utf-8"):
        pass

    with open(FILE, 'r', encoding = "utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            date, category, item, amount = line.split(",")

            amount = int(amount)

            records.append({'date':date, 'category':category, 'item':item, 'amount':amount})
    return records

def show_all():
    records = load_record()

    print("="*46)
    print(f'{"용 돈 기 록 장":<8}')
    print("-"*46)

    if not records:
        print("아직 기록이 없습니다")
        return

    print(f'{"번호":<5}{"날짜":<12}{"분류":<7}{"내용":<13}{"금액":>9}')
    print("-"*46)

    for i, r in enumerate(records, 1):
        print(f"{i:<5}{r['date']:<12}{r['category']:<7}{r['item']:<13}{r['amount']:>9,}")

    print("-"*46)

    total = sum([r['amount'] for r in records])

    print(f'{"합계":<37}{total:>9,}')
    print("="*46)

    




add_record("2026-08-24", "식비", "점심 김밥", 7000)

records = load_record()

print(len(records))
print(records[0])
print(records[0]['amount'] + 1000)

show_all()
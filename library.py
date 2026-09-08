from abc import ABC, abstractmethod


class Libraryitem(ABC):

    total_items = 0

    def __init__(self, title, item_id):
            self.title = title
            self.item_id = item_id
            self.is_loaned = False
            self.borrower = None
            self.total_items = self.total_items + 1

    def checkout(self, name):
        if self.is_loaned:
            return False

        self.is_loaned = True
        self.borrower = name
        return True

    def return_item(self):
        if not self.is_loaned:
            return False

        print(f"{self.borrower}님이 반납했습니다")
        self.is_loaned = False
        self.borrower = None
        return True
    
    @abstractmethod
    def loan_period(self):
        pass
    
    @abstractmethod
    def info(self):
        pass


class Book(Libraryitem):

    def __init__(self, title, item_id, author, pages):
        super().__init__(title, item_id)
        self.author = author
        self.pages = pages

    def loan_period(self):
         return 14

    def info(self):
        return f"[도서]{self.title}/{self.author}/{self.pages}쪽"


class DVD(Libraryitem):
    def __init__(self, title, item_id, director, minutes):
        super().__init__(title, item_id)
        self.director = director
        self.minutes = minutes
        

    def loan_period(self):
        return 7

    def info(self):
        return f"[DVD] {self.title} / {self.director} 감독 / {self.minutes}분" 
    
class Magazine(Libraryitem):
    def __init__(self, title, item_id, issue):
        super().__init__(title, item_id)
        self.issue = issue
        

    def loan_period(self):
        return 3

    def info(self):
        return f"[잡지]{self.title} / {self.issue}호"


class Library:
    def __init__(self, library_name, items):
        self.library_name = library_name
        self.items = items

    def add(self, item):
        self.items.append(item)
        print(f"총{len(self.items)}개")

    def find(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None


    def show_all(self):

        for item in self.items:item.info()

        
        state = f"대출중({item.borrower})"if item.is_loaned else "대출가능"

        print("="*56)

        print(f"{self.library_name:>8}")

        print("="*56)

        print(f"{'ID':<6}, {'정보':<32}, {'상태':>14}")

        print("-"*56)
        for item in self.items:
            if item.is_loaned:
                state = f"대출중({item.borrower})"
            else:
                state = "대출 가능"

            print(f"{item.item_id:<6}{item.info():<32}{state:>14}")


    def report(self):

        book_count = sum(
            isinstance(item, Book)
            for item in self.items
        )
        dvd_count = sum(
            isinstance(item, Magazine)
            for item in self.items
        )
        magazine_count = sum(
            isinstance(item, Magazine)
            for item in self.items
        )

        loaned_count = sum(
            item.is_loaned
            for item in self.items
        )

        print("-"*56)
        print(f"{'종류별 등록 현황':>8}")
        print(f"-"*56)
        print(f"{type(self.items).__name__:<6}{book_count:<32}")
        print(f"{type(self.items).__name__:<6}{dvd_count:<32}")
        print(f"{type(self.items).__name__:<6}{magazine_count:<32}")
        print("-"*56)
        print(f"{'대출 중':<6}{loaned_count:<32}")
        print(f"{'전체 등록':<6}{Libraryitem.total_items}")
        print("-"*56)             

library = Library("한빛도서관", [])
library.add(
    Book("파이썬 입문", "B001", "박응용", 480)
)
library.add(
    Book("자료구조", "B002", "김철수", 320)
)
library.add(
    DVD("인터스텔라", "D001", "놀란 감독", 169)
)
library.add(
    Magazine("과학동아", "M001", 9)
)

while True:
    choice = input(f"1.전체 목록, 2. 통계, 3. 대출, 4. 반납, 0. 종료:").strip()

    

    if choice == "0":
        break
    elif choice == "1":
        library.show_all()

    elif choice == "2":
        library.report()

    elif choice == "3":
        item_id = input("대출할 도서의 id를 입력하세요:").strip()
        item = library.find(item_id)

        if item is None:
            print("해당 id의 도서는 없습니다.")

        else:
            name = input("대출자 이름을 입력하세요:").strip()
            item.checkout(name)
        
    elif choice == "4":
        item_id = input("반납할 도서의 id를 입력하세요:").strip()
        item = library.find(item_id)

        if item is None:
            print("해당 id의 자료가 없습니다")

        else:
            item.return_item()
        

    else:
        print("없는 메뉴입니다")



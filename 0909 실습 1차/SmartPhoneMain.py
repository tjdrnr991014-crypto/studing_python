from Address import Addr
from SmartPhone import SmartPhone

class SmartPhoneMain:

    def printMenu(self):

        print(f"주소관리 메뉴")
        print("-"*30)
        print(f"1. 연락처 등록")
        print(f"2. 모든 연락처 출력")
        print(f"3. 연락처 검색")
        print(f"4. 연락처 삭제")
        print(f"5. 연락처 수정")
        print(f"6. 프로그램 종료")
        print("-"*30)

    def Start(self):

        phone = SmartPhone()

        addr1 = Addr("이성국", "01088779911", "python01@naver.com", "대구광역시", "친구")
        addr2 = Addr("박형우", "01055446622", "python02@naver.com", "대구광역시", "친구")
        
        phone.addAddr(addr1)
        phone.addAddr(addr2)
        
        while True:

            self.printMenu()


            choice = input("원하는 작업을 선택하세요(1~6):")

            if choice == "6":
                print("종료합니다.")
                break

            elif choice == "1":
                addr = phone.inputAddrData()
                phone.addAddr(addr)

            elif choice == "2":
                phone.PrintAllAddr()

            elif choice == "3":
                phone.searchAddr()

            elif choice == "4":
                phone.deleteAddr()

            elif choice == "5":
                phone.editAddr()

            else:
                print("잘못된 번호입니다.")
                continue




go = SmartPhoneMain()
go.Start()
from Address import Addr
from Address import CompanyAddr
from Address import CustomerAddr
from SmartPhone import SmartPhone

class SmartPhoneMain:

    def printMenu(self):

        print(f"Contact Manager")
        print("-"*30)
        print(f"1. 연락처 등록(회사)")
        print(f"2. 연락처 등록(거래처)")
        print(f"3. 모든 연락처 출력")
        print(f"4. 연락처 검색")
        print(f"5. 연락처 삭제")
        print(f"6. 연락처 수정")
        print(f"7. 프로그램 종료")
        print("-"*30)

    def Start(self):

        phone = SmartPhone()

        addr1 = CompanyAddr("우영우", "01088779911", "python01@naver.com", "대구광역시", "회사", 
                            "0000-01-01", "python", "sw", "대리")
        addr2 = CustomerAddr("박형우", "01055446622", "python02@naver.com", "대구광역시", "거래처",
                             "0000-01-01", "c++", "아이스아메리카노", "주임") 

        phone.addAddr(addr1)
        phone.addAddr(addr2)
        
        while True:

            self.printMenu()


            choice = input("원하는 작업을 선택하세요(1~7):")

            if choice == "7":
                print("종료합니다.")
                break

            elif choice == "1":
                company_addr = phone.inputCompanyAddr()
                phone.addAddr(company_addr)

            elif choice == "2":
                customer_addr = phone.inputCustomerAddr()
                phone.addAddr(customer_addr)

            elif choice == "3":
                phone.PrintAllAddr()

            elif choice == "4":
                phone.searchAddr()

            elif choice == "5":
                phone.deleteAddr()

            elif choice == "6":
                phone.editAddr()

            else:
                print("잘못된 번호입니다.")
                continue




go = SmartPhoneMain()
go.Start()
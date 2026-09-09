from Address import Addr
from Address import CompanyAddr
from Address import CustomerAddr

class SmartPhone:
    
    def __init__(self):

        self.addrlist = []

    def inputAddrData(self):
        
        name = input(f"이름:")
        phone_number = input(f"전화번호:")
        email = input(f"이메일:")
        address = input(f"주소:")
        group = input(f"그룹(회사/거래처):")
        birth = input(f"생일:")

        addr = Addr(name, phone_number, email, address, group, birth)

        return addr

    def inputCompanyAddr(self):
        
        name = input(f"이름:")
        phone_number = input(f"전화번호:")
        email = input(f"이메일:")
        address = input(f"주소:")
        group = input(f"그룹(회사/거래처):")
        birth = input(f"생일:")

        company_name = input(f"회사 이름:")
        department_name = input(f"부서 이름:")
        position = input(f"직급:")

        companyaddr = CompanyAddr(name, phone_number, email, address, group, 
                                  birth, company_name, department_name, position)

        return companyaddr

    def inputCustomerAddr(self):

        name = input(f"이름:")
        phone_number = input(f"전화번호:")
        email = input(f"이메일:")
        address = input(f"주소:")
        group = input(f"그룹(회사/거래처):")
        birth = input(f"생일:")

        customer_name = input(f"거래처 이름:")
        item = input(f"품목 이름:")
        customer_position = input(f"직급:")

        customeraddr = CustomerAddr(name, phone_number, email, address, group, 
                                    birth, customer_name, item, customer_position)

        return customeraddr


    def addAddr(self, addr):

        if len(self.addrlist) >= 12:
            print(f"최대 12개까지 저장 가능합니다")

        else:
            self.addrlist.append(addr)
            return f"데이터가 저장되었습니다."

    def PrintAddr(self, addr):

        print(f"이름: {addr.name}")
        print(f"전화번호:{addr.phone_number}")
        print(f"이메일:{addr.email}")
        print(f"주소:{addr.address}")
        print(f"그룹(회사/거래처)):{addr.group}")
        print(f"생일:{addr.birth}")

        if addr.group == "회사":
            print(f"회사 이름:{addr.company_name}")
            print(f"부서 이름:{addr.department_name}")
            print(f"직급:{addr.position}")

        elif addr.group == "거래처":
            print(f"거래처 이름:{addr.customer_name}")
            print(f"품목 이름:{addr.item}")
            print(f"직급:{addr.customer_positin}")

        else:
            return None

    def PrintAllAddr(self):

        for addr in self.addrlist:

            print(f"이름:", addr.name)
            print(f"전화번호:", addr.phone_number)
            print(f"이메일:", addr.email)
            print(f"주소:", addr.address)
            print(f"그룹(회사/거래처):", addr.group)
            print(f"생일:", addr.birth)

            if addr.group == "회사":
                print(f"회사 이름:", addr.company_name)
                print(f"부서 이름:", addr.department_name)
                print(f"직급:", addr.position)
            
            elif addr.group == "거래처":
                print(f"거래처 이름:", addr.customer_name)
                print(f"품목 이름:", addr.item)
                print(f"직급:", addr.customer_position)

            else:
                return None


    def searchAddr(self):

        search = input(f"검색할 이름:")

        for addr in self.addrlist:

            if addr.name == search:

                print(f"이름:", addr.name)
                print(f"전화번호:", addr.phone_number)
                print(f"이메일:", addr.email)
                print(f"주소:", addr.address)
                print(f"그룹(회사/거래처):", addr.group)
                print(f"생일:", addr.birth)

                if addr.group == "회사":
                    print(f"회사 이름:", addr.company_name)
                    print(f"부서 이름:", addr.department_name)
                    print(f"직급:", addr.position)
                            
                elif addr.group == "거래처":
                    print(f"거래처 이름:", addr.customer_name)
                    print(f"품목 이름:", addr.item)
                    print(f"직급:", addr.customer_positin)
                
                else:
                    return None
                return

    def deleteAddr(self):

        delete = input(f"삭제할 이름:")

        for addr in self.addrlist:

            if addr.name == delete:

                self.addrlist.remove(addr)

                return f"삭제되었습니다."

    def editAddr(self):

        edit = input(f"수정할 이름:")

        for addr in self.addrlist:

            if addr.name == edit:

                addr.name = input(f"수정한 이름:")
                addr.phone_number = input(f"수정한 전화번호:")
                addr.email = input(f"수정한 이메일:")
                addr.address = input(f"수정한 주소:")
                addr.group = input(f"수정한 그룹(회사/거래처):")
                addr.birth = input(f"수정한 생일:")

                if addr.group == "회사":
                    addr.company_name = input(f"수정한 회사 이름:")
                    addr.department_name= input(f"수정한 부서 이름:")
                    addr.position = input(f"수정한 직급:")
                                            
                elif addr.group == "거래처":
                    addr.customer_name = input(f"수정한 거래처 이름:")
                    addr.item = input(f"수정한 품목이름:")
                    addr.customer_position = input(f"수정한 직급:")

                return f"수정되었습니다"
                    
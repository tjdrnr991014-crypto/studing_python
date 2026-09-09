from Address import Addr

class SmartPhone:
    
    def __init__(self):

        self.addrlist = []

    def inputAddrData(self):
        
        name = input(f"이름:")
        phone_number = input(f"전화번호:")
        email = input(f"이메일:")
        address = input(f"주소:")
        group = input(f"그룹(친구/가족):")

        addr = Addr(name, phone_number, email, address, group)
        return addr


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
        print(f"그룹(친구/가족):{addr.group}")

    def PrintAllAddr(self):

        for addr in self.addrlist:

            print(f"이름:", addr.name)
            print(f"전화번호:", addr.phone_number)
            print(f"이메일:", addr.email)
            print(f"주소:", addr.address)
            print(f"그룹(친구/가족):", addr.group)


    def searchAddr(self):

        search = input(f"검색할 이름:")

        for addr in self.addrlist:

            if addr.name == search:

                print(f"이름:", addr.name)
                print(f"전화번호:", addr.phone_number)
                print(f"이메일:", addr.email)
                print(f"주소:", addr.address)
                print(f"그룹(친구/가족):", addr.group)

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

                new_name = input(f"수정한 이름:")
                new_phone_number = input(f"수정한 전화번호:")
                new_email = input(f"수정한 이메일:")
                new_address = input(f"수정한 주소:")
                new_group = input(f"수정한 그룹:")

                return f"수정되었습니다"
            
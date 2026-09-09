class Addr:
    def __init__(self, name, phone_number, email, address, group, birth):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
        self.group = group
        self.birth = birth

    def PrintAddr(self):
        print("이름:", self.name)
        print("전화번호:", self.phone_number)
        print("이메일:", self.email)
        print("주소:", self.address)
        print("그룹(회사/거래처):", self.group)
        print("생일:", self.birth)

class CompanyAddr(Addr):

    def __init__(self, name, phone_number, email, address, group, 
                 birth, company_name, department_name, position):
        
        super().__init__(name, phone_number, email, address, group, birth)
        self.company_name = company_name
        self.department_name = department_name
        self.position = position

    def PrintAddr(self):

        super.PrintAddr()

        print("회사 이름:", self.company_name)
        print("부서 이름:", self.department_name)
        print("직급:", self.position)

class CustomerAddr(Addr):
    def __init__(self, name, phone_number, email, address, group, 
                 birth, customer_name, item, customer_position):
        super().__init__(name, phone_number, email, address, group, birth)
        self.customer_name = customer_name
        self.item = item
        self.customer_position = customer_position

    def printAddr(self):

        super.printAddr()

        print("거래처 이름:", self.customer_name)
        print("품목 이름:", self.item)
        print("직급:", self.customer_position)

        



class Industry:
    salary=50000
    def __init__(self,name,gender,mobile_no,dob):
        self.name=name
        self.gender=gender
        self.mobile_no=mobile_no
        self.dob=dob
        
    def Emp_info(self):
        info=f"Name : {self.name}\nGender : {self.gender}\nMobile_no : {self.mobile_no}\nDOB : {self.dob}"
        return info
    
    def Tax(self,amount):
        self.salary=self.salary-amount

    @classmethod
    def increment(cls,amount):
        cls.salary=amount

    @staticmethod
    def sector(service):
        ser=['Hardware','Software']
        if service in ser:
            return True
        return False

e1=Industry('kowsi','Female',9811121543,2000)
e2=Industry('Monish','Male',9887766564,1999)
Industry.increment(100000)
print(e1.Emp_info())
print(e1.salary)
print(Industry.sector('Software'))

#OUTPUT
Name : kowsi
Gender : Female
Mobile_no : 9811121543
DOB : 2000
100000
True

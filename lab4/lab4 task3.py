class Account:
    def setter(self,num,bal,sc):
        self.__account_no=num
        self.__account_bal=bal
        self.__security_code=sc
    def getter(self):
        print("account no: ",self.__account_no)
        print("account balance: ",self.__account_bal)
        print("security code: ",self.__security_code)

acc1=Account()
acc1.setter(123,2000,3456)
acc1.getter()
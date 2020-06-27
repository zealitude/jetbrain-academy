import sqlite3
import random

class BankingSystem:

    conn = None
    loginedCarNum = None

    def __init__(self):
        self.createDB()
        self.createTable()

    def getDBCursor(self):
        return self.conn.cursor()

    def executeQuery(self, queryString, prepareStatment = ()):
        return self.getDBCursor().execute(queryString, prepareStatment)

    def createDB(self):
        self.conn = sqlite3.connect('card.s3db')

    def createTable(self):
        self.executeQuery("""create table if not exists card (
                        id INTEGER,
                        number TEXT,
                        pin TEXT,
                        balance INTEGER DEFAULT 0
                )""")

    def getBalance(self):
        cursor = self.executeQuery(f"select * from card where number = {self.loginedCarNum}")
        row = cursor.fetchone()
        return float(row[3])

    def checkBalance(self):
        balance = self.getBalance()
        print(f"Balance: {balance}\n")

    def updateBalance(self, cardNum, income):
        cursor = self.executeQuery(f"update card set balance = balance + {income} where number = {cardNum}")
        self.conn.commit()

    def addIncome(self):
        income = int(input("Enter income:"))
        self.updateBalance(self.loginedCarNum, income)
        print("Income was added!")

    def doTransfer(self):
        print("Transfer")
        targetCardNum = input("Enter card number:")

        if targetCardNum[:6] != "400000":
            print("Such a card does not exist.")
            return
        elif not self.isValidCarNumber(targetCardNum):
            print("Probably you made mistake in the card number. Please try again!")
            return
        elif targetCardNum == self.loginedCarNum:
            print("You can't transfer money to the same account!")
            return
        elif not self.isAccountExist(targetCardNum):
            print("Such a card does not exist.")
            return

        amount = int(input("Enter how much money you want to transfer:"))
        if self.getBalance() < amount:
            print("Not enough money!")
            return

        self.updateBalance(self.loginedCarNum, -amount)
        self.updateBalance(targetCardNum, amount)
        print("Success!")

    def closeAccount(self):
        cursor = self.executeQuery(f"delete from card where number = {self.loginedCarNum}")
        self.conn.commit()

    def logout(self):
        self.loginedCarNum = None
        print("You have successfully logged out!")

    def isLogined(self):
        return self.loginedCarNum is not None

    def loginAccount(self):
        cardNum = input("Enter your card number:")
        pinCode = input("Enter your PIN:")

        cursor = self.executeQuery("select * from card where number = ?", (cardNum,))
        row = cursor.fetchone()

        if row is None or row[2] != pinCode:
            print("Wrong card number or PIN!")
        else:
            self.loginedCarNum = cardNum
            print("You have successfully logged in!")

    def randomSequenceGenerateor(self, len, possibleChoices):
        seq = ""
        for _ in range(len):
            seq += random.choice(possibleChoices)

        return seq

    def isValidCarNumber(self, cardNum):
        return self.calcCheckSum(cardNum[:-1]) == cardNum[-1]

    def calcCheckSum(self, cardNumWithoutCheckSum):
        sumAll = 0
        for index, char in enumerate(cardNumWithoutCheckSum):
            temp = int(char)
            if index % 2 == 0: # 0-based index
                temp = temp * 2
                if temp >= 10:
                    temp = temp - 9
            # print(temp)
            sumAll += temp
        # print(sumAll)
        checkSum = 10 - sumAll % 10
        checkSum = 0 if checkSum == 10 else checkSum
        # print(checkSum)
        return str(checkSum)

    def generateNewCardNumber(self):
        cardNum = "400000" + self.randomSequenceGenerateor(9, "0123456789")
        # cardNum = "4000008784315851"
        return cardNum + self.calcCheckSum(cardNum)

    def generatePinCode(self):
        return self.randomSequenceGenerateor(4, "0123456789")

    def isAccountExist(self, cardNum):
        cursor = self.executeQuery("select * from card where number = ?", (cardNum,))
        row = cursor.fetchone()
        return row is not None

    def createAccount(self):
        while True:
            cardNum = self.generateNewCardNumber()
            if not self.isAccountExist(cardNum):
                pinCode = self.generatePinCode()
                cursor = self.executeQuery("insert into card (number, pin, balance) values (?, ?, ?)", (cardNum, pinCode, 0))
                self.conn.commit()
                print("Your card has been created")
                print("Your card number:")
                print(cardNum)
                print("Your card PIN:")
                print(pinCode)
                print()
                break

        # for row in self.executeQuery(f"select * from card"):
        #     print(row)

    def unloginMenu(self):
        print("""1. Create an account
2. Log into account
0. Exit""")
        option = input()
        return option

    def loginedMenu(self):
        print("""1. Balance
2. Add income
3. Do transfer
4. Close account
5. Log out
0. Exit""")
        option = input()
        return option

    def start(self):
        while True:
            if not self.loginedCarNum:
                option = self.unloginMenu()
                if option == "1":
                    self.createAccount()
                elif option == "2":
                    self.loginAccount()
                elif option == "0":
                    break
            else:
                option = self.loginedMenu()
                if option == "1":
                    self.checkBalance()
                elif option == "2":
                    self.addIncome()
                elif option == "3":
                    self.doTransfer()
                elif option == "4":
                    self.closeAccount()
                elif option == "5":
                    self.logout()
                elif option == "0":
                    break
            print('')

        self.conn.close()
        print("\nBye!")


def main():
    bs = BankingSystem()
    bs.start()

if __name__ == '__main__':
    main()

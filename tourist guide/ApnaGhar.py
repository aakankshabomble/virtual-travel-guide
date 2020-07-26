class OurHotel:
    def __init__(self, rt='', s=0, r=0, p=0, a=1000, name='', address='', cindate='', coutdate='', rno=104):

        print("***********************")
        print("\n**WELCOME TO APNAGHAR**2\n")
        print("***********************\n")

        self.rt = rt
        self.r = r
        self.s = s
        self.p = p
        self.a = a
        self.name = name
        self.address = address
        self.cindate = cindate
        self.coutdate = coutdate
        self.rno = rno

    def inputdata(self):
        self.name = input("\nPlease enter your name sir/mam: ")
        self.address = input("\nPlease enter your address: ")
        self.cindate = input("\nPlease enter your Check-in date: ")
        self.coutdate = input("\nPlease enter your Check-out date: ")
        print("\nYour room number is ", self.rno, "\n")

    def roomrent(self):
        print("*We have following rooms for you ***")
        print("1.   AC room with extra bed -----> 6000Rs per member ")
        print("2.   AC room with single bed  -----> 5000Rs per member ")
        print("3.   Non AC room with extra bed -----> 4000Rs per member ")
        print("4.   Non AC room with single bed -----> 3000Rs per member ")

        x = int(input("Enter your Choice please --> \n"))

        n = int(input("For How many Nights You Stay: "))

        if (x == 1):
            print("You have opted for AC room with extra bed ")
            self.s = 6000 * n

        elif (x == 2):
            print(" You have opted for AC room with  single bed ")
            self.s = 5000 * n

        elif (x == 3):
            print(" You have opted for Non AC room with extra bed ")
            self.s = 4000 * n

        elif (x == 4):
            print(" You have opted for Non AC room with  single bed ")
            self.s = 3000 * n

        else:
            print("Please Choose a room ")

        print("Your room rent is =", self.s, "\n ")

    def restaurentbill(self):

        print("\n\n***RESTAURENT MENU*")
        print("\n***We have following menu for you ***")
        print("1.   Mineral Water -----> 20Rs per bottle ")
        print("2.   Garam Garam Chaaai  -----> 25Rs per cup ")
        print("3.   Coffee  -----> 30Rs per cup ")
        print("4.   Cold Coffee -----> 80Rs per cup ")
        print("5.   BreakFast Combo  -----> 150Rs per Combo ")
        print("6.   Lunch  -----> 300Rs per thaali ")
        print("7.   Dinner -----> 355Rs per thaali ")
        print("8.   EXIT ")

        while (1):

            c = int(input("Please Enter Your Choice: "))
            if c == 1:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 20 * d

            elif c == 2:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 25 * d

            elif c == 3:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 30 * d

            elif c == 4:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 80 * d

            elif c == 5:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 150 * d

            elif c == 6:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 300 * d

            elif c == 7:
                d = int(input("Please Enter the Quantity: "))
                self.r = self.r + 355 * d

            elif c == 8:
                break;
            else:
                print("Invalid Option")

        print("Total food cost = Rs", self.r, "\n")

    def gamingbill(self):
        print("\n\n***WELCOME TO GAMING SECTION*")
        print("1.   Table Tennis -----> 60Rs per hour")
        print("2.   Bowling  -----> 80Rs per hour")
        print("3.   Snooker  -----> 75Rs per hour ")
        print("4.   Video Games -----> 80Rs per hour ")
        print("5.   Pool  -----> 50Rs per hour ")
        print("6.   Badminton  -----> 60Rs per hour ")
        print("7.   PUBG -----> 250Rs per hour ")
        print("8.   Cricket -----> 400Rs per hour")
        print("9.   EXIT ")

        while (1):

            g = int(input("Enter your choice: "))

            if g == 1:
                h = int(input("No. of hours: "))
                self.p = self.p + 60 * h

            elif g == 2:
                h = int(input("No. of hours: "))
                self.p = self.p + 80 * h

            elif g == 3:
                h = int(input("No. of hours: "))
                self.p = self.p + 75 * h

            elif g == 4:
                h = int(input("No. of hours: "))
                self.p = self.p + 80 * h

            elif g == 5:
                h = int(input("No. of hours: "))
                self.p = self.p + 50 * h

            elif g == 6:
                h = int(input("No. of hours: "))
                self.p = self.p + 60 * h

            elif g == 7:
                h = int(input("No. of hours: "))
                self.p = self.p + 250 * h

            elif g == 8:
                h = int(input("No. of hours: "))
                self.p = self.p + 400 * h


            elif g == 9:
                break;
            else:

                print("Invalid option")

        print("Total Game Bill=Rs", self.p, "\n")

    def display(self):
        print("\n\n**HOTEL BILL**")
        print("Customer details:")
        print("Customer name:", self.name)
        print("Customer address:", self.address)
        print("Check in date:", self.cindate)
        print("Check out date", self.coutdate)
        print("Room no.", self.rno)
        print("Your Room rent is:", self.s)
        print("Your Food bill is:", self.r)
        print("Your Game bill is:", self.p)
        self.rt = self.s + self.p + self.r

        print("Your sub total bill is:", self.rt)
        print("Additional Service Charges is", self.a)
        print("Your grandtotal bill is:", self.rt + self.a, "\n")
        self.rno += 1


def main():
    a = OurHotel()

    while (1):
        print("1. Enter Customer Data")

        print("2. Calculate rommrent")

        print("3. Calculate restaurant bill")

        print("4. Calculate gamebill")

        print("5. Total Cost")

        print("6.EXIT")

        b = int(input("\n Please Enter Your Choice: "))
        if b == 1:
            a.inputdata()

        if b == 2:
            a.roomrent()

        if b == 3:
            a.restaurentbill()

        if b == 4:
            a.gamingbill()

        if b == 5:
            a.display()

        if b == 6:
            quit()


main()

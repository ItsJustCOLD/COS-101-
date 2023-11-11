print("""
    {The Best Store around}
    Yusuf and sons limited
                                      Welcome,Customer
Kindly fill out the information below:
""")
Principal= float(input("please input the principal amount :"))
Rate= float(input("please input rate :"))
Time= float(input("please input time :"))
simple_interest= (Principal * Rate * Time)/100
compound_interest= (Principal * (1 + Rate/100)**Time-1)
print(simple_interest)
print(compound_interest)
print("""
Dear Ma/Sir
The Simple Interest and The Compound Interest respectively have been found for you above after putting the values of your choice.
                                         Thank You Very Much
         !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
         """)

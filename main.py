# QAP 4 Project 1 Data Files

# Author: Savanna Fifield       Date: 11/25/2022


import datetime


# Constants
HST_RATE = .15
NexPolNum = 1944 + 1
BASE_PREM_RATE = 869.00
ADD_CAR_DIS_RATE = .25
LIAB_COV_RATE = 130.00
GLASS_COV_RATE = 86.00
LOAN_COV_RATE = 58.00
PROCESS_FEE = 39.99

# Inputs
FirstName = input("Enter customers first name: ").title()
LastName = input("Enter customers last name: ").title()
StAdd = input("Enter customers Street Address: ")
City = input("Enter the city: ").upper()
Province = input("Enter the province: ").upper()
PostCode = input("Enter customers postal code: ").upper()
PhNum = input("Enter customers Phone Number: ")
NumCarIn = int(input("Enter the # of cars to be insured: "))
ExtraLib = input("Would the customer like extra Liability? Y or N: ").upper()

# Calculations
TotExtraCost = LIAB_COV_RATE + GLASS_COV_RATE + LOAN_COV_RATE
TotPremium = BASE_PREM_RATE + TotExtraCost
HST = TotPremium * HST_RATE
TotCost = TotPremium + HST
MonthPayment = (TotCost + PROCESS_FEE) / 8

# if Statements

if NumCarIn == 1:
    ExtraLib = LIAB_COV_RATE * NumCarIn
elif NumCarIn >= 1:
    ExtraLib = (ADD_CAR_DIS_RATE * NumCarIn) + LIAB_COV_RATE * NumCarIn

GlassCove = input("Would the customer like extra glass coverage? Y or N: ").upper()
if GlassCove == "Y":
    GlassCove = GLASS_COV_RATE * NumCarIn
elif GlassCove == "N":
    GlassCove = 0
    print()

LoanCar = input("Would the customer like a loaner car? Y or N: ").upper()
if LoanCar == "Y":
    LoanCar = LOAN_COV_RATE * NumCarIn
elif LoanCar == "N":
    LoanCar = 0
    print()

FullOrMon = input("Would the customer like to pay in full or monthly? F or M: ").upper()
if FullOrMon == "M":
    print()
elif FullOrMon == "F":
    print()


# Formatting
ExtraLibDsp = "${:,.2f}".format(ExtraLib)
GlassCoveDsp = "${:,.2f}".format(GlassCove)
LoanCarDsp = "${:,.2f}".format(LoanCar)
TotExtraCostDsp = "${:,.2f}".format(TotExtraCost)
TotPremiumDsp = "${:,.2f}".format(TotPremium)
HSTDsp = "${:,.2f}".format(HST)
TotCostDsp = "${:,.2f}".format(TotCost)
MonthPaymentDsp = "${:,.2f}".format(MonthPayment)

# Display outputs
print(f"        ONE STOP INSURANCE COMPANY     ")
print(f"==============================================     ")
print(f"Customer Information:               ")
print(f"-----------------------------------------------      ")
print(f"First Name:", (FirstName) , (LastName))
print(f"Policy Number:" , (NexPolNum))
print(f"Address: {StAdd:<5}   {City:<5}   {Province:<3}   {PostCode:<3}")
print(f"Phone Number:", (PhNum))
print(f"===============================================     ")
print(f"Pricing Information:                 ")
print(f"-----------------------------------------------      ")
print(f"Extra Liability Cost: {ExtraLibDsp:>20}")
print(f"Glass Coverage Cost: {GlassCoveDsp:>21}")
print(f"Loaner Car Cost: {LoanCarDsp:>25}")
print(f"Extra Costs: {TotExtraCostDsp:>29}")
print(f"Total Premium Cost: {TotPremiumDsp:>22}")
print(f"Full Price: {TotCostDsp:>30}")
if FullOrMon == "M":
    print(f"Monthly Payment: {MonthPaymentDsp:>25}")
print(f"===============================================     ")
print("Policy information processed and saved.")

# Policy File Creation
f = open("Policies.dat" , "w")
f.write("{},".format(NexPolNum))
f.write("{},".format(FirstName))
f.write("{},".format(LastName))
f.write("{},".format(StAdd))
f.write("{},".format(City))
f.write("{},".format(Province))
f.write("{},".format(PostCode))
f.write("{},".format(PhNum))
f.write("{},".format(NumCarIn))
f.write("{},".format(ExtraLib))
f.write("{},".format(GlassCove))
f.write("{},".format(LoanCar))
f.write("{},".format(FullOrMon))
f.write("{},".format(TotPremium))

f.close()




# File Creation

f = open("OSICDef.dat" , "w")

f.write("{},".format(NexPolNum))
f.write("{},".format(BASE_PREM_RATE))
f.write("{}".format(ADD_CAR_DIS_RATE))
f.write("{}".format(LIAB_COV_RATE))
f.write("{}".format(GLASS_COV_RATE))
f.write("{}".format(LOAN_COV_RATE))
f.write("{}".format(HST_RATE))
f.write("{}".format(PROCESS_FEE))

f.close()
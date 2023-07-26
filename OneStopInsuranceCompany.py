# Program for One Stop Insurance Company to enter and calculate insurance policies
# Written by: Kyla Leaman
# Date written: July 18, 2023

# import libraries
import datetime
import FormatValues as FV
import time
from tqdm import tqdm


# define constants - Open the defaults file and read the values into variables
f = open('OSICDef.dat', 'r')
NEXT_POLICY_NUM = int(f.readline())
BASIC_PREMIUM = float(f.readline())
ADD_CAR_DISCOUNT = float(f.readline())
EXTRA_LIABILITY_COVERAGE = float(f.readline())
GLASS_COVERAGE = float(f.readline())
LOANER_COVERAGE = float(f.readline())
HST_RATE = float(f.readline())
PROCESSING_FEE = float(f.readline())
f.close()

# define required functions
def FindPaymentDate(InvDate):
    # Determine the next payment date.
    invDateYear = invDate.year
    invDateMonth = invDate.month
    invDateDay = invDate.day

    payDateDay = 1
    payDateMonth = invDateMonth + 1
    payDateYear = invDateYear

    if invDateMonth == 12:
        payDateYear += 1
    payDate = datetime.date(payDateYear, payDateMonth, payDateDay)

    return payDate

# main program
while True:

    # inputs
    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        custFirst = input("Enter the customer's first name: ").title()
        if custFirst == "":
            print("Error - Customer first name must be entered.")
        elif not set(custFirst).issubset(allowed_char):
            print("Error - Customer name contains invalid characters.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'.")
        custLast = input("Enter the customer's last name: ").title()
        if custLast == "":
            print("Error - Customer last name must be entered.")
        elif not set(custLast).issubset(allowed_char):
            print("Error - Customer name contains invalid characters.")
        else:
            break

    while True:
        streetAdd = input("Enter the street address: ").title()
        if streetAdd == "":
            print("Error - street address must be entered.")
        else:
            break

    while True:
        allowed_char = set("ABCDEFGHIJKLMONPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz-'")
        city = input("Enter the city: ").title()
        if city == "":
            print("Error - City must be entered.")
        elif not set(city).issubset(allowed_char):
            print("Error - Customer name contains invalid characters.")
        else:
            break

    provLst = ["NL", "NS", "PE", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NV"]
    while True:
        prov = input("Enter the province (LL): ").upper()
        if prov == "":
            print("Error - Province must be entered.")
        elif len(prov) != 2:
            print("Error - Province must be 2 letters only.")
        elif prov not in provLst:
            print("Error - not a valid province.")
        else:
            break

    while True:
        allowed_letters = set("ABCDEFGHIJKLMONPQRSTUVWXYZ")
        allowed_numbers = set("0123456789")
        postCode = input("Enter the postal code (L0L0L0): ").upper()
        if postCode == "":
            print("Error - Postal code must be entered.")
        elif len(postCode) != 6:
            print("Error - Postal code must be 6 characters.")
        elif not set(postCode[0]).issubset(allowed_letters):
            print("Error - First character in the postal code must be a letter.")
        elif not set(postCode[1]).issubset(allowed_numbers):
            print("Error - Second character in the postal code must be a number.")
        elif not set(postCode[2]).issubset(allowed_letters):
            print("Error - Third character in the postal code must be a letter.")
        elif not set(postCode[3]).issubset(allowed_numbers):
            print("Error - Fourth character in the postal code must be a number.")
        elif not set(postCode[4]).issubset(allowed_letters):
            print("Error - Fifth character in the postal code must be a letter.")
        elif not set(postCode[5]).issubset(allowed_numbers):
            print("Error - Sixth character in the postal code must be a number.")
        else:
            break

    while True:
        phoneNum = input("Enter the phone number (999999999): ")
        if phoneNum == "":
            print("Error - Phone number must be entered.")
        elif len(phoneNum) != 10:
            print("Error - Phone number must be 10 digits.")
        elif not phoneNum.isdigit():
            print("Error - Phone number must be 10 digits.")
        else:
            break

    while True:
        try:
            numCars = int(input("Enter the number of cars being insured: "))
        except:
            print("Error - Number of cars is not a valid number.")
        else:
            break

    extList = ["Y", "N", "y", "n"]
    while True:
        extLiability = input("Would you like to add extra liability up to $1,000,000 to policy? (Y/N): ").upper()
        if extLiability == "":
            print("Error - must be entered.")
        elif len(extLiability) != 1:
            print("Error - must enter Y or N")
        elif extLiability not in extList:
            print("Error - must enter Y or N")
        else:
            break

    while True:
        glassCov = input("Would you like to add glass coverage to policy? (Y/N): ").upper()
        if glassCov == "":
            print("Error - must be entered.")
        elif len(glassCov) != 1:
            print("Error - must enter Y or N")
        elif glassCov not in extList:
            print("Error - must enter Y or N")
        else:
            break

    while True:
        allowed_char = set["YNyn"]
        loanerCov = input("Would you like to add loaner car coverage to policy? (Y/N): ").upper()
        if loanerCov == "":
            print("Error - must be entered.")
        elif len(loanerCov) != 1:
            print("Error - must enter Y or N")
        elif loanerCov not in extList:
            print("Error - must enter Y or N")
        else:
            break

    while True:
        payPlanList = ["Full", "Monthly"]
        payPlan = input("Would you like to pay in full or monthly: ").title()
        if payPlan == "":
            print("Error - must be entered.")
        elif payPlan not in payPlanList:
            print("Error - invalid entry - must enter Full or Monthly")
        else:
            break

    # Calculations
    # Invoice date is the current date
    invDate = datetime.datetime.now()
    # Payment date is the 1st day of the next month
    payDate = FindPaymentDate(invDate)

    # Calculate the insurance premium based off the number of cars, basic premium rate and additional car discount
    insurPrem = BASIC_PREMIUM
    if numCars > 1:
        addCardis = (BASIC_PREMIUM * (numCars-1)) * ADD_CAR_DISCOUNT # calculate additional car discount amount
        insurPrem += (BASIC_PREMIUM * (numCars-1)) - addCardis # calculate the total insurance premium including the additional cars minus discount
    else:
        pass

    # Calculate the extra liability if they have selected yes
    if extLiability == "Y":
        extraLibAmount = EXTRA_LIABILITY_COVERAGE * numCars
    else:
        extraLibAmount = 0.00

    # Calculate the optional glass coverage
    if glassCov == "Y":
        glassAmount = GLASS_COVERAGE * numCars
    else:
        glassAmount = 0.00

    # Calculate the optional loaner car coverage
    if loanerCov == "Y":
        loanerAmount = LOANER_COVERAGE * numCars
    else:
        loanerAmount = 0.00

    # Calculate the total extra costs
    totExtracost = extraLibAmount + glassAmount + loanerAmount

    # Calculate the total premium including the extra costs
    totPremium = insurPrem + totExtracost

    # Calculate the HST using the HST rate
    HST = totPremium * HST_RATE

    # Calculate the total cost including HST
    totCost = totPremium + HST

    # If the client has chosen to pay monthly, calculate the monthly fee including a processing fee
    if payPlan == "Monthly":
        monthlyFee = (totCost + PROCESSING_FEE) / 8
    else:
        monthlyFee = "N/A"

    # Outputs - print into a nice receipt
    # if statements to print Yes and No for optional questions
    if extLiability == "Y":
        extLibDSP = "Yes"
    else:
        extLibDSP = "No"

    if glassCov == "Y":
        glassCovDSP = "Yes"
    else:
        glassCovDSP = "No"

    if loanerCov == "Y":
        loanerCovDSP = "Yes"
    else:
        loanerCovDSP = "No"
    print()
    print("              One Stop Insurance Company")
    print("           123 Water Street, St. John's, NL")
    print("               Insurance Claim Invoice")
    print()
    print(f"   Invoice Date:  {FV.FDateS(invDate):<10s} ")
    print(f"   Policy Number: {NEXT_POLICY_NUM}")
    print()
    custFullname = custFirst + " " + custLast
    print(f"   {custFullname:<30s}")
    phoneNumDSP = f"{phoneNum[:3]}-{phoneNum[3:6]}-{phoneNum[6:]}"
    print(f"   {phoneNumDSP:<12s}")
    print(f"   {streetAdd:<30s}")
    custAddress = city + ", " + prov + ", " + postCode
    print(f"   {custAddress:<30s}")
    print("-" * 51)
    print("   Policy Information:")
    print()
    print(f"   Extra Liability:                        {extLibDSP:<3s}")
    print(f"   Optional Glass Coverage:                {glassCovDSP:<3s}")
    print(f"   Optional Loaner Car Coverage:           {loanerCovDSP:<3s}")
    print(f"   Payment plan:                           {payPlan:<7s}")
    print(f"   Number of cars insured:                 {numCars:>2d}")
    print("-" * 51)
    print("   Optional Add-Ons:")
    print()
    print(f"   Extra Liability Cost:              {FV.FDollar2(extraLibAmount):>10s}")
    print(f"   Glass Coverage:                    {FV.FDollar2(glassAmount):>10s}")
    print(f"   Loaner Car Coverage:               {FV.FDollar2(loanerAmount):>10s}")
    print("-" * 51)
    print("   Costs:")
    print()
    print(f"   Insurance Premium(base cost):      {FV.FDollar2(insurPrem):>10s}")
    print(f"   Total Add-On Costs:                {FV.FDollar2(totExtracost):>10s}")
    print("-" * 51)
    print("   Totals:")
    print()
    print(f"   Subtotal Premium Costs:            {FV.FDollar2(totPremium):>10s}")
    print(f"   HST:                               {FV.FDollar2(HST):>10s}")
    print(f"   Total Cost:                        {FV.FDollar2(totCost):>10s}")
    print("-" * 51)
    if payPlan == "Monthly":
        print(f"   Monthly payment:                   {FV.FDollar2(monthlyFee):>10s}")
        print(f"   Your first payment is due:         {FV.FDateS(payDate):>10s}")
    else:
        print(f"   Your payment is due:               {FV.FDateS(payDate):<10s}")
    print()

    # Write
    f = open("Policies.dat", "a")
    f.write(f"{NEXT_POLICY_NUM}, ")
    f.write(f"{invDate}, ")
    f.write(f"{custFirst}, ")
    f.write(f"{custLast}, ")
    f.write(f"{streetAdd}, ")
    f.write(f"{city}, ")
    f.write(f"{prov}, ")
    f.write(f"{postCode}, ")
    f.write(f"{phoneNumDSP}, ")
    f.write(f"{numCars}, ")
    f.write(f"{extLiability}, ")
    f.write(f"{glassCov}, ")
    f.write(f"{loanerCov}, ")
    f.write(f"{payPlan}, ")
    f.write(f"{totPremium}\n")
    f.close()

    print()
    print()
    print("Saving data - please wait")
    # Processing bar
    for _ in tqdm(range(20), desc="Processing", unit="ticks", ncols=100, bar_format="{desc}  {bar}"):
        time.sleep(.1)
    print("Insurance Policy data successfully saved!")
    time.sleep(1)
    print()

    # Update the policy number
    NEXT_POLICY_NUM += 1

# Housekeeping
    Continue = input("Would you like to process another claim (Y/N)?: ").upper()
    if Continue == "N":
        break
# Update the policy number
    NEXT_POLICY_NUM += 1

# Write the current values back to the default file
f = open('OSICDef.dat', 'w')
f.write(f"{NEXT_POLICY_NUM}\n")
f.write(f"{BASIC_PREMIUM}\n")
f.write(f"{ADD_CAR_DISCOUNT}\n")
f.write(f"{EXTRA_LIABILITY_COVERAGE}\n")
f.write(f"{GLASS_COVERAGE}\n")
f.write(f"{LOANER_COVERAGE}\n")
f.write(f"{HST_RATE}\n")
f.write(f"{PROCESSING_FEE}\n")
f.close()

print()
print("Thank you for using One Stop Insurance Company!")
print("Have a great day!")









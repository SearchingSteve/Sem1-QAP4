# Description: Invoice Calculator for One Stop Insurance Company
# Take in customer data, calculate invoice values, and then display formatted receipt

# Author: Stephen Crocker
# Date - Mar 19, 2024


# Define required Libraries
import FormatValues
from datetime import datetime
import time
import sys

# Define Constants / Default Values
NEXT_POLICY_NO = 1944
BASIC_PREMIUM = 869.00
EXTRA_CAR_DISCOUNT = 0.25
EXTRA_LIABILITY_COST = 130.00
GLASS_COST = 86.00
LOANER_COST = 58.00
HST_RATE = 0.15
MONTHLY_PROCESSING_FEE = 39.99
CURR_DATE = datetime.now()

# Define Accepted Provinces
accepted_provinces = ["AB", "BC", "MB", "NB", "NL", "NS", "ON", "PE", "QC", "SK", "NT", "NU", "YT"]

# Define Accepted Pay Periods
accepted_payment_options = ["F", "M", "DP"]

# Page format constants
RECIEPT_WIDTH = 47
FULL_LINE_BREAK = "-" * RECIEPT_WIDTH
SPACE_INDENT = " " * 5


# Define Program Functions

# Province Full name to Prefix function (THE PROVINCE PREFIXER)
def ProvincePrefix(province):
    if province == "Alberta":
        return "AB"
    elif province == "British Columbia":
        return "BC"
    elif province == "Manitoba":
        return "MB"
    elif province == "New Brunswick":
        return "NB"
    elif province == "Newfoundland and Labrador":
        return "NL"
    elif province == "Nova Scotia":
        return "NS"
    elif province == "Ontario":
        return "ON"
    elif province == "Prince Edward Island":
        return "PE"
    elif province == "Quebec":
        return "QC"
    elif province == "Saskatchewan":
        return "SK"
    elif province == "Northwest Territories":
        return "NT"
    elif province == "Nunavut":
        return "NU"
    elif province == "YUKON":
        return "YT"
    else:
        return


# Function to check if postal code is valid Canadian format
def CDNPostalCodeValidation(postal_code):
    # Ensure no spaces
    postal_code = postal_code.replace(" ", "")
    # Before Checking structure, check length
    if len(postal_code) != 6:
        return False
    # Check if is Valid Canadian Postal Code
    if (postal_code[0].isalpha() and postal_code[2].isalpha() and postal_code[4].isalpha() and
            postal_code[1].isdigit() and postal_code[3].isdigit() and postal_code[5].isdigit()):
        return True
    else:
        return False


# BONUS - Save invoice data to file
## Very simply function which takes parameters of the same name as they are in the code and write them to a file
def save_invoice_data(cust_first_name, cust_last_name, address, city, province, postal_code, phone_num,
                      num_cars_insured, extra_liability, optional_glass_cov, optional_loaner_car, payment_option,
                      down_pay_amount, monthly_payment_cost, total_insurance_premium, total_cost, claims):
    # Define NEXT_POLICY_NO as global to give access throughout script
    global NEXT_POLICY_NO

    # Define a variable and file structure for the data to be saved to
    filename = f"Policy_{NEXT_POLICY_NO}.txt"

    # Try to open the filename variable with 'w' (write) permission.
    ## As f refers our filename to be a file object, which allows us to use perform the write command.
    with open(filename, 'w') as f:
        f.write(f"Customer First Name: {cust_first_name}\n")
        f.write(f"Customer Last Name: {cust_last_name}\n")
        f.write(f"Address: {address}\n")
        f.write(f"City: {city}\n")
        f.write(f"Province: {province}\n")
        f.write(f"Postal Code: {postal_code}\n")
        f.write(f"Phone Number: {phone_num}\n")
        f.write(f"Number of Cars Insured: {num_cars_insured}\n")
        f.write(f"Extra Liability Coverage: {extra_liability}\n")
        f.write(f"Glass Coverage: {optional_glass_cov}\n")
        f.write(f"Loaner Car Option: {optional_loaner_car}\n")
        f.write(f"Payment Option: {payment_option}\n")
        if payment_option != "F":
            f.write(f"Down Payment Amount: {FormatValues.FDollar2(down_pay_amount)}\n")
            f.write(f"Monthly Payment Amount: {FormatValues.FDollar2(monthly_payment_cost)}\n")
        f.write(f"Total Insurance Premium: {FormatValues.FDollar2(total_insurance_premium)}\n")
        f.write(f"Total Cost: {FormatValues.FDollar2(total_cost)}\n")

        # Emulate invoice saving processing time and display
        for _ in range(5):  # Change to control no. of 'blinks'
            print('Saving Invoice data ...', end='\r')
            time.sleep(.5)  # To create the blinking effect
            sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
            time.sleep(.5)

        # Wait inbetween invoice and claims saving processes
        time.sleep(0.5)

        # Try to write each claim data
        if claims:
            f.write("\nClaims:\n")
            for claim in claims:
                f.write(f"Claim No: {claim[0]}, Claim Date: {claim[1]}, Amount: {FormatValues.FDollar2(claim[2])}\n")

            # Emulate claims saving processing time and display
            for _ in range(len(claims)):  # Change to control no. of 'blinks'
                print('Saving Claim data ...', end='\r')
                time.sleep(.2)  # To create the blinking effect
                sys.stdout.write('\033[2K\r')  # Clears the entire line and carriage returns
                time.sleep(.2)

    # Display save confirmation and update policy no
    print("\nPolicy data has been saved.")
    NEXT_POLICY_NO += 1


# User Inputs
while True:
    cust_first_name = input("Enter Customer first name ('End' to quit): ").title()
    if cust_first_name == "End":
        break
    elif cust_first_name == "":
        print("Data Entry Error - Customer first name cannot be blank.")
        continue
    else:
        pass

    while True:
        cust_last_name = input("Enter customer last name: ").title()
        if cust_last_name == "":
            print("Data Entry Error - Customer last name cannot be blank.")
        else:
            break

    while True:
        address = input("Enter address: ").title()
        if address == "":
            print("Data Entry Error - Customer first name cannot be blank.")
        else:
            break

    while True:
        city = input("Enter city: ").title()
        if city == "":
            print("Data Entry Error - Customer first name cannot be blank.")
        else:
            break

    while True:
        province = input("Enter the province: ").upper()
        province_prefixed = ProvincePrefix(province)
        if (province or province_prefixed) not in accepted_provinces:
            print("Data Entry Error - Province is Invalid")
            continue
        else:
            if province_prefixed == None:
                province_prefixed = province
            break

    postal_code = str(input("Enter the postal code: ")).upper()
    while not CDNPostalCodeValidation(postal_code):
        print("Data Entry Error - Postal code is Invalid")
        postal_code = str(input("Enter the postal code: ")).upper()

    while True:
        phone_num = input("Enter the phone number (xxx-xxx-xxxx): ")
        if len(phone_num) != 10:  # if phone number not equal to 10, display error message and retry input
            print("Data Entry Error - phone number must be 10 digits. NUMBERS ONLY")
            continue
        elif phone_num.isdigit() == False:  # otherwise if phone number is not all digits try to get input again
            print("Data Entry Error -  characters must be digits. Enter only digits no -")
            continue
        else:
            break

    while True:
        try:
            num_cars_insured = int(input("Enter the number of cars being insured: "))
            if num_cars_insured < 1:  # Add a check to ensure at least 1 car is being insured
                print("No cars ensured; You must insure at least one car. Please enter a valid number.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        extra_liability = input("Enter extra liability up to $1000? (Y or N): ").upper()
        if extra_liability != "Y" and extra_liability != "N":
            print("Data Entry Error - Must choose Y or N")
            continue
        else:
            break

    while True:
        optional_glass_cov = input("Enter extra glass coverage? (Y or N): ").upper()
        if optional_glass_cov != "Y" and optional_glass_cov != "N":
            print("Data Entry Error - Must choose Y or N")
            continue
        else:
            break

    while True:
        optional_loaner_car = input("Optional Loaner car? (Y or N): ").upper()
        if optional_loaner_car != "Y" and optional_loaner_car != "N":
            print("Data Entry Error - Must choose Y or N")
            continue
        else:
            break

    while True:
        payment_option = input("Enter payment options: F(Full), M(Monthly), DP(Down Pay): ").upper()
        if payment_option not in accepted_payment_options:
            print("Data Entry Error - Enter one of the following payment options: F(Full), M(Monthly), DP(Down Pay)")
            continue
        elif payment_option == "DP":
            down_pay_amount = float(input("Enter the down payment amount: "))
            break
        else:
            break

    # Template claims: [0:Claim number, 1:claim date, 2:Claim amount of all previous claims for the customer]
    claim1 = ["1000", "2000-01-01", 1000]
    claim2 = ["1001", "2001-01-01", 2000]
    claim3 = ["1002", "2002-01-01", 3000]

    # Claim storage and input for recording claims
    claims = [claim1, claim2, claim3]
    while True:
        claim_number = input("Enter a claim number OR type 'END' to finish: ")
        if claim_number.upper() == 'END':
            break
        elif not claim_number.isdigit():
            print("Data Entry Error - claim no must be a digit")
            continue

        while True:
            claim_date_input = input("Enter claim date (YYYY-MM-DD): ")
            try:
                claim_date = datetime.strptime(claim_date_input, "%Y-%m-%d")
                formatted_claim_date = FormatValues.FDateS(claim_date)
                break
            except ValueError:
                print("Data Entry Error - invalid claim date")


        while True:
            claim_amount = float(input("Enter claim amount: "))
            if claim_amount <= 0:
                print("Data Entry Error - claim amount must be greater than 0")
            else:
                break
        claims.append((claim_number, formatted_claim_date, claim_amount))


    # Calculations
    if num_cars_insured == 1:
        insurance_premium = BASIC_PREMIUM
    else:
        insurance_premium = BASIC_PREMIUM + (BASIC_PREMIUM * num_cars_insured * EXTRA_CAR_DISCOUNT)

    if extra_liability == "Y":
        extra_liability_costs = num_cars_insured * EXTRA_LIABILITY_COST
    else:
        extra_liability_costs = 0

    if optional_glass_cov == "Y":
        optional_glass_cost = num_cars_insured * GLASS_COST
    else:
        optional_glass_cost = 0

    if optional_loaner_car == "Y":
        optional_loaner_cost = num_cars_insured * LOANER_COST
    else:
        optional_loaner_cost = 0

    total_extra_cost = extra_liability_costs + optional_glass_cost + optional_loaner_cost
    total_insurance_premium = insurance_premium + total_extra_cost
    HST_cost = total_insurance_premium * HST_RATE
    total_cost = total_insurance_premium + HST_cost

    if payment_option == "F":
        down_pay_amount = 0
        monthly_payment_cost = 0
        payment_option_cost = total_cost

    elif payment_option == "M":
        down_pay_amount = 0
        monthly_payment_cost = (total_cost + MONTHLY_PROCESSING_FEE) / 8
        payment_option_cost = monthly_payment_cost
    else:
        monthly_payment_cost = (total_cost + MONTHLY_PROCESSING_FEE - down_pay_amount) / 8
        payment_option_cost = monthly_payment_cost

    # Check if current month is December. If it is, must update the year.
    if CURR_DATE.month == 12:
        next_payment_date = datetime(year=CURR_DATE.year + 1, month=1, day=1)
    else:
        next_payment_date = datetime(year=CURR_DATE.year, month=CURR_DATE.month + 1, day=1)

    # Formatting dates
    invoice_date = FormatValues.FDateS(CURR_DATE)
    next_payment_date_str = FormatValues.FDateS(next_payment_date)

    # Correctly format monetary values
    total_cost_formatted = FormatValues.FDollar2(total_cost)
    total_insurance_premium_formatted = FormatValues.FDollar2(total_insurance_premium)
    HST_cost_formatted = FormatValues.FDollar2(HST_cost)

    # Print Receipt
    print(FULL_LINE_BREAK)
    print(f"One Stop Insurance Invoice".center(RECIEPT_WIDTH))
    print(f"Invoice Date: {invoice_date}".rjust(RECIEPT_WIDTH))
    print(FULL_LINE_BREAK)

    print("Customer Info:")
    print(f"{cust_first_name} {cust_last_name}")
    print(f"Address: {address}")
    print(f"{city}, {province_prefixed}, {postal_code}")
    print(f"Phone: {phone_num}")
    print(FULL_LINE_BREAK)

    print("Policy Details:")
    print(f"Policy Number: {NEXT_POLICY_NO}")
    print(f"Number of Cars Insured: {num_cars_insured}")
    print(f"Extra Liability: {extra_liability}")
    print(f"Glass Coverage: {optional_glass_cov}")
    print(f"Loaner Car: {optional_loaner_car}")
    print(FULL_LINE_BREAK)

    print("Cost Details:")
    print(f"Total Insurance Premium: {total_insurance_premium_formatted}")
    print(f"Total Extra Costs: {FormatValues.FDollar2(total_extra_cost)}")
    print(f"HST (15%): {HST_cost_formatted}")
    print(f"Total Cost: {total_cost_formatted}")
    print(FULL_LINE_BREAK)

    print("Payment Details:")
    if payment_option == "F":
        print(f"Paid in Full: {total_cost_formatted}")
    elif payment_option == "M":
        print(f"Monthly Payment: {FormatValues.FDollar2(monthly_payment_cost)} for 8 months")
    else:
        if down_pay_amount > total_cost:
            amount_owed_back = down_pay_amount - total_cost
            print(f"Down Payment: {FormatValues.FDollar2(down_pay_amount)}")
            print(f"Amount owed back to the customer: {FormatValues.FDollar2(amount_owed_back)}")
        else:
            print(f"Down Payment: {FormatValues.FDollar2(down_pay_amount)}")
            remaining_cost = total_cost - down_pay_amount

            monthly_payment_cost = remaining_cost / 8
            print(f"Remaining Monthly Payment: {FormatValues.FDollar2(monthly_payment_cost)} for 8 months")

    print(f"Next Payment Date: {next_payment_date_str}")
    print(FULL_LINE_BREAK)

    # Try to print claims
    print("Claims History:")
    print(FULL_LINE_BREAK)
    print(f"{'Claim #':<11s}{'Claim Date #':<16s}{'Amount':>20s}")
    print(FULL_LINE_BREAK)
    for claim in claims:
        print(f"{claim[0]:<11s} {claim[1]:<16s} {FormatValues.FDollar2(claim[2]):>18}")
    print(FULL_LINE_BREAK)

    # Call save_invoice_data to save the input values, calculations and claims
    save_invoice_data(cust_first_name, cust_last_name, address, city, province, postal_code, phone_num,
                      num_cars_insured, extra_liability, optional_glass_cov, optional_loaner_car, payment_option,
                      down_pay_amount, monthly_payment_cost, total_insurance_premium, total_cost, claims)

    # Ask if user wants to repeat program for another invoice
    while True:
        Continue = input("Do you want to Process Another Sale (Y / N)?: ").upper()
        if Continue != "Y" and Continue != "N":
            print("Enter Y to Process Another Sale, or N to exit - Please re-enter.")
        else:
            break
    if Continue == "N":
        break

# Issues:
## The save_invoice_data will save the template claims for each invoice.
## This is not what would be wanted in a real scenario, rather to have the claims list start empty
## and add another function to save claims to an invoice (save_claims_to_invoice).

## Upon next time running will overwrite previous saved invoice files. This is due to the next policy no default
## variable not being updated in the python script. To fix could try to iterate through directory that contains invoices,
## get the everthing after the _ (Policy digits) and add one to this to properly specify the next ordered invoice.
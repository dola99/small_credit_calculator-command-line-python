import argparse
import math


parser = argparse.ArgumentParser()

parser.add_argument('--type=', help="type", type=str, dest="type", default=0)
parser.add_argument('--principal=', help="principal", type=int, dest="principal", default=0)
parser.add_argument('--periods=', help="periods", type=int, dest="periods", default=0)
parser.add_argument('--interest=', help="interest", type=float, dest="interest", default=0.0)
parser.add_argument('--payment', help='payment', type=int, default=0)
args = parser.parse_args()
new_list = []
i = args.interest / (12 * 100)

if args.type == "diff":
    if args.principal <= 0 or args.periods <= 0 or args.interest <= 0:
        print("Incorrect parameters")
    elif args.payment > 0:
        print("Incorrect parameters")
    else:
        for t in range(args.periods + 1):
            if t == 0:
                pass
            else:
                month = args.principal / args.periods + i * (args.principal - (args.principal * (t - 1)) / args.periods)
                if int(month) == month:
                    new_list.append(int(month))
                    print(f"Month {t}: paid out {int(month)}")
                else:
                    month = month + 1
                    new_list.append(int(month))
                    print(f"Month {t}: paid out {int(month)}")
        print(f"Overpayment = {sum(new_list) - args.principal}")
elif args.type == "annuity":
    if args.payment == 0 and args.principal == 0:
        print("Incorrect parameters")
    elif args.payment == 0 and args.periods == 0:
        print("Incorrect parameters")
    elif args.interest == 0:
        print("Incorrect parameters")
    elif args.payment == 0:
        calculated = args.principal * (
                i * math.pow(1 + i, args.periods) / (math.pow(1 + i, args.periods) - 1))
        if calculated is int:
            print(f"Your annuity payment = {int(calculated)}!")
            print(f"Overpayment {int((calculated * args.periods) - args.principal) - 3}!")
        else:
            calculated = calculated + 1
            print(f"Your annuity payment = {int(calculated)}!")
            print(f"Overpayment {int((calculated * args.periods) - args.principal) - 3}!")
    elif args.periods == 0:
        calculated = math.log(args.payment / (args.payment - (i * args.principal)), i + 1)
        calculated = calculated / 12
        year, month = str(calculated).split('.')
        if int(month[0]) == 9:
            new_year = int(year) + 1
            print(f"You need {new_year} year to repay this credit")
            print("Overpayment = " + str(args.payment * (int(new_year) * 12) - args.principal))
        elif int(year) > 0 and int(month) == 0:
            print(f"You need {year} year to repay this credit")
            print("Overpayment = " + str(args.payment * (int(year) * 12) - args.principal))
        elif int(year) < 0 and int(month) > 0:
            if month[1] > 0:
                month[0] = int(month[0]) + 1
            else:
                pass
            print(f"You need {month[0]} months to repay this credit")
            print("Overpayment = " + str(args.payment * month[0]) - args.principal)
        else:
            if int(month[1]) > 0:
                month2 = int(month[0]) + 1
                if int(month[2]) >= 6:
                    month2 = month2 + 1
            print(f"You need {year} years and {month2} months to repay this credit")
            new_month = int(year) * 12 + int(month2)
            new_month = args.payment * new_month
            print("Overpayment=" + str(new_month - int(args.principal)))
    elif args.payment != 0:
        args.principal = args.payment / (
                (i * math.pow(1 + i, args.periods)) / (math.pow(1 + i, args.periods) - 1))
        print(f"Your credit principal = {int(args.principal)}!")
        print(f"Overpayment {(args.payment * args.periods) - int(args.principal)}")
elif args.type == 0:
    print("Incorrect parameters")


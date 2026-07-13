"""
------------------------------------------------------------
Program Name : Age Calculator
Description : Calculates the exact age in years, months, days, total months, and total days using the user's date of birth.
------------------------------------------------------------
"""

from datetime import date


def calculate_age(birth_date):
    """Returns age in years, months, and days."""
    today = date.today()

    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust days if negative
    if days < 0:
        if today.month == 1:
            previous_month = 12
            previous_year = today.year - 1
        else:
            previous_month = today.month - 1
            previous_year = today.year

        days_in_previous_month = (
            date(today.year, today.month, 1) -
            date(previous_year, previous_month, 1)
        ).days

        days += days_in_previous_month
        months -= 1

    # Adjust months if negative
    if months < 0:
        months += 12
        years -= 1

    return years, months, days


def total_months(birth_date):
    """Returns total completed months lived."""
    today = date.today()

    months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)

    if today.day < birth_date.day:
        months -= 1

    return months


def main():
    print("=" * 50)
    print("               AGE CALCULATOR")
    print("=" * 50)

    name = input("Enter your name: ")

    print("\nEnter your Date of Birth")
    year = int(input("Year  (YYYY): "))
    month = int(input("Month (1-12): "))
    day = int(input("Day   (1-31): "))

    try:
        birth_date = date(year, month, day)
    except ValueError:
        print("\nInvalid date entered!")
        return

    today = date.today()

    if birth_date > today:
        print("\nDate of birth cannot be in the future.")
        return

    years, months, days = calculate_age(birth_date)

    total_days = (today - birth_date).days
    completed_months = total_months(birth_date)

    print("\n" + "=" * 50)
    print(f"Name           : {name}")
    print(f"Date of Birth  : {birth_date.strftime('%d-%m-%Y')}")
    print(f"Today's Date   : {today.strftime('%d-%m-%Y')}")
    print("-" * 50)
    print(f"Exact Age      : {years} Years, {months} Months, {days} Days")
    print(f"Total Months   : {completed_months}")
    print(f"Total Days     : {total_days}")
    print("=" * 50)


if __name__ == "__main__":
    main()

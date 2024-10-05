def split_wise():
    print("Welcome To Expensive Calculator OF 3 Friends")
    try:
        total = float(input("What was the total Amount: "))
    except ValueError:
        print("No Number Detected. Please enter a valid number.")
        exit()
    each = round(total / 3)
    print(f"Everyone has to pay: {each}")

    friend_1 = input("Enter Your 1st Friend Name ")
    friend_2 = input("Enter Your 2nd Friend Name ")
    friend_3 = input("Enter Your 3rd Friend Name ")

    friend_1_paid = float(input(f"How much did {friend_1} pay? "))  # e.g., 10
    friend_2_paid = float(input(f"How much did {friend_2} pay? "))  # e.g., 0
    friend_3_paid = float(input(f"How much did {friend_3} pay? "))  # e.g., 5

    outcome_1 = each - friend_1_paid  # Positive means owed, negative means overpaid
    outcome_2 = each - friend_2_paid
    outcome_3 = each - friend_3_paid

    print("\n--- Settlement Summary ---")

    for i, (friend, outcome) in enumerate(zip([friend_1, friend_2, friend_3], [outcome_1, outcome_2, outcome_3])):
        if outcome > 0:
            print(f"{friend} owes: {outcome:.2f}")
        elif outcome < 0:
            print(f"{friend} is owed: {-outcome:.2f}")
        else:
            print(f"{friend} has settled (no balance)")


split_wise()
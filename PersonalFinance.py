# AI Personal Finance Advisor

income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))

savings = income - expenses

print("\n----- Financial Report -----")
print("Income:", income)
print("Expenses:", expenses)
print("Savings:", savings)

if savings > income * 0.2:
    print("Advice: Excellent! You are saving well.")
elif savings > 0:
    print("Advice: Try to reduce expenses and increase savings.")
else:
    print("Advice: Your expenses exceed your income. Reduce spending.")

# Budget Recommendation
food = income * 0.30
rent = income * 0.40
savings_goal = income * 0.20
other = income * 0.10

print("\nSuggested Budget:")
print("Food:", food)
print("Rent:", rent)
print("Savings:", savings_goal)
print("Other:", other)
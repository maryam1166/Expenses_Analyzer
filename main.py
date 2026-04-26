import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_excel(r"C:\Users\My Computer\Desktop\vS codes\Finance_Analyzer\EXPENSE.xlsx")


file ="C:/Users/My Computer/Desktop/vS codes/Finance_Analyzer/EXPENSE.xlsx"

sheet1 = pd.read_excel(file, sheet_name="Transactions")
sheet2 = pd.read_excel(file, sheet_name="Budget")

# print(sheet1)
# print(sheet2)

# Summing up all the expenses from the Transactions sheet 
amount=sheet1['Amount'].sum()
print ("Total expenditure =",amount)
# Summing up the allocated budget from the Budget sheet 
budget=sheet2["amount"].sum()
print( "Total Budget=",budget)
# Calculating the savings
saving=budget-amount
print("Total savings =", saving)
percent_savings=(saving/budget)*100
print (percent_savings)
# Accessing the Amount column from the transaction sheet and converting it all to integer/float
sheet1["Amount"] = pd.to_numeric(sheet1["Amount"], errors="coerce")
# Summing up the actual expenditure per cateogory
actual = sheet1.groupby("Category")["Amount"].sum()
print(actual)
# Accessing the amount column from the transaction sheet and converting it all to integer/float
sheet2["amount"] = pd.to_numeric(sheet2["amount"], errors="coerce")
# Summing up the allocated budget per cateogory
actual2 = sheet2.groupby("Category")["amount"].sum()
print(actual2)
# creating a dataframe in which actual expenditure and allocated budget being alloted per category are being compared
comparison = pd.DataFrame({
    "Budget": actual2,
    "Actual": actual
}).fillna(0)
comparison.plot(kind="bar")
# Adding a difference column to get an idea of how much cash difference is occuring
comparison["Difference"] = comparison["Budget"] - comparison["Actual"]
# print(comparison)
# Checking the status per category to know where the expenditure is exceeding the alloted budget 
comparison["Status"] = comparison["Difference"].apply(lambda x: "Under Budget" if x >= 0 else "Over Budget")
print(comparison)
# plotting a comparison bar sheet 
plt.title("Budget vs Actual Spending")
plt.xlabel("Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
print("graph plotted")
import matplotlib.pyplot as plt

# Dataset
months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales = [100, 150, 130, 180, 220]

departments = ["IT", "HR", "Sales", "Finance"]
employees = [15, 10, 20, 12]

marks = [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

hours = [1, 2, 3, 4, 5, 6, 7]
scores = [30, 40, 45, 55, 65, 75, 90]

# 1. Line chart
plt.figure()
plt.plot(months, sales, label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()

# 2. Bar chart
plt.figure()
plt.bar(departments, employees, label="Employees")
plt.title("Employees by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.legend()

# 3. Histogram
plt.figure()
plt.hist(marks, bins=5)
plt.title("Distribution of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

# 4. Scatter plot
plt.figure()
plt.scatter(hours, scores)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.show()
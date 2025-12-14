# bar chart 
import matplotlib.pyplot as plt

# name=["kanak","manthan","vaibhav","guru"]
# marks=[40,40,12,35]

# plt.bar(name,marks)
# plt.xlabel("students")
# plt.ylabel("marks")
# plt.title("students marks bar chart")
# plt.show()

# pie cahrt
subject=["python","php","coa","maths"]
marks=[35,20,15,30]

plt.pie(marks,labels=subject,autopct='%1.1f%%',startangle=90)
plt.title("subject marks pie chart")
plt.axis("equal")
plt.show()
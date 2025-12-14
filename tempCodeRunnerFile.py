subject=["python","php","coa","maths"]
marks=[35,20,15,30]

plt.pie(marks,labels=subject,autopct='%1.1f%%',startangle=90)
plt.title("subject marks pie chart")
plt.axis("equal")
plt.show()
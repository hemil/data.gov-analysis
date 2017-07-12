# %matplotlib inline
import matplotlib.pyplot as plt

import pandas as pd

pd.set_option("display.mpl_style", "default")  # Make the graphs a bit prettier
# plt.rcParams["figure.figsize"] = (15, 5)

hostel_csv = pd.read_csv("source_files/hostel_info_2015-16.csv")

# print hostel_csv["name"][:3]
total_girls_intake = 0
total_boys_intake = 0

total_girls_capacity = 0
total_boys_capacity = 0

for row in hostel_csv.itertuples():
    if row.type == "Girls Hostel":
        total_girls_intake += row.students_residing
        total_girls_capacity += row.intake_capacity
    elif row.type == "Boys Hostel":
        total_boys_intake += row.students_residing
        total_boys_capacity += row.intake_capacity

print "Women: {intake}/{capacity}".format(intake=total_girls_intake, capacity=total_girls_capacity)
print "Men: {intake}/{capacity}".format(intake=total_boys_intake, capacity=total_boys_capacity)
print "Total: {intake}/{capacity}".format(intake=total_girls_intake + total_boys_intake,
                                          capacity=total_girls_capacity + total_boys_capacity)
# Save a chart
labels = "Men", "Women"
sizes = [total_boys_capacity-total_boys_intake, total_girls_capacity-total_girls_intake]
colors = ["lightskyblue", "lightcoral"]
explode = (0, 0)
patches = plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True, startangle=90)
plt.legend(patches, labels, loc="best")
plt.axis("equal")
plt.title("Hostel Empty Rooms by Gender 2015")
plt.savefig("analysis_files/Hostel Empty Rooms by Gender 2015.jpg")

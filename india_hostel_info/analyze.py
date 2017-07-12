# %matplotlib inline
import matplotlib.pyplot as plt

import pandas as pd

pd.set_option("display.mpl_style", "default")  # Make the graphs a bit prettier


def create_pie_char(labels, chart_values, chart_title, output_file_name):
    colors = ["lightskyblue", "lightcoral"]
    explode = (0, 0)
    patches = plt.pie(chart_values, explode=explode, labels=labels, colors=colors, autopct="%1.1f%%", shadow=True,
                      startangle=90)
    plt.legend(patches, labels, loc="best")
    plt.axis("equal")
    plt.title(chart_title)
    plt.savefig("analysis_files/{output_file_name}".format(output_file_name=output_file_name))

standalone_hostel_csv = pd.read_csv("source_files/hostel_info_standalone_2015-16.csv")
colleges_hostel_csv = pd.read_csv("source_files/hostel_info_colleges_2015-16.csv")
universities_hostel_csv = pd.read_csv("source_files/hostel_info_universities_2015-16.csv")

# print hostel_csv["name"][:3]
total_girls_intake = 0
total_boys_intake = 0

total_girls_capacity = 0
total_boys_capacity = 0

for row in colleges_hostel_csv.itertuples():
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


# Capacity by Gender
# Intake by Gender
# Empty Rooms by Gender
chart_title = "Hostel Empty Rooms by Gender 2015"
output_file_name = "Hostel Empty Rooms by Gender 2015.jpg"
chart_values = [total_boys_capacity-total_boys_intake, total_girls_capacity-total_girls_intake]
labels = "Men", "Women"
# Room Occupancy Men
# Room Occupancy Women
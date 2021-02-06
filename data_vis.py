
from matplotlib import pyplot as plt
from prettytable import PrettyTable

###########
#HISTOGRAM#
###########

# values on the y axis
y = [14, 3, 6, 9]

# plotting histogram
plt.hist(y)

# showing plot
plt.show()

##########
#BAR PLOT#
##########

# values on the x axis
x = [5, 2, 9, 4, 7]

# values on the y axis
y = [14, 3, 6, 9, 1]

# plotting bar
plt.bar(x, y)

# showing plot
plt.show()

###########
#LINE PLOT#
###########

# values on the x axis
x = [5, 2, 9, 4, 7]

# values on the y axis
y = [14, 3, 6, 9, 1]

# plotting line
plt.plot(x, y)

# showing plot
plt.show()

###########
#PIE CHART#
###########

# The labels are the names for the parts
label_set = '7', '6', '8+', '5-'

# we give each label a size
sizes = [20, 45, 15, 20]

# we use explode to show a particular slide
explode = (0, 0, 0, 0.1)

# subplots
fig1, ax1 = plt.subplots()

ax1.pie(sizes, explode=explode, labels=label_set,
        autopct='%1.1f%%', shadow=True, startangle=90)

# make sure its a circle
ax1.axis('equal')

# show the plot
plt.show()

#############
#Prettytable#
#############

# specifying column names
mytable = PrettyTable(["Student Name", "Class", "Section", "Percentage"])

# adding rows
mytable.add_row(["Serra", "X", "B", "91.2%"])
mytable.add_row(["Penny", "B", "C", "61.2%"])
mytable.add_row(["Erik", "B", "B", "90.2%"])
mytable.add_row(["Josso", "X", "A+", "100%"])
mytable.add_row(["Luka", "X", "B", "88.1%"])

# output
print(mytable)

# the following section is for testing better comments
# TODO: Implement x and y
# ? This is a query
# * this is hightlighted, way better then the stupid plain default comments
# ! this is very important

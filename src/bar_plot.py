import matplotlib.pyplot as plt

# Given list
data = [74, 77.2, 82, 69, 64.8, 71, 86.4, 88]

# Define colors for each bar
colors = ['cyan', 'pink', 'purple', 'orange', 'green', 'blue', 'brown', 'red']

ytick_labels = ['BUS', 'Bustle', 'BEE', 'Crossbeam', 'Approach-1 (avg)', 'Approach-1 (unions)', 'Approach-2 (avg)', 'Approach-2 (unions)']

# Define custom labels to be placed next to each bar
labels = [r'$21 \times 10^8$', r'$20 \times 10^7$', r'$23 \times 10^8$', r'$5 \times 10^4$', '', '', '', '']

# Create a horizontal bar plot with different colors
plt.barh(range(len(data)), data, color=colors)

# Adding labels, title, and custom y-axis tick labels
plt.xlabel('Number of Correct Programs')
plt.ylabel('Approach')
plt.title('Our Approaches vs. Others')
plt.yticks(range(len(data)), ytick_labels)

for i, value in enumerate(data):
    plt.text(value, i, f' {labels[i]}', va='center', fontsize=9, color='black', rotation=30)

# Show the plot
plt.show()
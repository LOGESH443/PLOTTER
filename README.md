# PLOTTER
Developed an interactive plotter using Python, leveraging Matplotlib for data visualization and Streamlit for building a responsive web-based user interface.
Implemented features to allow users to upload datasets, dynamically generate plots (line, bar, scatter, etc.), and customize chart parameters (axes, labels, colors, legends).
Integrated real-time data rendering, enabling users to interactively adjust plot attributes through an intuitive interface.

Features:
1) Line Plot – Customize line color and marker styles.
2) Bar Chart – Customize bar width.
3) Scatter Plot – Customize color and marker style.
4) Pie Chart – Visualize data in pie chart form with labels and percentages.
5) Violin Plot – Display the distribution of data across different levels.
6) Box Plot – Summarize data using quartiles and visualize outliers.
7) Gantt Chart (Horizontal Bar) – Visualize task schedules using start times and durations.

Error Handling:
The app includes built-in error handling to ensure users input valid data. For example:
 - X and Y values must have the same length.
 - If invalid inputs are provided, the app prompts the user to re-enter the values.

Plot Customizations:
 - For each plot type, users can input custom attributes like color, marker style, or bar width to tailor the plots to their preferences.

How to Use:
1) The user selects a plot type from the menu (1-7).
2) They input the X and Y values.
3) Optionally, they can provide custom labels for the plot title, X-axis, and Y-axis.
4) The user can also choose specific customizations like colors, markers, or bar width depending on the type of plot.
5) The graph is generated and displayed interactively.

# Plotter_App
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Function to get user input for x and y values
def get_data():
    x_values = st.text_input("Enter X values (space-separated):", "1 2 3 4 5")
    y_values = st.text_input("Enter Y values (space-separated):", "10 20 30 40 50")
    x_values = [float(x) for x in x_values.split()]
    y_values = [float(y) for y in y_values.split()]
    return x_values, y_values

# Function to generate different plots
def plot_data(plot_type, x_values, y_values):
    fig, ax = plt.subplots()

    if plot_type == 'Line Plot':
        ax.plot(x_values, y_values, marker='o')
        ax.set_title('Line Plot')
    elif plot_type == 'Bar Chart':
        ax.bar(x_values, y_values)
        ax.set_title('Bar Chart')
    elif plot_type == 'Scatter Plot':
        ax.scatter(x_values, y_values)
        ax.set_title('Scatter Plot')
    elif plot_type == 'Pie Chart':
        fig, ax = plt.subplots()
        ax.pie(y_values, labels=x_values, autopct='%1.1f%%')
        ax.set_title('Pie Chart')
    elif plot_type == 'Violin Plot':
        data = [y_values]  # Violin plots expect a 2D array
        ax.violinplot(data)
        ax.set_title('Violin Plot')
    elif plot_type == 'Box Plot':
        ax.boxplot(y_values, vert=False)
        ax.set_title('Box Plot')
    elif plot_type == 'Gantt Chart':
        ax.broken_barh([(x_values[i], y_values[i]) for i in range(len(x_values))], (10, 9))
        ax.set_ylim(5, 35)
        ax.set_xlim(min(x_values), max(x_values) + max(y_values))
        ax.set_xlabel('Time')
        ax.set_ylabel('Task')
        ax.set_yticks([15])
        ax.set_yticklabels(['Task'])
        ax.set_title('Gantt Chart')
    else:
        st.error("Invalid plot type")

    st.pyplot(fig)

# Main program
def main():
    st.title("Plot Generator")

    # Sidebar for selecting plot type
    plot_type = st.sidebar.selectbox("Choose a plot type:", 
                                     ["Line Plot", "Bar Chart", "Scatter Plot", "Pie Chart", "Violin Plot", "Box Plot", "Gantt Chart"])

    # Get the data to plot
    st.write(f"You selected: {plot_type}")

    if plot_type == 'Pie Chart':
        st.info("For Pie Chart, X values will be treated as labels and Y values as sizes.")
    
    x_values, y_values = get_data()

    # Generate the selected plot
    if len(x_values) == len(y_values):
        plot_data(plot_type, x_values, y_values)
    else:
        st.error("X and Y values must have the same length!")

if __name__ == "__main__":
    main()

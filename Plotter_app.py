# Plotter_App


import matplotlib.pyplot as plt

# Data Sets

def data():
    try:
        x_values = list(map(float, input("Enter X values (space-separated): ").split()))
        y_values = list(map(float, input("Enter Y values (space-separated): ").split()))
        
        if len(x_values) != len(y_values):
            raise ValueError("X and Y values must have the same length.")

        return x_values, y_values
    except ValueError as e:
        print(f"Error: {e}")
        return data()

# Labels
def labels():
    try:
        t = input("Enter the title of the graph: ")
        x = input("Enter X-axis label: ")
        y = input("Enter Y-axis label: ")
        return t, x, y
    except Exception as e:
        print(f"Error: {e}")
        return labels()

# Customizations
def plot_customizations(plot_type):
    customizations = {}
    
    if plot_type in ['1', '3']:  # Line and scatter plot
        customizations['color'] = input("Enter line color (e.g., 'r', 'g', 'b', etc.): ")
        customizations['marker'] = input("Enter marker style (e.g., 'o', 's', 'x', etc.): ")
    elif plot_type == '2':  # Bar chart
        customizations['bar_width'] = float(input("Enter bar width (default is 0.8): "))
    
    return customizations

# Graph Functions
def plot_data(plot_type):
    try:
        plt.figure()
        x_values, y_values = data()
        t, x, y = labels()
        customizations = plot_customizations(plot_type)

        if plot_type == '1':  # Line plot
            plt.plot(x_values, y_values, marker=customizations.get('marker', 'o'), color=customizations.get('color', 'b'))
            plt.title(t)
            plt.xlabel(x)
            plt.ylabel(y)
        elif plot_type == '2':  # Bar chart
            plt.bar(x_values, y_values, width=customizations.get('bar_width', 0.8))
            plt.title(t)
            plt.xlabel(x)
            plt.ylabel(y)
        elif plot_type == '3':  # Scatter plot
            plt.scatter(x_values, y_values, marker=customizations.get('marker', 'o'), color=customizations.get('color', 'b'))
            plt.title(t)
            plt.xlabel(x)
            plt.ylabel(y)
        elif plot_type == '4':  # Pie chart
            plt.pie(y_values, labels=x_values, autopct='%1.1f%%')
            plt.title(t)
        elif plot_type == '5':  # Violin plot
            plt.violinplot([y_values])
            plt.title(t)
            plt.xlabel(x)
            plt.ylabel(y)
        elif plot_type == '6':  # Box plot
            plt.boxplot(y_values, vert=False)
            plt.title(t)
            plt.xlabel(x)
            plt.ylabel(y)
        elif plot_type == '7':  # Gantt chart (Horizontal bar)
            fig, ax = plt.subplots()
            ax.broken_barh([(x_values[i], y_values[i]) for i in range(len(x_values))], (10, 9))
            ax.set_ylim(5, 35)
            ax.set_xlim(min(x_values), max(x_values) + max(y_values))
            ax.set_xlabel('Time')
            ax.set_ylabel('Task')
            ax.set_yticks([15])
            ax.set_yticklabels(['Task'])
            plt.title(t)
        else:
            raise ValueError("Invalid plot type selected.")

        if plot_type != '4':  # Pie chart doesn't need axis labels
            plt.grid(True)

        plt.show()

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Main function
def main():
    print("Choose a plot type:")
    print("1. Line Plot")
    print("2. Bar Chart")
    print("3. Scatter Plot")
    print("4. Pie Chart")
    print("5. Violin Plot")
    print("6. Box Plot")
    print("7. Gantt Chart (Horizontal Bar)")

    plot_type = input("Enter the number corresponding to the plot type: ")

    if plot_type not in ['1', '2', '3', '4', '5', '6', '7']:
        print("Invalid selection. Please choose a valid plot type.")
    else:
        if plot_type == '4':
            print("For Pie Chart, X values are labels and Y values are sizes.")

        # Generate the selected plot
        plot_data(plot_type)

if __name__ == "__main__":
    main()

def plot_interactive(ax: plt.Axes, x: list, y: list, title: str, xlabel: str, ylabel: str):

    # Create a line plot with a trend
    ax.scatter(x, y)
    sns.regplot(x = x, y = y, scatter = False, ax = ax)
   
    # Set the title and the labels for the axis
    ax.set_title(title, fontsize = 12)
    ax.set_xlabel(xlabel, fontsize = 12)
    ax.set_ylabel(ylabel, fontsize = 12)
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

if __name__ == '__main__':
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    # ==========================================================================================
    # Global API
    x = np.arange(-10, 11)
    plt.figure(figsize=(12, 6))
    plt.plot(x, x ** 2)
    plt.plot(x, -1 * (x ** 2))
    plt.title('My nice plot')
    plt.legend(['y = x^2', 'y = -x^2'])
    plt.show()

    # ==========================================================================================
    plt.figure(figsize=(12, 6))
    plt.title('My Nice Plot')

    plt.subplot(1, 2, 1)  # rows, columns, panel selected
    plt.plot(x, x ** 2)
    plt.plot([0, 0, 0], [-10, 0, 100])
    plt.legend(['X^2', 'Vertical Line'])
    plt.xlabel('X')
    plt.ylabel('X Squared')

    plt.subplot(1, 2, 2)
    plt.plot(x, -1 * (x ** 2))
    plt.plot([-10, 0, 10], [-50, -50, -50])
    plt.legend(['-X^2', 'Horizontal Line'])

    plt.xlabel('X')
    plt.ylabel('X Squared')
    plt.show()

    # ==========================================================================================
    fig, axes = plt.subplots(figsize=(12, 6))
    axes.plot(
        x, (x ** 2), color='red', linewidth=3,
        marker='o', markersize=8, label='X^2')

    axes.plot(x, -1 * (x ** 2), 'b--', label='-X^2')

    axes.set_xlabel('X')
    axes.set_ylabel('X Squared')

    axes.set_title("My Nice Plot")
    axes.legend()

    plt.show()

    # ==========================================================================================
    fig, axes = plt.subplots(figsize=(12, 6))

    axes.plot(x, x + 0, linestyle='solid', label='solid')
    axes.plot(x, x + 1, linestyle='dashed', label='dashed')
    axes.plot(x, x + 2, linestyle='dashdot', label='dash')
    axes.plot(x, x + 3, linestyle='dotted', label='dotted')

    axes.set_title("My Nice Plot")
    axes.legend()

    plt.show()

    # ==========================================================================================
    print('Markers: {}'.format([m for m in plt.Line2D.markers]))

    line_styles = ['_', '-', '--', ':']

    print('Line styles: {}'.format(line_styles))

    # ==========================================================================================
    # Other types of plots
    plot_objects = plt.subplots()

    fig, ax = plot_objects

    ax.plot([1, 2, 3], [1, 2, 3])
    plt.show()

    # ==========================================================================================
    plot_objects = plt.subplots(nrows=2, ncols=2, figsize=(14, 6))

    fig, ((ax1, ax2), (ax3, ax4)) = plot_objects

    ax4.plot(np.random.randn(50), c='yellow', label='Yellow')
    ax1.plot(np.random.randn(50), c='red', linestyle='--', label='Dashed')
    ax2.plot(np.random.randn(50), c='green', linestyle=':', label='Dotted')
    ax3.plot(np.random.randn(50), c='blue', marker='o', linewidth=3.0, label='Thick')

    ax1.legend()
    ax2.legend()
    ax3.legend()
    ax4.legend()

    plt.show()

    # ==========================================================================================
    # Scatter plot
    N = 50
    x = np.random.rand(N)
    y = np.random.rand(N)
    colors = np.random.rand(N)
    area = np.pi * (20 * np.random.rand(N)) ** 2  # 0 to 15 point radii
    plt.figure(figsize=(14, 6))

    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Spectral', edgecolors='black')
    plt.colorbar()

    plt.show()

    # ==========================================================================================
    fig = plt.figure(figsize=(14, 6))

    ax1 = fig.add_subplot(1, 2, 1)
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel1')
    plt.colorbar()

    ax2 = fig.add_subplot(1, 2, 2)
    plt.scatter(x, y, s=area, c=colors, alpha=0.5, cmap='Pastel2')
    plt.colorbar()

    plt.show()

    fig.savefig('hist.png')

    # ==========================================================================================
    # Histogram
    values = np.random.randn(1000)
    plt.subplots(figsize=(12, 6))

    plt.hist(values, bins=100, alpha=0.8,
             histtype='bar', color='steelblue',
             edgecolor='green')
    plt.xlim(xmin=-5, xmax=5)

    plt.show()

    # ==========================================================================================
    # KDE (Kernel Density Estimation)
    from scipy import stats

    density = stats.kde.gaussian_kde(values)

    plt.subplots(figsize=(12, 6))

    values2 = np.linspace(min(values) - 10, max(values) + 10, 100)

    plt.plot(values2, density(values2), color='#FF7F00')
    plt.fill_between(values2, 0, density(values2), alpha=0.5, color='#FF7F00')
    plt.xlim(xmin=-5, xmax=5)

    plt.show()

    # Combine plots
    plt.subplots(figsize=(12, 6))

    plt.hist(values, bins=100, alpha=0.8, density=True,
             histtype='bar', color='steelblue',
             edgecolor='green')

    plt.plot(values2, density(values2), color='#FF7F00', linewidth=3.0)
    plt.xlim(xmin=-5, xmax=5)

    plt.show()

    # ==========================================================================================
    # Bar plots
    Y = np.random.rand(1, 5)[0]
    Y2 = np.random.rand(1, 5)[0]

    plt.figure(figsize=(12, 4))

    barWidth = 0.5
    plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894')

    plt.show()

    # ==========================================================================================
    plt.figure(figsize=(12, 4))

    barWidth = 0.5
    plt.bar(np.arange(len(Y)), Y, width=barWidth, color='#00b894', label='Label Y')
    plt.bar(np.arange(len(Y2)), Y2, width=barWidth, color='#e17055', bottom=Y, label='Label Y2')

    plt.legend()
    plt.show()

    # Box plots and outlier detection
    values3 = np.concatenate([np.random.randn(10), np.array([10, 15, -10, -15])])

    plt.figure(figsize=(12, 4))

    plt.hist(values3)
    plt.legend(['Values'])
    plt.show()

    # ==========================================================================================
    plt.figure(figsize=(12, 4))

    plt.boxplot(values3)
    plt.show()

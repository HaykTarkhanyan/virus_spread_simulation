import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons

# Make code DRY in future, perhaps never though


def growth_rate(ls):
    """
    Function takes an input of data per day and returns a list
    containing change between values per day
    """
    growth = [max(0, ls[i + 1] - ls[i]) for i in range(len(ls) - 1)]
    return growth


def plot_data(inf, dead, recovered, start_emergency=7,
              start_deepening=1, start_recovering=10,
              vir_sev=0.3, inf_chance=0.5, markers=["", "."], linestyle="-"):
    """
    Function plots everyday stats, as well growth statistic on the linear scale
    """
    day_num = list(range(1, len(dead) + 1))

    fig_1, ax_1 = plt.subplots()

    plt.xlabel('Day number')
    plt.ylabel('Num people')

    plt.title(f'Virus severeness - {vir_sev}, inf_chance - {inf_chance}')

    inf_1, = ax_1.plot(
        day_num, inf, markers[0] + linestyle + "r", lw=2, label='infected')
    dead_1, = ax_1.plot(
        day_num, dead, markers[0] + linestyle + "k", lw=2, label='dead')
    rec_1, = ax_1.plot(day_num, recovered,
                       markers[0] + linestyle + "b", lw=2, label='Recovered')

    ax_1.plot([start_emergency] * 2, [0, max(dead + inf + recovered)], "--r",
              alpha=0.5, label="Emergency time!")

    ax_1.plot([start_recovering] * 2, [0, max(dead + inf + recovered)], "--b",
              alpha=0.5, label="Hospitalization time!")

    ax_1.plot([start_deepening] * 2, [0, max(dead + inf + recovered)], "--k",
              alpha=0.5, label="Deepening time")

    lines_1 = [inf_1, dead_1, rec_1]

    major_xticks_1 = np.arange(0, len(dead) + 1, max(1, len(dead) // 10))
    minor_xticks_1 = np.arange(0, len(dead) + 1, max(1, len(dead) // 20))
    major_yticks_1 = np.arange(0, max(dead + inf + recovered) + 1,
                               max(1, max(dead + inf + recovered) // 10))
    minor_yticks_1 = np.arange(0, max(dead + inf + recovered) + 1,
                               max(1, max(dead + inf + recovered) // 20))

    ax_1.set_xticks(major_xticks_1)
    ax_1.set_xticks(minor_xticks_1, minor=True)
    ax_1.set_yticks(major_yticks_1)
    ax_1.set_yticks(minor_yticks_1, minor=True)

    ax_1.grid(linestyle=":", which="minor")
    ax_1.grid(linestyle="-", which="major")

    plt.legend(ncol=2, title="Who's who")

    rax = plt.axes([0.05, 0.4, 0.1, 0.15])
    labels_1 = [str(line.get_label()) for line in lines_1]

    visibility_1 = [line.get_visible() for line in lines_1]
    check_1 = CheckButtons(rax, labels_1, visibility_1)

    def func_1(label):
        index = labels_1.index(label)

        lines_1[index].set_visible(not lines_1[index].get_visible())
        plt.draw()

    check_1.on_clicked(func_1)

    plt.savefig(os.path.join(os.getcwd(), "stats.png"))

    fig_2, ax_2 = plt.subplots()
    del day_num[-1]

    # rewriting inf, dead and recovered with their growth values
    inf = growth_rate(inf)
    dead = growth_rate(dead)
    recovered = growth_rate(recovered)

    plt.xlabel('Day number')
    plt.ylabel('Num people')

    plt.title(f'Virus severeness - {vir_sev}, inf_chance - {inf_chance}')

    inf_2, = ax_2.plot(
        day_num, inf, markers[1] + linestyle + "r", lw=2, label='infected')
    dead_2, = ax_2.plot(
        day_num, dead, markers[1] + linestyle + "k", lw=2, label='dead')
    rec_2, = ax_2.plot(day_num, recovered,
                       markers[1] + linestyle + "b", lw=2, label='Recovered')

    ax_2.plot([start_emergency] * 2, [0, max(dead + inf + recovered)], "--r",
              alpha=0.5, label="Emergency time!")

    ax_2.plot([start_recovering] * 2, [0, max(dead + inf + recovered)], "--b",
              alpha=0.5, label="Hospitalization time!")

    ax_2.plot([start_deepening] * 2, [0, max(dead + inf + recovered)], "--k",
              alpha=0.5, label="Deepening time")

    lines_2 = [inf_2, dead_2, rec_2]

    major_xticks_2 = np.arange(0, len(dead) + 1, max(1, len(dead) // 10))
    minor_xticks_2 = np.arange(0, len(dead) + 1, max(1, len(dead) // 20))
    major_yticks_2 = np.arange(0, max(dead + inf + recovered) + 1,
                               max(1, max(dead + inf + recovered) // 10))
    minor_yticks_2 = np.arange(0, max(dead + inf + recovered) + 1,
                               max(1, max(dead + inf + recovered) // 20))

    ax_2.set_xticks(major_xticks_2)
    ax_2.set_xticks(minor_xticks_2, minor=True)
    ax_2.set_yticks(major_yticks_2)
    ax_2.set_yticks(minor_yticks_2, minor=True)

    ax_2.grid(linestyle=":", which="minor")
    ax_2.grid(linestyle="-", which="major")

    plt.legend(ncol=2, title="Who's who")

    rax = plt.axes([0.05, 0.4, 0.1, 0.15])
    labels_2 = [str(line.get_label()) for line in lines_2]

    visibility_2 = [line.get_visible() for line in lines_2]
    check_2 = CheckButtons(rax, labels_2, visibility_2)

    def func_2(label):
        index = labels_2.index(label)

        lines_2[index].set_visible(not lines_2[index].get_visible())
        plt.draw()

    check_2.on_clicked(func_2)

    plt.savefig(os.path.join(os.getcwd(), "growth.png"))

    plt.show()

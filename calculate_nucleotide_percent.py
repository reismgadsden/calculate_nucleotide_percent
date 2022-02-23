"""
Calculate the total percents of nucleotides between
two sequences in order to compare two sequences.

author: Reis Gadsden
version: 23/02/22

class: CS-5531 @ Appalchian State University
instructor: Mohammad Mohebbi
"""
import os
import numpy as np
import matplotlib.pyplot as plt


def main():
    dir_path = ".\\sequences"
    dir_content = os.listdir(dir_path)

    container = []

    for x in dir_content:
        f = open(dir_path + "\\" + x, 'r')
        name, counts = calc_nucleotides(f)
        container.append([name, counts])
        f.close()

    generate_bar(container)




def calc_nucleotides(file) -> tuple:
    content = file.readlines()
    name = ""
    count = [0, 0, 0, 0]
    total_count = 0
    for line in content:
        if line[0] == '>':
            name = line[13:].replace(", complete genome", "")
            continue
        for x in line:
            if x.upper() == 'A':
                count[0] += 1
            elif x.upper() == 'C':
                count[1] += 1
            elif x.upper() == 'G':
                count[2] += 1
            elif x.upper() == 'T':
                count[3] += 1

            if x.upper() in "ACGT":
                total_count += 1

    for i in range(0, 4):
        count[i] = (count[i] / total_count) * 100

    return name, count



def generate_bar(container):
    fig, ax = plt.subplots()
    x = np.arange(len(container[0][1]))

    width = 0.7 / len(container[0][1])

    firstbar = ax.bar(x - width/2, container[0][1], width, label=container[0][0])
    secbar = ax.bar(x + width / 2, container[1][1], width, label=container[1][0])

    ax.set_ylabel("Nucleotide Occurence Percentage")
    ax.set_xticks(x, ['A', 'C', 'G', 'T'])
    ax.set_title(container[0][0] + " vs. " + container [1][0] + "Nucleotide Percentages")
    ax.legend()
    plt.xlabel("Nucleotides")

    ax.bar_label(firstbar, padding=3)
    ax.bar_label(secbar, padding=3)

    fig.tight_layout()

    plt.show()



if __name__ == "__main__":
    main()
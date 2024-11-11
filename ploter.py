import matplotlib.pyplot as plt

def change_for_floats(line: str):
    items = line.split(';')
    x = float(items[0])
    y = float(items[1])
    return x, y


def deduplicate_and_sort(dane):
    dupli_list = []
    for i in dane:
        dupli_list.append(change_for_floats(i))
    no_duplicates = list(set(dupli_list))
    no_duplicates.sort(key=lambda x: x[0])
    return no_duplicates


def plot_points(points):
    x = list(map(lambda x: x[0], points))
    y = list(map(lambda x: x[1], points))
    plt.scatter(x, y)
    plt.show()


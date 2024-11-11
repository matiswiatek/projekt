import argparse

from ploter import plot_points, deduplicate_and_sort

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='PLOTER',
        description='ploteruje',
        epilog='ploting')
    parser.add_argument('-i', '--input-file', help='input file', required=True)
    args = parser.parse_args()

    try:
        with open(args.input_file, 'r') as file:
            dane = file.readlines()
            points = deduplicate_and_sort(dane)
            plot_points(points)

    except FileNotFoundError:
        print('nie znaleziony')


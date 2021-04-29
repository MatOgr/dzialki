import os
import sys
import argparse
import xml.etree.ElementTree as ET


def retrieve_info(path_n_format):

    path, file_format = path_n_format
    print(f"\nFILE: {path.split('/')[-1]}\nFORMAT:{file_format}")
    labels_tree = ET.parse("format.xml")
    labels = labels_tree.find(file_format)
    if labels is None:
        print(f"No labels for format '{file_format}' - update the 'format.xml' file with sought labels")
        sys.exit()

    namespace = labels.attrib['namespace']

    data = ET.parse(path)
    if data is None:
        print("No data found in the given file - may be the 'format' is inappropriate?")
        sys.exit()
    data_root = data.getroot()

    print('############\tInformacje na temat działki\t############\n')
    for key in labels:
        node = data_root.findall(f'.//{namespace}{key.tag}')
        if len(node) == 0:
            print(f"Nie znaleziono informacji dla etykiety '{key.tag}'")
        for child in node:
            print(f'{key.text}:\t{child.text}')


if __name__ == '__main__':

    my_parser = argparse.ArgumentParser(usage='%(prog)s [option] path format',
                                        description='Retrieves information written in given format from xml file')
    my_parser.add_argument('Path',
                           metavar='path',
                           type=str,
                           help='the path to .xml file')
    my_parser.add_argument('Format',
                           metavar='format',
                           type=str,
                           help='the format in which data is written in .xml file')
    args = my_parser.parse_args()

    input_path = [args.Path, args.Format]

    if not os.path.isfile(input_path[0]):
        print('The file specified does not exist')
        sys.exit()

    retrieve_info(input_path)
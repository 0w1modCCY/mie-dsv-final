import argparse
import subprocess
import time

from data_logger import Logger as log
import features

def to_string(array):
    string = "" + array[0]
    array.pop(0)
    for node in array:
        string = ", " + node

class Node:
    def __init__(self, value, nodes):
        self.value = value
        self.nodes = nodes


def node_run(node):
    args = ['python3', 'node.py', '-v', str(node.value), '-n', str(to_string(node.nodes))]
    subprocess.Popen(args, stdout=subprocess.DEVNULL)


if __name__ == '__main__':

    # Getting parser and argument setup
    parser = argparse.ArgumentParser(description='Nodes manager.')
    parser.add_argument("-t", "--topology", type=str, help="Single topology")
    parser.add_argument("-f", "--file", type=str, help="File with topologies")
    parser.add_argument("-n", "--num", type=int, help="Max number of topologies")
    args = parser.parse_args()

    if (args.topology and args.file) or (not (args.topology) and not (args.file)):
        parser.error(
            "\nYou need to choose exactly one option: \n\t-t for single topology \n\t-f for file with topologies")

    topo = features.Parser()

    if args.topology:
        topo.topologies.put(args.topology)
    elif args.file:
        if args.num:
            topo.read_file(args.file, args.num)
        else:
            topo.read_file(args.file, 100)

    log.clear_all()

    num = 1
    while not (topo.topologies.empty()):
        print("Loading topology: " + str(num))
        nodes = topo.topologies.get().split(',')
        print("Topology size: " + str(len(nodes)) + " nodes")
        log.log_general_header(num, str(len(nodes)))

        start = time.time()

        for n in nodes:
            n = Node(n, nodes)
            node_run(n)

        end = time.time()

        print("Topology executed in: %.2f" % (end - start) + "s\n")
        log.log_general_bottom("%.2f" % (end - start) + "s\n")
        num = num + 1

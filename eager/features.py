from queue import Queue


class Parser:
    def __init__(self):
        self.topologies = Queue()

    def read_file(self, file, limit):
        with open(file, 'r') as f:
            lines = f.readlines()
            for i in range(min(limit, len(lines))):
                line = lines[i].replace('\n', '')
                self.topologies.put(line)
        return self.topologies

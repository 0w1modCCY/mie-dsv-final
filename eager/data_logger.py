import time


class Logger:
    @staticmethod
    def log_received(sender, receiver):
        with open("/log/received.txt", 'a') as f:
            t = time.asctime().split(" ")[3]
            f.write("<" + str(receiver) + "," + t + "," + str(sender) + "," + str(receiver) + ">\n")

    @staticmethod
    def log_sent(sender, receiver):
        with open("/log/sent.txt", 'a') as f:
            t = time.asctime().split(" ")[3]
            f.write("<" + str(sender) + "," + t + "," + str(sender) + "," + str(receiver) + ">\n")

    @staticmethod
    def log_finish(leader):
        with open("/log/general.txt", 'a') as f:
            f.write("Leader elected: " + str(leader) + "\n")

    @staticmethod
    def log_general_header(num, size):
        with open("/log/general.txt", 'a') as f:
            f.write("== Topology " + str(num) + " ==\n")
            f.write("Topology size: " + str(size) + "\n")

    @staticmethod
    def log_general_bottom(execution):
        with open("/log/general.txt", 'a') as f:
            f.write("Execution time: " + str(execution) + "\n")

    @staticmethod
    def clear(file):
        with open(file, 'w') as f:
            f.write("")

    @staticmethod
    def clear_all():
        Logger.clear("/log/general.txt")
        Logger.clear("/log/sent.txt")
        Logger.clear("/log/received.txt")


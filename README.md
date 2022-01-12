FIT CTU username = morenvic

# Table of Contents
1. [Project Description](#semester-project-solution-specification)
2. [Algorithm Description](#about-unidirectional-links-eager-leader-election-algorithm)
3. [Algorithm Example](#algorithm-example)

# Semester Project Solution Specification
- For the solution, the usage of **Google’s RPC (gRPC)** framework is required. 

- The fundamental **introduction** of it can be seen [here](https://courses.fit.cvut.cz/MIE-DSV/tutorials/files/tutorials-3.pdf). 

- The selected programming language for implementation depends on the author of the implementation.

- The solution can be implemented on a single virtual machine by using processes, but the **processes have to communicate with each other via gRPC**.

- The solution will contain an **initial process** which will start all communicating processes.

- At the program **start**, there will be passed a **single string value parameter from the command-line** representing the ring topology of the nodes with their IDs.

![Command line parameter: 22, 7, 15, 10, 8, 11, 24](https://courses.fit.cvut.cz/MIE-DSV/tutorials/files/Diagram1.png)

- The textual file containing the pregenerated ring topologies can be downloaded from [here](https://courses.fit.cvut.cz/MIE-DSV/tutorials/files/topologies.txt)

- The algorithm simulation has to contain a **log file** containing the overview of **sent and received messages**. The message format should be **<Node ID, Time, Sender ID, Receiver ID>**. The *Node ID* is the ID of the node which logs the message, the *time value* means the system (process) time immediately before the message sending or after receiving.

- *For example:* the message <24, 10:00:00, 11, 24> means that the message was received and logged by node 24 at 10:00:00. The message <24, 10:00:05, 24, 22> means that the message logged by the node 24, sent from node 24 to node 22 at 10:00:05 etc.

- The implementation must be continuously stored to the **FIT’s Giltab repository** due to the inspection of changes.

- The mandatory part of the project is the **Project Report** containing the *algorithm description* (by own words), *implementation description* (main classes, UML scheme, etc.), and measurements of *message count for at least 100 topologies* from [here](https://courses.fit.cvut.cz/MIE-DSV/tutorials/files/topologies.txt). 

- The measurements will contain the count of messages which were necessary to spread through the ring topology to achieve the final state. 

- The project report must be stored at the Gitlab repository as well.

- Finally, the deadline of storing the final solution is **1.1.2022 23:59:59**.


# About Unidirectional Links Eager Leader Election Algorithm

The algorithm implemented for this solution is the Unidirectional Links Eager Leader Election Algorithm in a distributed system using a ring topology.
This algorithm consists of a given list of nodes that make a ring, like the picture above, and the algorithm has to start in a Unique Initiator and analize each of the
nodes pairs one by one. In each comparison between two nodes, if the sender's value is lower than the receiver's value, then the receiver is eliminated from the topology
and the in the followings interations it will be skipped. The idea is that in each iteration at least one node is eliminated until only one node is left which is the leader.
We have followed the most common desing pattern as shown in class that consists of communicating each node only with the one in the right from the node view as the links are
unidirectional, and there each node can only be connected to another node (but just one, not two or more).

1. The fisrt node from the given list is considered as the Inititator and therefore as a sender.
2. Sender sends a message to the receiver (next node)
3. If sender's value is lower than receiver's value, then receiver is eliminated. If not, continue to next pair.
4. If a node is eliminated, the sender has to skip to the next available node in the topology.
5. If sender and receiver are the same node, then is a leader. Finish.

## Algorithm Example

3,1,2,4 <br />
Nodes = [3,1,2,4] <br />
Links = {3-1, 1-2, 2-4, 4-3} <br />
<br />
Iteration 1: <br />
¿3 < 1? False, therefore continue with next pair of nodes. <br />
¿1 < 2? True, therefore eliminate node 2 and new receiver of node 1 is node 4 because nodes list is now [3,1,4] <br />
¿2 < 4? True, therefore eliminate node 4 and new reciever of node 1 is node 3 because nodes list is now [3,1] <br />
<br />
Iteration 2: <br />
¿3 < 1? False, therefore continue with next pair of nodes. <br />
¿1 < 3? True, therefore eliminate node 3 and new receiver of node 1 is node 1 because nodes list is now [1] <br />
¿1 == 1? True, therefore NODE 1 IS LEADER <br />


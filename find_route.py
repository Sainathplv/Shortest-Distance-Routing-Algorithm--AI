import sys
import sysconfig
import queue

# we need find a search algorithm for a given text file
# if the text file has source,destination,and distance
# so firstly we need to get the data from the lines and seperate them as source,destination,and distance
# and plot a graph to that


# ref : https://www.geeksforgeeks.org/python-create-graph-from-text-file/
def plot_graph(inputfile):
    fileread = open(inputfile,"r")
    graph = dict() # to make a relation b/w source and destination and its value
    for row in fileread:
        if row != "END OF INPUT":
            data = row.split(' ')
            source = data[0]
            destination = data[1]
            distance = data[2].strip('\n')

            graph.setdefault(source, {})[destination] = distance
            graph.setdefault(destination,{})[source] = distance

        else:
            break

    fileread.close()

    return graph

# if heuristic file is given
def read_heuristic(input_heuristicfile):
    fileread = open(input_heuristicfile,'r')
    heuristicgraph = dict()
    for row in fileread:
        if row != "END OF INPUT":
            data = row.split(' ')
            place = data[0]
            value = data[1]
            heuristicgraph[place] = value

        else:
            break

    fileread.close()
    return heuristicgraph

# now lets create a function for informed search algorithm
# ref : https://isaaccomputerscience.org/concepts/dsa_search_a_star?examBoard=all&stage=all

def informed(src, dest, graph, heuristic):
    print('Informed Search Algorithm ')
    visited = set()
    unvisited = set()
    queueset = queue.PriorityQueue()
    queueset.put((0, [src], 0))
    result = dict()

    generated = 0
    expanded = 0
    size = 1

    while not queueset.empty():
        node = queueset.get()
        current = node[1]
        length = len(current)
        current_place = current[length - 1]

        if current_place not in visited:
            visited.add(current_place)
            expanded += 1
        if current_place == dest:
            current.append(node[2])
            result['path'] = current[:-1]
            result['cost'] = current[-1]
            print('Generated:', generated)
            print('Expanded:', expanded)
            print('Maximum nodes:', size)
            return result

        children = graph[current_place]
        for child in children.keys():
            if child not in visited:
                cost = node[0] + int(heuristic[child])
                heur = node[2] + int(children[child])
                path = current[:]
                path.append(child)
                queueset.put((cost, path, heur))
                size = max(size, queueset.qsize())
                generated += 1

    print('Generated:', generated)
    print('Expanded:', expanded)
    print('Maximum nodes:', size)


def uninformed(src, dest, graph):
    print('Uninformed Search Algorithm -- Uniform Cost Search ')
    if src not in graph and dest not in graph:
        return 'Path not found'

    else:
        visited = set()
        queueset = queue.PriorityQueue()
        queueset.put((0, [src]))

        generated = 0
        expanded = 0

        result = dict()
        size = 1

        while not queueset.empty():
            node = queueset.get()
            curr = node[1][len(node[1]) - 1]

            # print('curr', curr)
            expanded += 1

            if curr not in visited:
                visited.add(curr)
                if dest in node[1]:
                    result['path'] = node[1]
                    result['cost'] = str(node[0])
                    print('Generated:', generated)
                    print('Expanded:', expanded)
                    print('Maximum nodes:', size)
                    return result

                cost = node[0]
                for child in graph[curr]:
                    temp = node[1][:]
                    temp.append(child)
                    generated += 1
                    # if child not in visited:
                        # queue.put((cost + int(graph[curr][child]), temp))
                    queueset.put((cost + int(graph[curr][child]), temp))
                    size = max(size, queueset.qsize())

        print('Generated:', generated)
        print('Expanded:', expanded)
        print('Maximum nodes:', size)
        # return 'Path does not exist'


def main():
    input_file = sys.argv[1]
    graph = plot_graph(input_file)
    # print(graph)

    src = sys.argv[2]
    dest = sys.argv[3]

    if len(sys.argv) == 4:
        result = uninformed(src, dest, graph)
        if result:
            # print(result)
            print('Distance: ', result['cost'])
            print('Path: ')
            for i in range(len(result['path']) - 1):
                print(result['path'][i] + ' to ' + result['path'][i+1] + ': ' +
                      graph[result['path'][i]][result['path'][i+1]] + ' kms')
        else:
            print('Path not found')

    elif len(sys.argv) == 5:
        heuristic_file = sys.argv[4]
        heuristic = read_heuristic(heuristic_file)
        result = informed(src, dest, graph, heuristic)
        if result:
            # print(result)
            print('Distance: ', result['cost'])
            print('Path: ')
            for i in range(len(result['path']) - 1):
                print(result['path'][i] + ' to ' + result['path'][i + 1] + ': ' +
                      graph[result['path'][i]][result['path'][i + 1]] + ' kms')
        else:
            print('Path not found')

    else:
        print('Enter valid arguments')

main()
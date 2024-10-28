def display_menu():
    print('---- Menu ----')
    print('1) Add suspect')
    print('2) Add accomplice')
    print('3) Display all suspects')
    print('4) Finnd potential accomplices')
    print('E) Exit')

def display_suspect(suspect, graph):
    if suspect in graph:
        print(f'{suspect}: ')
        for accomplice in graph[suspect]:
            print(f'\t{accomplice}')


def display_all_suspects(graph):
    # graph is a dictionary, key = name suspect, value = name accomplices
    # graph[suspect] = accomplice
    print('---- All suspects ----')
    for suspect in graph:
        display_suspect(graph)


def find_potential_accomplices(suspect, graph):
    potential_accomplices = set()

    for accomplice in graph[suspect]:
        # set difference, includes all other accomplice but the current one 
        potential_accomplices.update(graph.get(accomplice, set()))
    
    potential_accomplices -= graph[suspect]
    potential_accomplices.discard(suspect)
    
    return {suspect: potential_accomplices}


def display_potential_accomplices(suspect, graph):
    potential_new = find_potential_accomplices(suspect, graph)
    known = display_suspect(suspect, graph)
    new = display_all_suspects(suspect, potential_new)
    print('---- Potential accomplices ----')
    print('Already known accomplices: ')


# def display_all_suspects(graph):
#     print('---- All suspects ----')
#     display_suspect(, graph)
        
# def main():
#     social_graph: 

# if __name__ == '__main__':
#     main()
import pickle

def display_menu():
    print('---- Menu ----')
    print('1) Add suspect')
    print('2) Add accomplice')
    print('3) Display all suspects')
    print('4) Find potential accomplices')
    print('E) Exit')

def display_suspect(suspect, graph):
    accomplices = graph.get(suspect, set())
    if accomplices:
        print(f'{suspect}:')
        for accomplice in sorted(accomplices):
                print(f'    {accomplice}')
    else:
        print(f'{suspect}:')


def display_all_suspects(graph):
    # graph is a dictionary, key = name suspect, value = name accomplices
    # graph[suspect] = accomplice
    print('---- All suspects ----')
    for suspect in graph:
        display_suspect(suspect, graph)


def find_potential_accomplices(suspect, graph):
    potential_accomplices = set()
    for accomplice in graph.get(suspect, []):
        # set difference, includes all other accomplice but the current one 
        potential_accomplices.update(graph.get(accomplice, set()))
    potential_accomplices -= graph.get(suspect, set())
    potential_accomplices.discard(suspect)
    return {suspect: potential_accomplices}


def display_potential_accomplices(suspect, graph):
    potential_new_accomplices = find_potential_accomplices(suspect, graph)
    print('---- Potential accomplices ----')
    print('Already known accomplices:')
    display_suspect(suspect, graph)
    print('\nPotential new accomplices:')
    display_suspect(suspect, find_potential_accomplices(suspect, graph))


def load_from_file(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)


def save_to_file(graph, filename):
    with open(filename, 'wb') as file:
        pickle.dump(graph, file)

def main():
    filename = input('Social graph filename: ').strip()

    try:
        social_graph = load_from_file(filename)
        print('*** Graph loaded from file. ***')
    except FileNotFoundError:
        social_graph = {}
        print('*** File not found. Starting with empty graph. ***')
            
    
    keep_going = True
    while keep_going:
        display_menu()
        choice = input('Option: ').strip() # prevents errors of extra spaces 

        if choice == '1':
            suspect = input('Name a suspect: ').strip()
            if suspect not in social_graph:
                social_graph[suspect] = set()
                save_to_file(social_graph, filename)

        elif choice == '2':
            suspect = input('Name a suspect: ').strip()
            accomplice = input('Name the accomplice: ').strip()
            if suspect in social_graph:
                social_graph[suspect].add(accomplice)
                if accomplice not in social_graph:
                    # Initialize accomplice in graph if not already present
                    social_graph[accomplice] = set()
                social_graph[accomplice].add(suspect)
                save_to_file(social_graph, filename)

        elif choice == '3':
            display_all_suspects(social_graph)

        elif choice == '4':
            suspect = input('Name a suspect: ').strip()
            if suspect in social_graph:
                display_potential_accomplices(suspect, social_graph)
        
        elif choice.lower() == 'e':
            keep_going = False
                

if __name__ == '__main__':
    main()
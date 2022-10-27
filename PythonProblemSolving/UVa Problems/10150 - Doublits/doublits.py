class Tree(object):
    # makes a tree node
    def __init__(self, data, working_dictionary) -> None:
        self.data = data
        self.working_dictionary = working_dictionary
        self.children = get_one_letter_diff_from_target(working_dictionary, data)
        
def get_words_of_len_x(arr: list, x: int) -> list:
    arr_to_return = []
    
    for word in arr:
        if len(word) == x:
            arr_to_return.append(word)
            
    return arr_to_return

def check_num_of_differences(string1: str, string2: str) -> int:
    length_of_strings = len(string1)
    count = 0
    
    for i in range(length_of_strings):
        if string1[i] != string2[i]:
            count += 1
            
    return count

def get_one_letter_diff_from_target(arr: list, target: str) -> list:
    possible_diffs = []
    
    for item in arr:
        if check_num_of_differences(item, target) == 1:
            possible_diffs.append(item)
            
    return possible_diffs

def evaluate_tree(node: Tree, current_solution_arr: list):
    
    for word in node.children:
        new_node = Tree(word)
        get_one_letter_diff_from_target(working_dictionary, word)
    

def evaluate(first_str: str, second_str: str, dictionary: list) -> list:
    list_to_return = []
    
    if len(first_str) == len(second_str):
        working_dictionary = get_words_of_len_x(dictionary, len(second_str))
        
        possible_steps = get_one_letter_diff_from_target(working_dictionary, second_str)
        
        new_node = Tree(second_str)
        new_node.children.extend(possible_steps)
        
        current_solution = []
        
        evaluate_tree(new_node, current_solution)
        
        return list_to_return
    else:
        return ["No solution."]
    
    

def main():
    dictionary_list = []
    get_input = None
    
    while get_input != "":
        get_input = input()
        dictionary_list.append(get_input)
        
    del dictionary_list[-1]
    
    vals_to_evaluate = []
    
    try:
        while True:
            two_vals = input().split()
            vals_to_evaluate.append(two_vals)
    except EOFError:
        pass
    
    solutions = []
        
    for pair in vals_to_evaluate:
        solutions.append(evaluate(pair[0], pair[1], dictionary_list))
        
    for i, solution in enumerate(solutions):
        for word in solution:
            print(word)
        if i < len(solutions):
            print()
    
    
if __name__ == "__main__":
    main()
    
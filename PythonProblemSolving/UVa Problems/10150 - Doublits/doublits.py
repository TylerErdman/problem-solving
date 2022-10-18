def get_words_of_len_x(arr: list, x: int) -> list:
    arr_to_return = []
    
    for word in arr:
        if len(word) == x:
            arr_to_return.append(word)
            
    return arr_to_return

def get_one_letter_diff_from_target(arr: list, target: str) -> list:
    possible_diffs = []
    
    for thing in arr:
        if check_num_of_differences(thing, target)

def evaluate(pair: list, dictionary: list) -> list:
    list_to_return = []
    
    if len(pair[0]) == len(pair[1]):
        working_dictionary = get_words_of_len_x(dictionary, len(pair[0]))
        
        possible_steps = get_one_letter_diff_from_target(working_dictionary, pair[0])
        
        
        
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
        solutions.append(evaluate(pair, dictionary_list))
        
    for i, solution in enumerate(solutions):
        for word in solution:
            print(word)
        if i < len(solutions):
            print()
    
    
if __name__ == "__main__":
    main()
    
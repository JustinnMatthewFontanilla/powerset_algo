# Justinn Matthew Fontanilla
# Discrete Math % CP2
# Generates the power set from user input using a recursive approach

def powerset(input_set):
    if len(input_set) == 0:   # Base case: the power set of an empty set is a set containing the empty set
        return [set()]
    first_elem = input_set[0]  # Get the first element and the rest of the set
    rest = input_set[1:]
    
    rest_powerset = powerset(rest)  # Recursively compute the power set of the rest of the set
    
    # Combine the subsets: add the first element to each subset 
    # in the power set of the rest of the set
    with_first_elem = [subset | {first_elem} for subset in rest_powerset]  

    # Return the combination of both sets (with and without the first element)
    return rest_powerset + with_first_elem 

def main():
    retry = True
    while retry:
        try:
            user_input = input("Enter the elements of the set, separated by spaces: ")
            input_set = user_input.split()  # Convert input to a list of elements
            
            result = powerset(input_set) # Generate the power set

            print("The power set is:") # Print the power set
            for subset in result:
                print(subset)
            retry_input = True
            while retry_input:  # Ask the user if they want to try again
                    if retry == "y" or "n":
                        retry_input = False
                    else:
                        print("Invalid input. Please try again. for retry reply")
                        retry_input = True
        except:
            print("Invalid input. Please try again. for set input")
            retry = True

# Check if the script is being run as the main program, if true: call the main()
if __name__ == "__main__":
    main()

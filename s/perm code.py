def generate_permutations(elements):
    if not elements:
        return [[]]

    all_permutations = []

    for i in range(len(elements)):
        chosen_element = elements[i]
        remaining_elements = elements[:i] + elements[i+1:]
        subproblem_permutations = generate_permutations(remaining_elements)

        for permutation in subproblem_permutations:
            all_permutations.append([chosen_element] + permutation)

    return all_permutations

def main():

    num_elements = int(input("Enter the number of elements: "))

    
    elements = [input(f"Enter element {i + 1}: ") for i in range(num_elements)]

   
    result = generate_permutations(elements)

   
    print("Permutations will be :")
    for perm in result:
        print(perm)

if __name__ == "__main__":
    main()

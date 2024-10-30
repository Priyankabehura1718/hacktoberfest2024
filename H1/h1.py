import os

# Base directory for contributions
BASE_DIR = "Hacktoberfest2024_Contributions"

# Create a base directory if it doesn't exist
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)

# Function to create user directory and solution categories
def create_user_directory(username):
    user_dir = os.path.join(BASE_DIR, username)
    categories = ["DSA", "Dynamic_Programming", "Graph_Theory", "Sorting_Algorithms", "Other"]

    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
        print(f"Directory created for user '{username}'")

    # Create subdirectories for categories
    for category in categories:
        category_dir = os.path.join(user_dir, category)
        if not os.path.exists(category_dir):
            os.makedirs(category_dir)
            print(f"Created category folder '{category}' for user '{username}'")
    return user_dir

# Function to add solution file to a specific category
def add_solution(username, category, problem_statement, solution_code, time_complexity=None, space_complexity=None):
    user_dir = create_user_directory(username)
    category_dir = os.path.join(user_dir, category.replace(" ", "_"))

    # Check if category is valid
    if not os.path.exists(category_dir):
        print(f"Invalid category '{category}'. Please use an existing category.")
        return

    # File name for the solution
    problem_title = problem_statement.split()[0]  # Use first word of problem statement for simplicity
    solution_filename = os.path.join(category_dir, f"{problem_title}.py")

    # Write solution to file
    with open(solution_filename, "w") as file:
        file.write(f"# Problem: {problem_statement}\n")
        file.write(f"# Solution by: {username}\n\n")
        file.write(f"# Time Complexity: {time_complexity}\n" if time_complexity else "")
        file.write(f"# Space Complexity: {space_complexity}\n\n" if space_complexity else "")
        file.write(solution_code)
    
    print(f"Solution '{problem_title}' added in '{category}' for user '{username}'")

# Example Usage
if _name_ == "_main_":
    # Sample contributor data
    username = "Sarthak50"
    category = "DSA"
    problem_statement = "Find the maximum sum subarray"
    solution_code = '''
def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum
    '''
    time_complexity = "O(n)"
    space_complexity = "O(1)"

    # Add solution to repository
    add_solution(username, category, problem_statement, solution_code, time_complexity, space_complexity)
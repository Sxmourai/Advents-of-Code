import sys # Imports the sys module
file_name = "input" # Sets the file name
if len(sys.argv) > 1 and sys.argv[1] == "test": # Checks if "test" input parameter was set
    file_name = "test_input"
with open(file_name, "r") as f: # Opens the input / test_input
    r = f.read() # Reads the file

def predict_next(previous): # Declares function to predict next value
    n = 0 # Sets our predicted value to 0
    for step in reversed(previous): # Iterate over our step in reversed order
        spe_num = step[-1] # Gets the next number to add to our predicted value
        n+=spe_num # Adds it
    return n # Returns the value


def get_steps(full_nums): # Create the steps, and return the predicted value
    steps = [] # Declares the steps as a 2dim array
    nums = full_nums[-1] # Gets the last step (by default the input line)
    for i,n in enumerate(nums[:-1:]): # Iterates over all numbers, without the last one (because can't get step between last element and the next one)
        step = nums[i+1]-n # Gets the difference between n and n+3 i.e.
        steps.append(step) # Adds it to the step
    for step in steps: # Checks if all values in step is 0
        if step != 0:
            break
    else:# All steps = 0
        return predict_next(full_nums) # returns the predicted value
    return get_steps(full_nums + [steps,]) # Run recursively the function, with the new step


s=0 # Starts the sum at 0
for line in r.splitlines(keepends=False): # Iterate on all lines without \n
    nums = list(map(lambda n: int(n),line.split(" "))) # Transforms all nums in line into a list of numbers
    s+=get_steps([nums,]) # Adds the predicted value to sum
print(s) # Prints the sum
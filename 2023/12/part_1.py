import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    r = f.read()



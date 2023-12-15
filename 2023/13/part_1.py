import sys
FILE_NAME = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    FILE_NAME = "test_input"
with open(FILE_NAME, "r", encoding="utf-8") as f:
    r = list(map(lambda line: list(line), f.read().splitlines(keepends=False)))

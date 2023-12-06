def split_int(content, sep):
    return list(map(lambda x: int(x), filter(lambda x: x.strip() != '', content.split(sep))))

import sys
file_name = "input"
if len(sys.argv) > 1 and sys.argv[1] == "test":
    file_name = "test_input"
with open(file_name, "r") as f:
    seeds = split_int(f.readline()[7:], " ")
    f.readline()  # Skip first line
    r = f.readlines()

old_seeds = []
new_seeds = seeds.copy()
mapper = ""
for line in r:
    line = line.strip()

    if line:
        if line.endswith(" map:"):
            source, to, destination = line[:-5].split("-")
            mapper = source, destination
            for old_seed in old_seeds:
                new_seeds.append(old_seed)
            old_seeds = new_seeds.copy()
            new_seeds = []
        else:
            dest,src,_len = split_int(line, " ")
            src_range = range(src, src+_len)
            to_remove = []
            for seed in old_seeds:
                if seed in src_range:
                    to_remove.append(seed)
                    new_seeds.append(seed-src+dest)

            for seed in to_remove:
                old_seeds.remove(seed)

for old_seed in old_seeds:
    new_seeds.append(old_seed)

print(new_seeds,min(new_seeds)) # 278755257
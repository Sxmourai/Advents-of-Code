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
new_seeds = []
for i,seed in enumerate(seeds[::2]):
    i *= 2
    i += 1
    new_seeds.append((seed, seeds[i]))
print(new_seeds)
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
            for (seed_start, seed_len) in old_seeds[:]:
                seed_end = seed_start+seed_len
                end = src+_len
                if seed_start>=src and seed_start<=end:
                    old_seeds.remove((seed_start, seed_len))
                    if seed_end<=end:
                        #print("Transform:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",seed_start-src+dest, seed_start-src+dest+seed_len)
                        new_seeds.append((seed_start-src+dest, seed_len))
                    else:
                        ns = seed_start-src+dest
                        nl = (dest+_len)-seed_start-src+dest
                        print("T:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",ns, nl)
                        new_seeds.append((ns, nl))
                        ns = ns+nl
                        nl = seed_len-nl
                        print("T:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",ns, nl)
                        new_seeds.append((ns, nl))
                        
                        
                        

for old_seed in old_seeds:
    new_seeds.append(old_seed)

m = min(map(lambda x: x[0],new_seeds))
print(new_seeds,m)
if m == 46:
    print("Test passed")



#                if seed_start>=src and seed_start<=end:
 #                   to_remove.append((seed_start, seed_len))
  #                  if seed_end<=end:
   #                     #print("Transform:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",seed_start-src+dest, seed_start-src+dest+seed_len)
    #                    new_seeds.append((seed_start-src+dest, seed_len))
     #               else:
      #                  ns = seed_start-src+dest
       #                 nl = (dest+_len)-seed_start-src+dest
        #                print("T:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",ns, nl)
         #               new_seeds.append((ns, nl))
          #              ns = ns+nl
           #             nl = seed_len-nl
            #            print("T:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",ns, nl)
             #           new_seeds.append((ns, nl))
                        
#                if seed_start>=src and seed_start<=end:
 #                   to_remove.append((seed_start, seed_len))
  #                  if seed_end<=end:
   #                     #print("Transform:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",seed_start-src+dest, seed_start-src+dest+seed_len)
    #                    new_seeds.append((seed_start-src+dest, seed_len))
     #               else:
      #                  ns = seed_start-src+dest
       #                 nl = (dest+_len)-seed_start-src+dest
        #                print("T:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",ns, nl)
         #               new_seeds.append((ns, nl))
          #              ns = ns+nl
           #             nl = seed_len-nl
            #            print("T:",seed_start,"--",seed_end,"in",src,"--",end,  "\tto\t",dest,dest+_len, "\tso",ns, nl)
             #           new_seeds.append((ns, nl))
                        
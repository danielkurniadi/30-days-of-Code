def permutations(f):
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        print(''.join(running))
        f.write("{}\n".format(''.join(running)))
    else:
        for i in range(len(characters)):
            if ((bitmask>>i)&1) == 0:
                bitmask |= 1<<i
                running.append(characters[i])
                permutations(f)
                bitmask ^= 1<<i
                running.pop()

raw = raw_input()
characters = list(raw)
running = []
bitmask = 0
with open("output_permute.txt", "w") as f:
    permutations(f)
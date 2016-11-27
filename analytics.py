from __future__ import print_function


# increment counter in usageStats for function 'functionName'
def hit(functionName):
    with open("usageStats/stats.dat", "a+") as f:
        lines = f.read().splitlines()
        output = []
        found = False

        for line in lines:
            line = line.split("\t")
            if line[0] == functionName and len(line) > 1:
                try:
                    line[1] = str(int(line[1]) + 1)
                    found = True
                except:
                    print("couldn't increment counter for " + functionName
                          + " in usage stats")
            output.append("\t".join(line))

        if not found:
            output.append(functionName + "\t1")

    with open("usageStats/stats.dat", "w+") as f:
        print("\n".join(output), file=f)
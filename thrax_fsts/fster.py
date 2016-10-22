from subprocess import Popen, PIPE
import sys

def getRewrites(output):
    lines = output.split("\n")
    rewrites = []
    for line in lines[1:]:
        line = line.split(":")
        if len(line) == 3:
            rewrites.append(line[2])
        elif len(line) == 2:
            rewrites.append(None)
    return rewrites

def main():
    inputs = ["00011111", "0101"]
    if len(sys.argv) < 5:
        numout = "100"
        symtab = ""#"--input_mode=byte.sym --output_mode=byte.sym"
    else:
        numout = sys.argv[3]
        symtab = sys.argv[4]
    thraxcmd = "echo " + "\n".join(inputs) + " | thraxmakedep --save_symbols " + sys.argv[1] + ".grm && make && thraxrewrite-tester --print_rules=false --far=" + sys.argv[1] +".far " + symtab  + " --noutput="+ numout  + " --rules="+ sys.argv[2]
    p = Popen(thraxcmd, stdout = PIPE, shell=True)
    output, error = p.communicate()
    print "********** OUTPUT ********"
    print output.split("\n")
    print "********** OUTPUT ********"
    answers = getRewrites(output)
    print answers
    for i in range(len(answers)):
        if answers[i] == None:
            answer = ""
        else:
            answer = answers[i]
        print inputs[i] + " : " + answer
    

main()

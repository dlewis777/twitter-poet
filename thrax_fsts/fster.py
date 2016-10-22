from subprocess import Popen, PIPE
import sys

def getRewrites(output):
    lines = output.split("\n")
    rewrites = []
    for line in lines[1:]:
        line = line.split(":")
        if len(line) == 3:
            rewrites.append(line[2])
        elif len(line) == 2 and line[1] == " Rewrite failed.":
            rewrites.append("")
    return rewrites


def checkInputs(inputs, grm, fst, symtab = ""):
    numout = "1"
    thraxcmd = "thraxmakedep --save_symbols " + grm + ".grm && make && thraxrewrite-tester --print_rules=false --far=" + grm +".far " + symtab  + " --noutput="+ numout  + " --rules="+ fst
    p = Popen(thraxcmd, stdout = PIPE, stdin = PIPE, shell=True)
    output, error = p.communicate(input=b"\n".join(inputs))
    answers = getRewrites(output)
    for i in range(len(answers)):
        print inputs[i] + " : " + answers[i]
    return answers


def main():
    inputs = ["elephant", "howdy", "bicycle animal"]
    if len(sys.argv) < 4:
        numout = "100"
        symtab = ""
    else:
        symtab = sys.argv[3]
    checkInputs(inputs, sys.argv[1], sys.argv[2])

main()

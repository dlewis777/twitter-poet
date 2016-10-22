from subprocess import Popen, PIPE
import sys



def main():
    if len(sys.argv) < 5:
        numout = "100"
        symtab = "--input_mode=$symtab --output_mode=$symtab"
    else:
        numout = sys.argv[3]
        symtab = sys.argv[4]
    thraxcmd = "thraxmakedep --save_symbols " + sys.argv[1] + ".grm && make && thraxrewrite-tester --print_rules=false --far=" + sys.argv[1] +".far " + symtab  + " --noutput="+ numout  + " --rules="+ sys.argv[2]
    p = Popen(thraxcmd, shell=True)
    p.communicate()

main()
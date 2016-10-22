from subprocess import Popen, PIPE
import sys



def main():
    if len(sys.argv) < 5:
        numout = "100"
        symtab = ""#"--input_mode=byte.sym --output_mode=byte.sym"
    else:
        numout = sys.argv[3]
        symtab = sys.argv[4]
    thraxcmd = "thraxmakedep --save_symbols " + sys.argv[1] + ".grm && make && thraxrewrite-tester --print_rules=false --far=" + sys.argv[1] +".far " + symtab  + " --noutput="+ numout  + " --rules="+ sys.argv[2]
    p = Popen(thraxcmd, stdout = PIPE, shell=True)
    output, error = p.communicate()
    print output

main()

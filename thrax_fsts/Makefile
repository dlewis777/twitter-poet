dactyls.far: dactyls.grm byte.far arpabet.far arpabet.sym ../data/cmudict.txt ../data/cmudict.txt
	thraxcompiler --save_symbols --input_grammar=$< --output_far=$@

byte.far: byte.grm 
	thraxcompiler --save_symbols --input_grammar=$< --output_far=$@

arpabet.far: arpabet.grm arpabet.sym
	thraxcompiler --save_symbols --input_grammar=$< --output_far=$@

clean:
	rm -f byte.far arpabet.far

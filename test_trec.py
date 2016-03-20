import os
os.system(
    "./evaluator/trec_eval.9.0/trec_eval ./evaluator/data/robust/aq.trec2005.qrels ./evaluator/participants/robust/input.ASUDE > test_output.txt"
    )

#P10 - 23 P20 - 25 MAP - 6

file = open("test_output.txt")
lines=file.readlines()
MAP_score = lines[6][-7:]
P10_score = lines[23][-7:]
P20_score = lines[25][-7:]
print MAP_score
print P10_score
print P20_score
file.close()
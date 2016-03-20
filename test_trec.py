import os

#This can be run from Bash using: python -c "import test_trec; test_trec.getScores([qrels], [rels])"
#For example: python -c "import test_trec; test_trec.getScores(, './evaluator/participants/robust/input.ASUDE')

#Takes two strings as the paths for the judgement file and the file to be judges and returns
#tuple of the results for MAP, P10 and P20

def getScores(qrels_path, rels_path):

	#Runs trec_eval as a Bash command and then saves the output to the file test_output.txt
    os.system(
		"./evaluator/trec_eval.9.0/trec_eval " + qrels_path + " " + rels_path + " > test_output.txt"
		)


	#Then opens test_output.txt and gets the scores for MAP, P10, P20

    file = open("test_output.txt")
    lines=file.readlines()
    MAP_score = lines[6][-7:]
    P10_score = lines[23][-7:]
    P20_score = lines[25][-7:]
    print MAP_score
    print P10_score
    print P20_score
    file.close()

    return (MAP_score, P10_score, P20_score)


#"./evaluator/trec_eval.9.0/trec_eval ./evaluator/data/robust/aq.trec2005.qrels ./evaluator/participants/robust/input.ASUDE > test_output.txt"
with open("data.txt" , "r") as allData:
    Data = allData.read()
    question_list = Data.split("QUESTION: ")

Answers = []
Questions = []
Duals = [33,35,38,41,60,68,100,114,115,117,119,126,137]
Triples = [83]
for question_number in range(1, len(question_list)):
    Data = question_list[question_number].split('Correct Answer ~ ')
    Questions.append(Data[0])
    answer = str(Data[1])
    if question_number+1 in Duals:
        Answers.append(answer[:2])
    elif question_number+1 in Triples:
        Answers.append(answer[:3])
    else:
        Answers.append(answer[0])
    question_number+=1
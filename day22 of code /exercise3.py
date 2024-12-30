questions=[['Who is known as the Father of the Nation in India?','Jawaharlal Nehru','Subhas Chandra Bose','Mahatma Gandhi','Sardar Vallabhbhai Patel',3],
          ['Which of these is the longest river in the world?','Amazon','Nile','Yangtze','Mississippi',2]]
levels=[1000,2000]
money=0
for i in range(0,len(questions)):
    question=questions[i]
    print('question for rs.',levels[i])
    print('a',question[1],'       ','b',question[2])
    print('c',question[3],'       ','d',question[4])
    reply=int(input('enter your answer 1-4 '))
    if (reply==question[-1]):
        print('correct answer,you won',levels[i] )
    else:
        print('worng answer')
print(len(questions))
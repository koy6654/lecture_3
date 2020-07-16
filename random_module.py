import random as rd

def random_monster():
    monster = rd.randint(1,10)
    human = rd.randint(1,6)
    print("공격은 hit 입력, 무시하기는 ig")
    command = input()
    if(command == 'hit'):
        if(monster >= human):
            print("You lose!")
        else:
            print("You win!")
    elif(command == 'ig'):
        print("Bye!")

#random_monster()

def lotto_num():
    num = list(range(1,46))
    select_num = rd.randint(1,8)
    first_num = [rd.randint(1,8)-1]
    second_num = [rd.randint(9,16)-1]
    third_num = [rd.randint(17,24)-1]
    fouth_num = [rd.randint(25,32)-1]
    fifth_num = [rd.randint(33,40)-1]
    sixth_num = [rd.randint(41,45)-1]
    print("오늘 대박예감 번호입니다 {} {} {} {} {} {}" . format(first_num, second_num, third_num, fouth_num, fifth_num, sixth_num))


#lotto_num()
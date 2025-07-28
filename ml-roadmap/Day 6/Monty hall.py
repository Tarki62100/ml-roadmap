import numpy as np
#kanka belki bir ara bakarsan bu monty hall problemi zaten biliyorsundur da basitce soylemek gerekirse uc kapi var bu kapilardan birinin arkasinda araba obur 
#ikisinin arkasinda essek var sonra bir adam geliyo sana arkasinda esek olan kapilardan birini aciyor simdi sen arabayi kazanma ihtimalini arttirmak icin sectigin
#kapiyi degistirmeli misin yoksa fark etmez mi? kodda bu var istersen en asagidaki fonksiyonun icindeki sayiyi buyut sonuc daha az farklilikla cikar
def master_choice(a,b):
    num = np.random.randint(0,3)
    while num==a or num==b:
        num = np.random.randint(0,3)
    return num
def door_switch(doors,a):
    for door in doors:
        if door!=a:
            return door
def monty_hall_switch():
    doors=[0,1,2]
    player_door = np.random.randint(0,3)
    car_door = np.random.randint(0,3)
    master_door=master_choice(car_door,player_door)
    doors.remove(master_door)
    player_switch_door = door_switch(doors,player_door)
    if player_switch_door == car_door:
        return True
    else:
        return False
def monty_hall_no_switch():
    player_door = np.random.randint(0,3)
    car_door = np.random.randint(0,3)
    if player_door==car_door:
        return True
    else:
        return False
def many_trials(trial_num,monty_problem):
    player_wins = 0
    for i in range(trial_num):
        if monty_problem():
            player_wins+=1
    return player_wins
def pct_diff_btw_wins(num):
    print("Percentage difference between wins when choosing a different door versus not choosing a different door:%",(many_trials(num,monty_hall_switch)-many_trials(num,monty_hall_no_switch))/(num/100))
pct_diff_btw_wins(100000)




    

    

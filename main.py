from algo_project import *
from noncomparision import *
from ui_2 import *
def main():
    read = open(ui_main(), "r")
    score_list = read.read().split(',');
    float_list = []
    int_list = []
    for i in range(len(score_list)):
        float_list.append(float(score_list[i][0:]))
    for i in range(len(score_list)):
        int_list.append(int(score_list[i][0:]))
    print("CHOOSE YOUR OPTION \n1. SORTING VISUALIZED \n2. N-TIME GRAPH OF ALGORITHMS\n3. ALGORITHM 7.25 FROM BOOK\n4. ALGORITHM 8.24 FROM THE BOOK")
    choice = 10
    while choice!=0:
        choice = ui_choice()
        if choice ==1:
            visualize_code(int_list)
            break
        elif choice==2:
            main_code(float_list, int_list)
            break
        elif choice==3:
            book_725(int_list)
            break
        elif choice==4:
            print("Enter 1st number: ")
            n = int(input())
            print("Enter 2nd number: ")
            m = int(input())
            book_824(int_list, n, m)
            break        
main()
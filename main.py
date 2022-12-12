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
    choice = 10
    while choice!=0:
        choice = ui_choice()
        if choice ==1:
            visualize_code(int_list)
        elif choice==2:
            main_code(float_list, int_list)
        choice = 0
main()
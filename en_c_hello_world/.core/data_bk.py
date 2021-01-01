import random
compiler = 'gcc'

language = 'en'

answer_sheets = dict()
answer_sheets['main.c'] = '''
#include<stdio.h>
/**
 * This is a warm-up question, use this to test if your enviroment works.
 * Level: Kindergarten
 * Please print the string "Hello world!"
 */


int main(){

    /*⬇︎Please answer within this area⬇︎*/
    
    /*⬆︎Please answer within this area⬆︎*/

    return 0;
}
'''


standard_answer=dict()
standard_answer['main.c'] =r'''
    printf("Hello world!");
'''


def prepare_answer_sheets():
    return answer_sheets
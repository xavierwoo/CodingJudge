import random
compiler = 'g++'

language = 'cn'

answer_sheets = dict()
answer_sheets['main.cpp'] = '''
#include<iostream>
using namespace std;
/**
 * 热身题。请用此题检测环境是否已设置好。
 * 难度: 做不出来的话这边建议换专业之难度
 *
 * 请输出字符串 "Hello world!"
 */


int main(){

    /*⬇︎请在此区域内作答⬇︎*/
    
    /*⬆︎请在此区域内作答⬆︎*/

    return 0;
}
'''


standard_answer=dict()
standard_answer['main.cpp'] =r'''
    cout<<"Hello world!";
'''


def prepare_answer_sheets():
    return answer_sheets
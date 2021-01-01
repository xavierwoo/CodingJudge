import random
import time
compiler = 'g++'

language = 'cn'

answer_sheets = dict()

answer_sheets_bk = dict()
answer_sheets_bk['main.cpp'] = '''
#include<iostream>
using namespace std;

/*
 * 单链表的插入操作
 * 难度：简单
 * 
 * 要求：
 * 已知单链表节点结构为Node， 
 * 请在main函数中完成操作：在链表的第一个data值为100的元素之后插入data值为1024的新节点。
 * 注意，原始链表将在验证时随机生成
 * 
*/

struct Node{
    int data;
    Node* next;
    Node(int d, Node* n):data(d),next(n){}     
};

Node* create_linked_list();
void print_linked_list(Node* head);
void delete_list(Node* head);

int main(){
    Node* head = create_linked_list(); //此处链表在判定时将随机生成
    cout<<"原始链表数据:"<<endl;
    print_linked_list(head);

    /*⬇︎请在此区域内作答⬇︎*/
    
    /*⬆︎请在此区域内作答⬆︎*/

    cout<<"更新后的链表数据:"<<endl;
    print_linked_list(head);
    delete_list(head);
    return 0;
}

Node* create_linked_list(){

@rand@

    return head;
}

void print_linked_list(Node* head){
    Node* curr = head;
    while(curr != nullptr){
        cout<<curr->data<<" ";
        curr = curr->next;
    }
    cout<<endl;
}

void delete_list(Node* head){
    Node* curr = head;
    
    while(curr != nullptr){
        Node* next = curr->next;
        delete curr;
        curr = next;
    }
}
'''

standard_answer=dict()
standard_answer['main.cpp'] ='''
    Node* curr = head;
    Node* new_node = new Node(1024, nullptr);
    while(curr != nullptr && curr->data != 100){
        curr = curr->next;
    }
    new_node->next = curr->next;
    curr->next = new_node;
'''


def prepare_answer_sheets():
    list_length = random.randint(5, 10)
    cent_pos = random.randint(0, list_length - 1)

    insert_code = []
    insert_code.append('\tNode* head = new Node({0}, nullptr);'.format(100 - cent_pos))
    insert_code.append('\tNode* curr = head;')
    insert_code.append('\tfor(int i={0}; i<{1}; ++i){{'.format(100-cent_pos+1, 100 - cent_pos + list_length))
    insert_code.append('\t\tcurr->next = new Node(i, nullptr);')
    insert_code.append('\t\tcurr = curr->next;')
    insert_code.append('\t}')
    insert_code = '\n'.join(insert_code)

    answer_sheets['main.cpp'] = answer_sheets_bk['main.cpp'].replace('@rand@', insert_code, 1)
    
    return answer_sheets
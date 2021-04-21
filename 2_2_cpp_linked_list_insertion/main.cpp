
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

	Node* head = new Node(94, nullptr);
	Node* curr = head;
	for(int i=95; i<101; ++i){
		curr->next = new Node(i, nullptr);
		curr = curr->next;
	}

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

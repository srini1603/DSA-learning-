#include<iostream>
using namespace std;
struct Node
{
	int data;
	Node* next;
};
Node* head;

void inseratstart(int n) {
	Node* temp = new Node();
	temp->data = n;
	temp->next = head;
	head = temp;
	 
}
void insertinposition(int data, int n) {
	Node* temp1 = new Node();
	temp1->data = data;
	temp1->next = NULL;
	if (n == 1) {
		temp1->next = head;
		head = temp1;
		return;
	}
	
		Node* temp2 = head;
		for (int i = 1; i < n-2; i++) {
			temp2 = temp2->next;
		}
		temp1->next = temp2->next;
		temp2->next = temp1;
}
void insert(int data) {//insert at end
	Node* temp = new Node();
	temp->data = data;
	temp->next = NULL;
	Node* last = head;
	if (head == NULL)
	{
		head = temp;
		return;
	}
	while (last->next != NULL)
	{
		last = last->next;
	}
	last->next = temp;
	return;
	}
void deletelast() {
	Node* temp = head;
	while (temp->next->next != NULL) {//end if temp1->temp->NUll
		temp = temp->next;//jump to next and again check in while
	}
	Node* del = temp->next;
	temp->next = NULL;
	delete del;
}
void deleteposition(int n) {
	Node* prev = head;
	if (n == 1) {
		head = prev->next;
		delete prev;
		return;
	}
	for (int i = 0; i < n - 2; i++)
	{
		prev = prev->next;
	}
	Node* nextnode = prev->next;
	prev->next = nextnode->next;
	delete nextnode;
}
void printList(){
	Node* tempn = head;
	while (tempn != NULL)
	{
		cout << " " << tempn->data;
		tempn = tempn->next;
	}
	cout << endl;
}
void main() {
	head = NULL;
	insert(1);
	insert(2);
	insert(3);
	insert(4);
	insertinposition(5, 2);
	inseratstart(6);
	printList();
	deleteposition(4);
	deletelast();
	printList();


}
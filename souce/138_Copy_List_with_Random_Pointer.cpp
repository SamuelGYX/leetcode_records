/*
138. Copy List with Random Pointer Medium

Overview:

    Return a deep copy of the given linked list.

Solution:

    The key point of this problem is "deep copy", which means the random pointers must point to the same "location" within the original and copied list (instead of same "node"). How shall we translate a node pointer into the location inside the new list?

    This is solved by three iterations.

    1. Insert a new node after each node in the original list.

    2. Assign value to random pointer of new nodes.
        
        ```c
        if (iter->random != NULL)
            iter->next->random = iter->random->next;
        ```

    3. Split the original and new list.

Tricky points:

    1. Do not need to update random pointer when the original one is NULL. Otherwise, you will try to reference NULL pointer.

        ```c
        if (iter->random != NULL)
            iter->next->random = iter->random->next;
        ```

    2. We need a pseudo head for the new list whose next pointer pointing to the real result.

        ```c
        Node* res = new Node(0, NULL, NULL);
        ...
        return res->next;
        ```
 */

/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;

    Node() {}

    Node(int _val, Node* _next, Node* _random) {
        val = _val;
        next = _next;
        random = _random;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        Node* iter = head, * next;
        while (iter != NULL) {
            next = iter->next;
            iter->next = new Node(iter->val, NULL, NULL);
            iter->next->next = next;
            iter = next;
        }
        
        iter = head;
        while (iter != NULL) {
            if (iter->random != NULL)
                iter->next->random = iter->random->next;
            iter = iter->next->next;
        }
        
        Node* res = new Node(0, NULL, NULL), * resIter = res;
        iter = head;
        while (iter != NULL) {
            resIter->next = iter->next;
            iter->next = iter->next->next;
            iter = iter->next;
            resIter = resIter->next;
        }
        
        return res->next;
    }
}
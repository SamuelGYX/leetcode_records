/*
142. Linked List Cycle II Medium

Overview:

    Given a linked list, return the entry node for a loop, otherwise return NULL.

Solution:

    Iterate the list with a slow pointer p1 with step=1 and a fast pointer p2 with step=2. If p1 meets with p2 at some node, there must exists a loop.

    Example:

                         +-------> 3M
                         |
                         +         +
                                   |
    0S +-----> 1 +-----> 2E        |
                                   |
                         ^         v
                         |
                         +-------+ 4

        S       E   M
    p1  0   1   2   3 
    p2  0   2   4   3

    Notation:

        S: start node
        E: entry node
        M: meeting node

        AB: the distance between node A and node B.
            e.g. SE: the distance between node S and node E.
        L1: the distance traveled by p1 when meets
        L2: the distance traveled by p2 when meets
        C:  the length of circle
        n:  p2 may have traveled in the loop for many times(n) when p1 and p2 meets at node M (n >= 1)
    
    Therefore, we know that

        L1 * 2 = L2
        =>  (SE + EM) * 2 = SE + EM + n*C
        =>  SE = (n-1)*C + C - EM
        =>  SE = (n-1)*C + ME

    This means the distance between SE is equal to the distance between ME. Then, we could get E from M with this property.

Tricky points:

    1. The list must have at least 2 nodes before we could move 2 steps.

    2. We only need to check whether p2 meets NULL. But we have to check two subsequent nodes.
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        if (head == NULL || head->next == NULL)
            return NULL;
        ListNode *p1 = head, *p2 = head, *start = head;
        while (p2->next != NULL && p2->next->next != NULL) {
            p1 = p1->next;
            p2 = p2->next->next;
            if (p1 == p2) {
                while (start != p1) {
                    start = start->next;
                    p1 = p1->next;
                }
                return start;
            }
        }
        return NULL;
    }
};
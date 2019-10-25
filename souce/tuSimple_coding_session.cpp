/*
Description

Given two alphabet strings str1 and str2. You can change the characters in
str1 to any alphabet characters in order to transform str1 to str2. One
restriction is, in each operation, you should change all the same characters
simultaneously.

What's more, you may use another special character * if necessary, which means
during each operations, you may change the same alphabet characters to *, or
change all * to a specific character. Please note that "turn the same
characters to *" and "turn all * to a specific character" both take exact
one operation.

We want to know the minimum operation times. If impossible, return -1.

Input format

Two strings.

Output format

One integer.

Examples

Example 1:
str1: accs, str2: eeec
operation 1: change 'a'->'e'; // str1: eccs
operation 2: change 'c'->'e'; // str1: eees
operation 3: change 's'->'c'; // str1: eeec
return 3;

Example 2:
str1: accs, str2: efec
return -1;

Example 3:
str1: abb , str2: baa
operation 1: change 'a'->'*'; // str1: *bb
operation 2: change 'b'->'a'; // str1: *aa
operation 3: change '*'->'b'; // str1: baa
return 3;
*/
#include <iostream>
#include <vector>
#include <string>
#include <locale>
using namespace std;

const int node_nr = 26;
vector<bool> visit(node_nr, false);

bool dfs(int start, int end, vector<int>& connect, vector<bool>& visit) {
    if (connect[start] == end)
        return true;
    if (connect[start] == -1 || visit[connect[start]])
        return false;
    
    visit[connect[start]] = true;
    if (dfs(connect[start], end, connect, visit)) {
        return true;
    } else {
        visit[connect[start]] = false;
        return false;
    }
}

int main() {
    string str1 = "abcdef", str2 = "bcaefd";
    int len1 = str1.length(), len2 = str2.length();
    
    if (len1 != len2)
        return -1;

    // construct map
    
    vector<int> connect(node_nr, -1);
    int edge_count = 0;
    
    for (int i = 0; i < len1; i++) {
        // convert all to lowercase
        
        if (connect[str1[i]-'a'] == -1) {
            connect[str1[i]-'a'] = str2[i]-'a';
            edge_count++;
        } else if (connect[str1[i]-'a'] != str2[i]-'a')
            return -1;
    }
    
    // count the number of loops
    
    int loop_count = 0;
    
    for (int i = 0; i < node_nr; i++) {
        if (connect[i] == i)
            continue;
        
        if (!visit[i] && dfs(i, i, connect, visit))
            loop_count++;
    }
    
    // return res
    
    return edge_count + loop_count;
}
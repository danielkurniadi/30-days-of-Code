#include<iostream>
#include<vector>
#include<unordered_set>

using namespace std;

/* Longest Consecutive Sequence Problem
*
* @definition: 
*   Given an unsorted array of integer, find the longest consecutive elements sequence,
*   that can be created from the element in the array.
*
* @solution: 
*   There is a simple way to approach this problem. It uses the power of hashing or memoization. 
*   The implementation can be done using simply an array to cache and retrieve in O(1) manner for each element
*   Or we can use a more suitable built-in data structure in cpp called hashSet, a hashmap that replicates the behavior of set (mathematically).
*   Hashset in C++ is called `std::unordered_set`.
*/

// using array memoization
int longestConsecutive(const vector<int> &A) {
    int minz = A[0];
    int maxz = A[0];
    for(int i; i<A.size(); i++)
    {
        if(A[i] > maxz)
            maxz = A[i];
        if(A[i] < minz)
            minz  =A[i];
    }
    
    int length = maxz-minz+1;
    vector <int> binlist(length, 0);
    
    for(int i=0; i<A.size(); i++){
        int a = A[i];
        binlist[a-minz] = 1;
    }
    int count = 0;
    int maxcount = 0;
    for(int i; i<binlist.size(); i++)
    {
        if(binlist[i]==1)
            count++;
        else{
            if(count>maxcount)
                maxcount=count;
            count=0;
        }
    }
    if(count>maxcount)
        maxcount = count;
    return maxcount;
}

// using unordered hashmap
int longestConsecutive(const vector<int> &A) {
    if (A.size() == 0)
        return 0;
    unordered_set<int> hashSet;

    for(int i; i<A.size(); i++)
        hashSet.insert(A[i]);
    
    int maxcount = 0;
    for(int i; i<A.size(); i++)
    {
        int left = A[i]-1;
        int right = A[i]+1;
        int count = 1;
        
        if(hashSet.find(A[i]) == hashSet.end())
            continue;
        
        hashSet.erase(A[i]);
        while(hashSet.find(left) != hashSet.end())
        {
            count++; 
            hashSet.erase(left);
            left--;   
        }
            
        while(hashSet.find(right) != hashSet.end()){
            count++; 
            hashSet.erase(right); 
            right++;
        }
        
        if(count>maxcount)
            maxcount = count;
    }
    
    return maxcount;
}
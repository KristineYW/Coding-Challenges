"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
"""

# We have to turn the split array into a list
# Then create a set to remove duplicate numbers
# Then we remove the first max from the set
# Then n becomes the second max number

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

lst = list(arr)
set1 = set(lst)
set1.remove(max(set1))
n = max(set1)

print(n)

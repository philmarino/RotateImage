def rotate(matrix):
    #clever solution from Aaru_07: https://leetcode.com/problems/rotate-image/solutions/5533383/very-easy-c-solution-beats-100/?envType=study-plan-v2&envId=top-interview-150
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j] #check out this swap
        matrix[i].reverse()

    return matrix

# Example 1:
# Input: 
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix))
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:
# Input: 
matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix))
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
 
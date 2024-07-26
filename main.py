def rotate(matrix):
    answer = []
    
    for i in range(len(matrix)):
        answer.append([]) 
        for j in range(len(matrix)-1, -1, -1):
            answer[i].append(matrix[j][i])

    return answer

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
 
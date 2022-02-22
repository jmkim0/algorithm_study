n_m = input().split(" ")
n = int(n_m[0])
m = int(n_m[1])
matrix = []
for i in range(n):
    matrix.append(input())

def check_line(line1, line2):
    count = 0
    
    for i in range(8):
        if line1[i] != line2[i]:
            count += 1
    
    return count

min_paint = -1

for i in range(n-7):
    for j in range(m-7):
        count1 = 0
        count2 = 0

        for k in range(8):
            if k%2 == 0:
                count1 += check_line(matrix[i+k][j : j+8], "WBWBWBWB")
                count2 += check_line(matrix[i+k][j : j+8], "BWBWBWBW")
            else:
                count1 += check_line(matrix[i+k][j : j+8], "BWBWBWBW")
                count2 += check_line(matrix[i+k][j : j+8], "WBWBWBWB")
        
        if count1 <= count2:
            less_count = count1
        else:
            less_count = count2
        
        if min_paint==-1 or min_paint>less_count:
            min_paint = less_count
        
print(min_paint)
        


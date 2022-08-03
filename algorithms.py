## sliding window

n=5
s=[1, 2, 1, 3, 2]
d=3
m= 2
count = 0
for i in range(len(s)):
        temp = s[i:i+m]
        if sum(temp) == d:
                count += 1


print(count)



# unique path only bottom and right start from 1 reaches 6 how many path available
# bactracking algo
arr = [[1,2,3],
       [4,5,6],
       [4,5,6],
       [4,5,6]]
m= len(arr)
n = len(arr[0])

class temp:
        paths = 0
        def unique(self,row, col, m, n):
                if col==n-1:
                        for i in range(row,m):
                                pass
                        self.paths += 1
                        return
                if row == m-1:
                        for i in range(col,n):
                                pass
                        self.paths += 1
                        return
                self.unique(row,col+1,m,n)
                self.unique(row+1,col,m,n)

t =  temp()
t.unique(0,0,m,n)

print(t.paths)
        
                
        

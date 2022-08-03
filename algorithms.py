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
        
        
# for longest non repeating character use hashset
# append the new char if char(new) is not in set use (j varibale) or else  remove from front 
# pwwken  
# 1)p 2)pw 3)(since it w and in substring we'll remove untill we remove w pw->w ->"")  4) w 5) wk 6) wke 7)wken


s = "pwwken"
t = []
maxs = 0
i =0
j =0
while(i<len(s) and j <len(s)):
        print(t)
        if(s[i] in t):
                t.pop(j)
        else:
                t.append(s[i])
                maxs = max(maxs, len(t))
                i += 1

print(maxs)

                
        

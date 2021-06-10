s = input()
for i in s.split():#i n s we write jyotirmoy nath then first i will take jyotirmoy and second time it will take nath 
    s = s.replace(i,i.capitalize()) #when loop start running it will first take jyotirmoy which will store in i and second time i will store nath.
print(s)
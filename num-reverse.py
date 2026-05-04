n = 6578
temp = n
rev = 0
while temp != 0:
    r = temp % 10 #6
    rev = (rev*10)+r #(24*10)+6=>246
    temp = temp // 10
    
print(rev)
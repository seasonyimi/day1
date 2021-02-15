ACCOUNT='yonghu'
PASSWORD='123456'
i=5
print("请输入用户名：")
user_account=input()
print("请输入密码：")
user_password=input()
# if用法举例
""" if (ACCOUNT==user_account) and (PASSWORD==user_password) :
    print("登录成功")
else:
    print("用户或密码输入错误") """

# while expression:
#     pass
# else:
#     pass

a=[['apple','banana','orangle','grape'],(1,2,3)]
for x in a:
    if 2 in x:
        break
    for y in x:
        # if y=='orangle':
        #     break
        print(y)   #end=''可以使不换行，里面加\n为换行
else:
    print("fruit is gone")   #if中很少用else

b=[1,2,3]
for x in b:
    if x==2:
        continue
    print(x)

for c in range(10,0,-2):  
    print(c,end=' | ')



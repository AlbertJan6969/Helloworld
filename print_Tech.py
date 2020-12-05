print("\033[0mhi\033[0m")
print("\033[1mSuixinBlog: hi\033[0m")
print("\033[4mSuixinBlog: hi\033[0m")
print("\033[5mSuixinBlog: hi\033[0m")
print("\033[7mSuixinBlog: hi\033[0m")

print("字体色：")
print("\033[30mSuixinBlog: hi\033[0m")
print("\033[31mSuixinBlog: hi\033[0m")
print("\033[32mSuixinBlog: hi\033[0m")
print("\033[4;33mSuixinBlog: hi\033[0m")
print("\033[34mSuixinBlog: hi\033[0m")
print("\033[1;35mSuixinBlog: hi\033[0m")
print("\033[4;36mSuixinBlog: hi\033[0m")
print("\033[37mSuixinBlog: hi\033[0m")
print("背景色：")
print("\033[1;37;40m\tSuixinBlog: hi\033[0m")
print("\033[37;41m\tSuixinBlog: hi\033[0m")
print("\033[37;42m\tSuixinBlog: hi\033[0m")
print("\033[37;43m\tSuixinBlog: hi\033[0m")
print("\033[37;44m\tSuixinBlog: hi\033[0m")
print("\033[37;45m\tSuixinBlog: hi\033[0m")
print("\033[37;46m\tSuixinBlog: hi\033[0m")
print("\033[1;30;47m\tSuixinBlog: hi\033[0m")

import time
'''
c="hello world"
for x in c:
    print(x,end="")
    time.sleep(0.35)
'''
def PrintFunction(string):
    S=string
    for x in S:
        print(x,end="")
        time.sleep(0.35)
    print()
PrintFunction("Good night Sir")
PrintFunction("Hello but")
input("hello")

      # SYSU Python Big-data Tutorial #
                  Section 2 
         Copyright by PassionPenguin
            All Rights Reservered

         Last Updated: Jan 30, 2021

# 3 Python 程序设计教程

## 3.1 声明和调用函数

### 3.1.1 定义函数

* 可以使用def关键字来创建Python自定义函数，其基本语法结构如下：

```
def 函数名 (参数列表):
	函数体
```

* 参数列表可以为空，即没有参数；也可以包含多个参数，参数之间使用逗号（,）分隔。函数体可以是一条语句，也可以由一组语句组成。

创建一个非常简单的函数PrintWelcome，它的功能是打印字符串“欢迎使用Python”，代码如下：

```python
def PrintWelcome():
    print("欢迎使用Python")
```

定义函数PrintString()，通过参数决定要打印的内容。

```python
def PrintString(str):
    print(str)
```

变量 `str` 是函数的参数。在函数体中，参数可以像其他变量一样被使用。 可以在函数中定义多个参数，参数之间使用逗号分隔。

定义一个函数sum()，用于计算并打印两个参数之和。函数sum()包含两个参数。参数num1和num2，代码如下：

```python
def _sum(num1, num2):
    print(num1 + num2)
```

### 3.1.2 调用函数

可以直接使用函数名来调用函数，无论是系统函数还是自定义函数，调用函数的方法都是一致的。

```python
def PrintWelcome():
    print("欢迎使用Python");


PrintWelcome();
```

```python
def PrintString(str):
    print(str)


PrintString("传递参数")
```

```python
def sum(num1, num2):
    print(num1 + num2)


sum(1, 3)
```

### 3.1.3 变量的作用域

在函数中也可以定义变量，在函数中定义的变量被称为局部变量。局部变量只在定义它的函数内部有效，在函数体之外，即使使用同名的变量，也会被看作是另一个变量。相应地，在函数体之外定义的变量是全局变量。全局变量在定义后的代码中都有效，包括它后面定义的函数体内。如果局部变量和全局变量同名，则在定义局部变量的函数中，只有局部变量是有效的。

```python
a = 100  # 全局变量


def setNumber():
    a = 10  # 局部变量
    print(a)  # 打印局部变量a


setNumber()
print(a)  # 打印全局变量$a
```

## 3.2 参数

### 3.2.1 在函数中传递参数

1．普通参数
Python实行按值传递参数。值传递指调用函数时将常量或变量的值（通常称其为实参）传递给函数的参数（通常称其为形参）。值传递的特点是实参与形参分别存储在各自的内存空间中，是两个不相关的独立变量。因此，在函数内部改变形参的值时，实参的值一般是不会改变的。6.1.2小节介绍的实例都属于按值传递参数的情况。

```python
def func(num):
    num += 1


a = 10
func(a)
print(a)
```

```python
def func(num):
    print("形参num的地址", id(num))


a = 10
func(a)
print("实参a的地址", id(a))
```

使用列表作为函数参数的例子。

```python
def sum(list):
    total = 0
    for x in range(len(list)):
        print(list[x], "+")
        total += list[x]
    print("=", total)


list = [15, 25, 35, 65]
sum(list)
```

```python
def print_dict(dict):
    for (k, v) in dict.items():
        print("dict[%s] =" % k, v)


dict = {"a": "apple", "b": "banana", "g": "grape", "o": "orange"}
print_dict(dict)
```

```python
def swap(list):
    temp = list[0]
    list[0] = list[1]
    list[1] = temp


list = [1, 2]
print(list)
swap(list)
print(list)
```

```python
def changeA(dict):
    dict['a'] = 1


d = {'a': 10, 'b': 20, 'c': 30}
changeA(d)
print(d)
```

#### 参数的默认值

在Python中，可以为函数的参数设置默认值。可以在定义函数时，直接在参数后面使用“=”为其设置默认值。在调用函数时可以不指定拥有默认值的参数的值，此时在函数体中以默认值作为该参数

```python
def say(message, times=1):
    print(message * times)


say('hello')
say('Python', 3)
```

函数 `say()` 有2个参数：`message` 和 `times`。其中 `times` 的默认值为 1。

```python
def func1(a=1, b, c=10):
    return d = a + b * c;


print(func1(10, 20, 30))
```

Python还支持可变长度的参数列表。可变长参数可以是元祖或字典。当参数以*开头时，表示可变长参数将被视为一个元祖，格式如下： def func(*t):
在func ()函数中t被视为一个元祖，使用t[index]获取每一个可变长参数。 可以使用任意多个实参调用func()函数，例如：

```python
func(1, 2, 3, 4)
```

```python
def func1(*t):
    print("可变长参数数量如下：")
    print(len(t))
    print("依次为：")
    for x in range(len(t)):
        print(t[x])


func1(1, 2, 3, 4)
```

```python
def sum(*t):
    sum = 0
    for x in range(len(t)):
        print(str(t[x]) + "+")
        sum += t[x]
    print("=" + str(sum))


sum(1, 2)
sum(1, 2, 3, 4)
sum(11, 22, 33, 44, 55)
```

```python
def sum(*t):
    sum = 0
    for x in range(len(t)):
        print(str(t[x]) + "+")
        sum += t[x]
    if len(t) > 0:
        print("=" + str(sum))


sum()
```

```python
def sum(**t):
    print(t)


sum(a=1, b=2, c=3)
```

### 3.2.2 函数的返回值

对【例3-6】中的sum()函数进行改造，通过函数的返回值返回相加的结果，代码如下：

```python
def sum(num1, num2):
    return num1 + num2


print(sum(1, 3))
```

```python
def filter_even(list):
    list1 = []
    for i in range(len(list)):
        if list[i] % 2 == 0:
            list1.append(list[i])
            i -= 1
    return list1


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = filter_even(list)
print(list2)
```

## Python 的内置函数
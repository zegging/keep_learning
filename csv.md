# csv--csv文件读写

一些专业名词解释与翻译：
1. 定界符：指明某一字符串的开始或结束的一个或多个字符。
2. 转义符：用作转义字符序列中的前导符。将某些具有特殊含义的字符 (称之为元字符) 使其失去特殊含义而成为普通字符；将某些不具备特殊含义的字符 (在正则表达式中按其本义出现，它们匹配自身) 使其具有特殊含义。

escape char:转义字符
separator char 分隔符
quote char 引号符
delimiter 分隔符

## 模块定义的函数
### `csv.reader(csvfile, dialect='excel', **fmtparams)`
返回一个 `reader` 对象，该对象将逐行遍历 `csvfile`。`csvfile` 可以是任何对象，只要这个对象支持 `iterator` 协议并在每次调用 `__next__()` 方法时都返回字符串，`文件对象` 和 `列表对象` 均适用。如果 `csvfile` 是文件对象，则打开它时应使用 `newline=''`。如果没有指定 `newline=''`，则嵌入引号中的换行符将无法正确解析，并且在写入时，使用 `\r\n` 换行的平台会有多余的 `\r` 写入。由于 `csv` 模块会执行自己的（通用）换行符处理，因此指定 `newline=''` 应该总是安全的。

 可选参数 `dialect` 是用于不同的 `CSV` 变种的特定参数组。它可以是 `Dialect` 类的子类的实例，也可以是 `list_dialects()` 函数返回的字符串之一。另一个可选关键字参数 `fmtparams` 可以覆写当前变种格式中的单个格式设置。有关变种和格式设置参数的完整详细信息，请参见 `变种与格式参数` 部分。

csv 文件的每一行都读取为一个由字符串组成的列表。除非指定了 `QUOTE_NONNUMERIC` 格式选项（在这种情况下，未加引号的字段会转换为浮点数），否则不会执行自动数据类型转换。
```python
import csv
with open('test_csv.csv', newline='') as csvfile:
    readerfile = csv.reader(csvfile)
    print(readerfile)
```
output:
```text
<_csv.reader object at 0x00000213AA38D3C0>
```

```python
import csv
with open('test_csv.csv') as csvfile:
    readerfile = csv.reader(csvfile)
    for row in readerfile:
        print(row)
```
output:
```text
['A', 'B', 'C']
['D', 'E', 'F']
['G', '', '']
```
注意，当我们在直接输出 csvfile 中的 row 时其实默认输出了 `open()` 函数在文本模式下读取文件时将行结束符转换为的 `\n`。
```python
import csv
import re
with open('test_csv.csv') as csvfile:
    readerfile = csv.reader(csvfile)
    for row in csvfile:
        print(re.sub('\n', '', row))
```
output:
```text
A,B,C
D,E,F
G,,
```
```python
import csv
with open('test_csv.csv') as csvfile:
    readerfile = csv.reader(csvfile)
    for row in csvfile:
        print(row)
```
output:
```text
A,B,C

D,E,F

G,,
```



###  `QUOTE_*` 常量
`csv` 模块定义了以下常量：

`csv.QUOTE_ALL`

指示 `writer` 对象给所有字段加上引号。
```python
import csv
with open('test_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
    writer.writerow(['a', 'b', 'c\''])
```
output:
```text
a,b,c'
```

`csv.QUOTE_MINIMAL`

指示 `writer` 对象仅为包含特殊字符（例如 `定界符`、`引号字符` 或 `行结束符` 中的任何字符）的字段加上引号。
```python
import csv
with open('test_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_MINIMAL)
    writer.writerows([['a', 'b', 'c,', 'd"', "e'", '\r\n', 'f'], ['g', 'h']])
```
output:
```text
a,b,"c,","d""",e',"
",f
g,h,,,,,
```

`csv.QUOTE_NONNUMERIC`

指示` writer` 对象为所有非数字字段加上引号。
```python
import csv
with open('test_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(['x', 1])
```
output:
```text
"x",1
```
需要注意的是，在编译器中打开的时候可能没有quotechar包围，需要直接查看文本。

指示 `reader` 将所有未用引号引出的字段转换为 `float` 类型。
```python
import csv
with open('test_2.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
```
output:
```text
"x",1

['x', 1.0]
```
如果csv中的字段不能被转化为float类型将会报错：
```python
import csv
with open('test_2.csv', 'r', newline='') as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
```
output:
```text
x,1

ValueError: could not convert string to float: 'x'
```

`csv.QUOTE_NONE`

指示 `writer` 对象不使用引号引出字段。当 `定界符` 出现在输出数据中时，其前面应该有 `转义符`。如果未设置 `转义符`，则遇到任何需要转义的字符时，`writer` 都会抛出 `Error` 异常。
```python
import csv
with open('test_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 1, "'", 'y'])
```
output:
```text
x,1,',y
```
我们需要注意到，在WPS或者PyCharm中读取 test_2.csv 这个文件的时候，默认将 `'` 作为定界符读取，这样就会直接输出 `'` 到下一个 `'` 之间的内容作为一个字段，因此会将 `'y\r\n` 在界面上输出，于是读取的效果是这样的：
```text
x,1,",y
"
```
但用 `csv` 逐行输出内容的时候会输出：`['x', '1', "'", 'y']` 到控制台。

当我们设定 `quoting=csv.QUOTE_NONE` 的时候，会控制我们最终输出的文件该字段是否用定界符 `'` 引出字段：
```python
import csv
with open('test_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['x', 1, 'abc,def', "abc'def",'y'])
```
output:
```text
x,1,"abc,def",abc'def,y

```
在这里我们可以看到在csv文件中字符串 `abc,def` 前后是由定界符 `'` 的，这保证了我们用csv模块再次读取文件（默认分隔符是 `,`）的时候得到的字段是我们想要的：`['x', '1', 'abc,def', "abc'def", 'y']`。
```python
import csv
with open('test_2.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='!')
    writer.writerow(['x', 1, 'abc,def', 'abc’def','y'])
```
output:
```text
x,1,abc!,def,abc’def,y

```
在 `writer = csv.writer(csvfile, quoting=csv.QUOTE_NONE, escapechar='!')` 中我们将转义符设定为 `!` ，这样我们在csv文件中得到的输出是如上。所以我们再次读取csv文件并且逐行输出时控制台的输出为：`['x', '1', 'abc!', 'def', 'abc’def', 'y']`。如果我们不设定转义字符 `escapechar`，那么运行程序的时候将会报错：`_csv.Error: need to escape, but no escapechar set`，这是因为模块输出的分隔符 `,` 和字符串中的 `,` 没有区别。

## 变种与格式参数
为了更容易指定输入和输出记录的格式，特定的一组格式参数组合为一个 dialect（变种）。一个 dialect 是一个 `Dialect` 类的子类，它具有一组特定的方法和一个 `validate()` 方法。创建 `reader` 或 `writer` 对象时，程序员可以将某个字符串或 `Dialect` 类的子类指定为 dialect 参数。要想补充或覆盖 dialect 参数，程序员还可以单独指定某些格式参数，这些参数的名称与下面 `Dialect` 类定义的属性相同。

### `newline=''`
如果没有指定 `newline=''`，则嵌入引号中的换行符将无法正确解析，并且在写入时，使用 `\r\n` 换行的平台会有多余的 `\r` 写入。由于 csv 模块会执行自己的（通用）换行符处理，因此指定 `newline=''` 应该总是安全的。

### `Dialect` 类支持以下属性
#### `Dialect.delimiter`
一个用于分隔字段的单字符，默认为 ','。
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print(row, len(row))
```
output:
```text
a,'b,"c",d,e
f,g,,,
h,i,j,k,
l,,,,

['a', "'b", 'c', 'd', 'e'] 5
['f', 'g', '', '', ''] 5
['h', 'i', 'j', 'k', ''] 5
['l', '', '', '', ''] 5
```
当我们把关键字参数修改为空格 `' '` 时得到不同的输出。
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ')
    for row in reader:
        print(row, len(row))
```
output:
```text
a,'b,"c",d,e
f,g,,,
h,i,j,k,
l,,,,

['a,\'b,"c",d,e'] 1
['f,g,,,'] 1
['h,i,j,k,'] 1
['l,,,,'] 1
```
注意：`TypeError: "delimiter" must be a 1-character string`，delimiter参数只能设定为一个字符的字符串。

#### `Dialect.quotechar`
一个单字符，用于包住含有特殊字符的字段，特殊字符如` 定界符` 或 `引号字符` 或 `换行符`。默认为 `"`。
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar='"')
    for row in reader:
        for each in row:
            print(each)
        print(row, len(row))
```
output:
```text
a,'b,"c",'d'
e,',"\n",',

a
'b
c
'd'
['a', "'b", 'c', "'d'"] 4
e
'
\n
'

['e', "'", '\\n', "'", ''] 5
```
注意，在csv文件的第二行最后的 `,` 形成了一个空白字段。

当我们将quotechar设置为单引号 `'` 时可以得到不同的输出：
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, quotechar='\'')
    for row in reader:
        print(row, len(row))
```
output:
```text
a,'b,"c",'d'
e,',",,',,

['a', 'b,"c",d\''] 2
['e', ',",,', '', ''] 4
```
同时我们还要注意，一个quoterchar和接下来的一个quotechar之间的字符都会被认为是同一个字段中的内容，若果没有下一个quoterchar则直至末尾（此时会将\r\n代表的换行符也视为字段的一部分）。我们可以在接下来的这个例子中看到：
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        for each in row:
            print(each)
        print(row, len(row))
```
output:
```text
a,'b,"c,'d'
e,',\n,',

a
'b
c,'d'
e,',\n,',
['a', "'b", "c,'d'\r\ne,',\\n,',"] 3
```
#### `Dialect.doublequote`
控制出现在字段中的 `引号字符` 本身应如何被引出。当该属性为 `True` 时，双写引号字符。如果该属性为 `False`，则在 `引号字符` 的前面放置 转义符。默认值为 `True`。
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, doublequote=False, quotechar='!')
    for row in reader:
        for each in row:
            print(each)
        print(row, len(row))
```
output:
```text
a,'b,
!"'c'!,

a
'b

['a', "'b", ''] 3
"'c'

['"\'c\'', ''] 2
```
属性为 `True` 时：
```python
import csv
with open('test_1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, doublequote=True, quotechar='!')
    for row in reader:
        for each in row:
            print(each)
        print(row, len(row))
```
output:
```text
a,'b,
!"'c'!,

a
'b

['a', "'b", ''] 3
"'c'

['"\'c\'', ''] 2

```
……没区别啊？

#### `Dialect.quoting`
控制 `writer` 何时生成引号，以及 `reader` 何时识别引号。该属性可以等于任何 `QUOTE_*` 常量，默认为 `QUOTE_MINIMAL`。









指示 `reader` 不对引号字符进行特殊处理。

#### `Dialect.escapechar`
一个用于 `writer` 的单字符，用来在 `quoting` 设置为` QUOTE_NONE` 的情况下转义 `定界符`，在 `doublequote` 设置为 `False` 的情况下转义 `引号字符`。在读取时，`escapechar` 去除了其后所跟字符的任何特殊含义。该属性默认为 `None`，表示禁用转义。




Dialect.lineterminator
放在 writer 产生的行的结尾，默认为 '\r\n'。




**为什么？？**

```python
import csv
with open('test_csv.csv') as csvfile:
    readerfile = csv.reader(csvfile)
    for row in csvfile:
        print(row)

    print('-------------1-------------')

    for row_readerfile in readerfile:
        print(row_readerfile)

    print('-------------2-------------')
```
output:
```text
A,B,C

D,E,F

G,,
-------------1-------------
-------------2-------------
```



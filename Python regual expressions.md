# 正则表达式 Python
我们在 Python 中通过导入 re 模块来使用正则表达式来匹配字符串中的内容。

正则表达式语言相对较小且受限，因此并非所有可能的字符串处理任务都可以使用正则表达式完成。有些任务尽管*可以*用正则表达式来完成，但表达式会变得非常复杂。这些情况下，最好通过编写 Python 代码来进行处理。也许 Python 代码会比精心设计的正则表达式慢，但它可能更容易理解。

[regexlearn](https://regexlearn.com/zh-cn)是一个在线练习网站，[regex101](https://regex101.com)是一个正则表达式在线验证网站，可在学习过程中适当使用。

## 元字符
大多数字母和符号都会简单地匹配到自身，但是元字符会匹配一些非常规的内容，在正则表达式语言中具有特殊的作用。

以下是元字符的完整列表：
```
. ^ $ * + ? {} [] \ | ()
```
#### `[]`
`[]`可以用来指定一个字符类别，也就是一个希望匹配的字符的集合。这些字符可以单独列出也可以通过范围来表示。
* `[abc]`将匹配a、b、c中的任意一个字符
* `[a-c]`也将匹配a、b、c中的任意一个字符，即`[abc]`与`[a-c]`有相同的效果。

元字符（除了`\ `）在字符类中是不起作用的。 例如，`[akm$]` 将会匹配以下任一字符 'a', 'k', 'm' 或 $ 。$ 通常是一个元字符，但在一个字符类中它的特殊性被消除了。

#### `^`
我们可以通过对集合取反来匹配字符类中未列出的字符，方法是把`^`放在字符类的最开头
* `[^5]`将匹配除了 5 以外的任意字符
* `[5^]`将匹配 5 或 ^ 。

#### `\ `
`\ `用于转义元字符，以便可以在表达式中匹配元字符本身，例如，如果需要匹配一个 [ 或 \ ，可以在其前面加上一个反斜杠来消除它们的特殊含义：`\[` 或 `\\`匹配到的字符是`[`或`\ `。

同时反斜杠后面可以跟各种字符来表示各种特殊序列。

#### `\ `语句速查表

| 正则表达式语法        | 匹配字符 |
|----------------| ------ |
| Header         | Title  |
| Paragraph      | Text   |

#### `\number`
`\number`匹配数字代表的组合。每个括号是一个组合，组合从1开始编号。比如`(.+) \1`匹配 `'the the'` 或者 `'11 11'`, 但不会匹配 `'thethe'` (注意组合后面的空格)。这个特殊序列只能用于匹配前面99个组合。如果 number 的第一个数位是0， 或者 number 是三个八进制数，它将不会被看作是一个组合，而是八进制的数字值。在 '[' 和 ']' 字符集合内，任何数字转义都被看作是字符。
```python
import re
source_1 = '''
the the thethe 11 11 22 3 22 111111 4 4 4
'''
pattern = re.compile(r'(.+) \1 ')
lst = re.findall(pattern , source_1)
for each in lst:
    print(each)
'''
如果两个相同字符串组合之间只有空白字符间隔，就会被编号并且输出
'''
```
输出：
```
the
11
4
```

#### `\w`
`\w`对于 Unicode (str) 样式： 匹配Unicode词语的字符，包含了可以构成词语的绝大部分字符，也包括数字和下划线,等价于字符类`[a-zA-Z0-9_]`。
```python
import re
source_4 = '''a我，aa（（_awef。11abc cdef aghijk,bb225,a1111
'''
pattern = re.compile(r'a\w')
lst = re.findall(pattern , source_4)
print(lst)

pattern = re.compile(r'a\w*')
lst_1 = re.findall(pattern , source_4)
print(lst_1)

pattern = re.compile(r'\wa\w*')
lst_2 = re.findall(pattern , source_4)
print(lst_2)

pattern = re.compile(r'\w*a\w*')
lst_3 = re.findall(pattern , source_4)
print(lst_3)
```
输出：
```
['a我', 'aa', 'aw', 'ab', 'ag', 'a1']
['a我', 'aa', 'awef', 'abc', 'aghijk', 'a1111']
['aa', '_awef', '1abc']
['a我', 'aa', '_awef', '11abc', 'aghijk', 'a1111']
```

#### `\W`
`\W`匹配非单词字符的字符。这与 `\w` 正相反,`[^a-zA-Z0-9_]` 。

#### `\b`
`\b`匹配空字符串，但只在单词开始或结尾的位置。一个单词被定义为一个单词字符的序列。注意，通常 `\b` 定义为 `\w` 和 `\W` 字符之间，或者` \w` 和字符串开始/结尾的边界， 意思就是`r'\bfoo\b'` 匹配 `'foo', 'foo.', '(foo)', 'bar foo baz'` 但不匹配 `'foobar'` 或者 `'foo3'`。`\b`代表着单词的开头或结尾，也就是单词的分界处。虽然通常英文的单词是由空格，标点符号或者换行来分隔的，但是`\b`并不匹配这些单词分隔字符中的任何一个，它只匹配一个位置。
```python
import re
source_3 = '''hi hill, 889hi87 hihihi,hi, hi.（（（hi
'''
pattern = re.compile(r'hi')
p_1 = re.compile(r'\bhi')
p_2 = re.compile(r'\bhi\b')
lst = re.findall(pattern , source_3)
print(lst)          # 所有的hi
lst_1 = re.findall(p_1 , source_3)
print(lst_1)        # 所有的前没有Unicode字母，数字或下划线的hi
lst_2 = re.findall(p_2, source_3)
print(lst_2)        # 所有前后都没有Unicode字母，数字或下划线的hi
```
输出：
```
['hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi']
['hi', 'hi', 'hi', 'hi', 'hi', 'hi']
['hi', 'hi', 'hi', 'hi']
```

#### `\B`
`\B`匹配空字符串，但不能在词的开头或者结尾。意思就是 `r'py\B'` 匹配 `'python', 'py3', 'py2'`, 但不匹配 `'py', 'py.', 'py!'`. `\B` 是 `\b` 的取非，所以Unicode样式的词语是由Unicode字母，数字或下划线构成的。
```python
import re
source_3 = '''hi hill, 889hi87 hihihi,hi, hi.（（（hi
'''
pattern = re.compile(r'hi')
p_1 = re.compile(r'\Bhi')
p_2 = re.compile(r'\Bhi\B')
lst = re.findall(pattern , source_3)
print(lst)          # 所有的hi
lst_1 = re.findall(p_1 , source_3)
print(lst_1)        # 所有的前有Unicode字母，数字或下划线的hi
lst_2 = re.findall(p_2, source_3)
print(lst_2)        # 所有前后都有Unicode字母，数字或下划线的hi
```
输出：
```
['hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi', 'hi']
['hi', 'hi', 'hi']
['hi', 'hi']
```

#### `\d`
`\d`对于 Unicode (str) 样式： 匹配任何 Unicode 十进制数 `[0-9]`。
```python
import re
source_5 = '''九千一百八十六 玖千壹佰捌拾陆 9186 ⅠⅡ Ⅵ。九十9186'''
pattern = re.compile(r'\d+')
lst = re.findall(pattern, source_5)
print(lst)
```
输出：
```
['9186', '9186']
```

##### `\D`
`\D`匹配任何非十进制数字的字符。就是 `\d` 取非。等价于`[^0-9]`
```python
import re
source_5 = '''九千一百八十六 玖千壹佰捌拾陆 9186 ⅠⅡ Ⅵ。九十9186'''
pattern = re.compile(r'\D+')
lst = re.findall(pattern, source_5)
print(lst)
```
输出：
```
['九千一百八十六 玖千壹佰捌拾陆 ', ' ⅠⅡ Ⅵ。九十']
```

##### `\s`
`\s`对于 Unicode (str) 样式： 匹配任何 Unicode 空白字符，等价于字符类 `[ \t\n\r\f\v]`。
```python
import re
source_6 = '''九千一百八十六 玖千壹\t佰捌拾陆 9186 
ⅠⅡ Ⅵ。\n 九十9186'''
pattern = re.compile(r'\s')
lst = re.findall(pattern, source_6)
print(lst)
```
output
```
[' ', '\t', ' ', ' ', '\n', ' ', '\n', ' ']
```

##### `\S`
`\S`匹配任何非空白字符。就是 \s 取非，等价于字符类 `[^ \t\n\r\f\v]`。
```python
import re
source_6 = '''九千一百八十六 玖千壹\t佰捌拾陆 9186 
ⅠⅡ Ⅵ。\n 九十9186'''
pattern = re.compile(r'\S+')
lst = re.findall(pattern, source_6)
print(lst)
```
output:
```
['九千一百八十六', '玖千壹', '佰捌拾陆', '9186', 'ⅠⅡ', 'Ⅵ。', '九十9186']
```

##### `\Z`
`\Z`只匹配字符串尾。

如果你没有使用原始字符串（ `r'raw'` ）来表达样式，要牢记 Python 也使用反斜杠作为转义序列；如果转义序列不被 Python 的分析器识别，反斜杠和字符才能出现在字符串中。如果 Python 可以识别这个序列，那么反斜杠就应该重复两次。这将导致理解障碍，所以高度推荐，就算是最简单的表达式，也要使用原始字符串。

##### `.`
`.`匹配除换行符之外的任何字符，并且有一个可选模式（ `re.DOTALL` ），在该模式下它甚至可以匹配换行符。 `.` 通常用于你想匹配“任何字符”的场景。

#### `*`
重复元字符 `*` 指定前一个字符可以匹配零次或更多次，而不是只匹配一次。
```python
import re
source_7 = '''abcbd'''
pattern = re.compile(r'a[bcd]*b')
lst = re.findall(pattern, source_7)
```
output:
```text
['abcb']
```

###### 匹配的贪婪模式
类似 `*` 这样的重复是贪婪的，当重复正则时，匹配引擎将尝试重复尽可能多的次数。如果表达式的后续部分不匹配，则匹配引擎将回退并以较少的重复次数再次尝试。参考 [正则基础之——贪婪与非贪婪模式](https://blog.csdn.net/lxcnn/article/details/4756030)

##### `+`
另一个重复元字符 `+` 表示匹配一次或更多次。请注意 `*` 与 `+` 之间的差别。`*` 表示匹配 零次或更多次，也就是说它所重复的内容是可以完全不出现的。而 `+` 则要求至少出现一次。举一个类似的例子，`ca+t` 可以匹配 `'cat'` （ 1 个 'a' ）或 `'caaat'` （ 3 个 'a'），但不能匹配 `'ct'` 。

##### `?`
重复限定符 `?` 表示匹配一次或零次。你可以认为它把内容变成了可选的。例如，`home-?brew` 可以 匹配 `'homebrew'` 或 `'home-brew'`。

##### `{m,n}`
重复限定符是 `{m,n}`，其中 m 和 n 是十进制整数。 该限定符意味着必须至少重复 m 次，最多重复 n 次。 例如，`a/{1,3}b` 可以匹配 `'a/b', 'a//b', 'a///b'` ，但不能匹配中间没有斜杆的 `'ab'`，或者四个斜杆的 `'a////b'` 。m 和 n 不是必填的，缺失的情况下会设定为默认值。缺失 m 会解释为最少重复 0 次 ，缺失 n 则解释为最多重复无限次。

三个重复限定符都可以用这种标记法来表示。 `{0,}` 等同于 `*` ，`{1,}` 等同于 `+` ，`{0,1}` 等同于 `?` 。 如果可以的话，最好使用 `* + ?` ，因为后者更简洁易读。

### 零宽度断言

我们接下来要讨论的其余一些元字符是**零宽度断言**。 它们不会使解析引擎在字符串中前进一个字符；相反，它们根本不占用任何字符，只是成功或失败。例如，`\b` 是一个断言，指明当前位置位于字边界；这个位置根本不会被 `\b` 改变。这意味着永远不应重复零宽度断言，因为如果它们在给定位置匹配一次，它们显然可以无限次匹配。
#### `|`
`|`或者“or”运算符。 如果 `A` 和 `B` 是正则表达式，`A|B` 将匹配任何与 `A` 或 `B` 匹配的字符串。 `|` 具有非常低的优先级，以便在交替使用多字符字符串时使其合理地工作。 `Crow|Servo` 将匹配 `'Crow'` 或 `'Servo'`，而不是 `'Cro', 'w', 'S', 'ervo'`。如果不用`()`来限制`|`的范围，结果容易出错。

#### `^`
`^`在字符串的开头匹配，如果设置 `re.compile( , re.M)` 关键字参数，则会在每个换行符后立刻进行一次匹配（即每行开头进行一次匹配）。
```python
import re
source_8 = '''From Here to Eternity, 
From Reciting From Memory'''
print(source_8)
pattern_1 = re.compile(r'^From', re.MULTILINE)
lst_1 = re.findall(pattern_1, source_8)
print(lst_1)
pattern_2 = re.compile(r'^From')
lst_2 = re.findall(pattern_2, source_8)
print(lst_2)
```
output
```text
From Here to Eternity, 
From Reciting From Memory
['From', 'From']
['From']
```
#### `$`
`$`匹配行的末尾，定义为字符串的结尾，或者后跟换行符的任何位置（设置 `re.compile( , re.M)` 关键字参数）。
```python
import re 
source_9 = '''{block}\n
{block} 
{block}'''
print(source_9)
pattern_1 = re.compile(r'}$',re.M)
lst_1 = re.findall(pattern_1, source_9)
print(lst_1)
pattern_2 = re.compile(r'}$')
lst_2 = re.findall(pattern_2, source_9)
print(lst_2)
```
output:
```text
{block}

{block} 
{block}
['}', '}']
['}']
```

#### `\A`
`\A`仅匹配字符串的开头。 当不在 MULTILINE 模式时，`\A` 和 `^` 实际上是相同的。 在 MULTILINE 模式中，它们是不同的: `\A` 仍然只在字符串的开头匹配，但 `^` 可以匹配在换行符之后的字符串内的任何位置。

#### `\Z`
`\Z`只匹配字符串尾。效果参考`\A`。

#### `\b`
`\b`字边界。 这是一个零宽度断言，仅在单词的开头或结尾处匹配。单词被定义为一个字母数字字符序列，因此单词的结尾由空格或非字母数字字符表示。
```python
import re
source_10 = ''''no class at all, the declassified algorithm. one subclass is'''
pattern = re.compile(r'\bclass\b')
lst = re.findall(pattern, source_10)
print(lst)
```
output
```text
['class']
```

使用这个特殊序列时，你应该记住两个细微之处。 首先，这是 Python 的字符串文字和正则表达式序列之间最严重的冲突。 在 Python 的字符串文字中，`\b` 是退格字符，ASCII 值为8。 如果你没有使用原始字符串，那么 Python 会将 `\b` 转换为退格，你的正则不会按照你的预期匹配。
```python
import re
source_10 = ''''no class at all, the declassified algorithm. one subclass is'''
pattern = re.compile('\bclass\b')
print('\bclass\b')
lst = re.findall(pattern, source_10)
print(lst)
```
output:
```text
clas
[]
```

#### `\B`
`\B`另一个零宽度断言，这与 `\b` 相反，仅在当前位置不在字边界时才匹配。
```python
import re
source_10 = ''''no class at all, the declassified algorithm. one subclass is'''
pattern = re.compile(r'\Bclass\B')
lst = re.findall(pattern, source_10)
print(lst)
```
output:
```text
['class']
```

### 分組

#### `()`
正则表达式通常用于通过将正则分成几个子组来解析字符串，这些子组匹配不同类别。

组由 `'( )'` 元字符标记。与数学表达式的含义大致相同；它们将包含在其中的表达式组合在一起，你可以使用重复限定符重复组的内容，例如 `*`，`+`，`?` 或 `{m,n}`。 例如，`(ab)*` 将匹配 `ab` 的零次或多次重复。

用 `( )` 表示的组也捕获它们匹配的文本的起始和结束索引；这可以通过将参数传递给 `group()、start()、end() span()`。 组从 0 开始编号。组 0 始终存在；它表示整个正则，所以匹配对象方法都将组 0 作为默认参数。 
```python
import re
source_11 = '''abcd'''
pattern = re.compile(r'(a(b)c)d')
m = re.match(pattern, source_11)
print(m)
print(m.group(), m.group(0), m.group(1), m.group(2))
```
output:
```text
<re.Match object; span=(0, 4), match='abcd'>
abcd abcd abc b
```

我们可以发现，子组从左到右编号，从 1 向上编号。 组可以嵌套；要确定编号，只需计算从左到右的左括号字符。

当我们分组捕获匹配的文本并且使用`.findall()`输出结果时将按照分组的编号按顺序输出每个匹配到的组。
```python
import re
source_11 = '''abcd'''
pattern = re.compile(r'(a(b)c)d')
lst = re.findall(pattern, source_11)
print(lst)
```
output:
```text
[('abc', 'b')]
```

我们需要注意的是： If a group is contained in a part of the pattern that did not match, the corresponding result is None. If a group is contained in a part of the pattern that matched multiple times, the last match is returned.
```python
string = '''abc'''
pattern = re.compile(r'([abc])+')
m = re.match(pattern, string)
print(m.group(), m.group(1))
lst = re.findall(pattern, string)
print(lst)

string = '''abca'''
pattern = re.compile(r'([abc])+')
m = re.match(pattern, string)
print(m.group(), m.group(1))
lst = re.findall(pattern, string)
print(lst)

string = '''abc'''
pattern = re.compile(r'([abc])([abc])([abc])')
m = re.match(pattern, string)
print(m.group(), m.group(1), m.group(2), m.group(3))
lst = re.findall(pattern, string)
print(lst)

string = 'abc123'
pattern = re.compile(r'([abc])+([123])+')
m = re.match(pattern, string)
print(m.group(), m.group(1), m.group(2))
lst = re.findall(pattern, string)
print(lst)
```
output:
```text
abc c
['c']
abca a
['a']
abc a b c
[('a', 'b', 'c')]
abc123 c 3
[('c', '3')]
```
显然这里的区别是`([abc])+`被视为是一个确定的组，`+`指出了组的匹配模式是贪婪的并且至少匹配一次，正则对象不断匹配，并且将最后一个匹配对象`c`输出。在之后的匹配对象这一章节我们将详细讨论。

### 非捕获组
有时你会想要使用组来表示正则表达式的一部分，但是对检索组的内容不感兴趣。 你可以通过使用非捕获组来显式表达这个事实: `(?:...)`，你可以用任何其他正则表达式替换 `...`。 `(?:...)` 在修改现有模式时特别有用，因为你可以添加新组而不更改所有其他组的编号方式。 值得一提的是，捕获和非捕获组之间的搜索没有性能差异；两种形式没有一种更快。
```python
import re
source_13 = '''2022-09-26'''
pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
lst = re.findall(pattern, source_13)
print(lst)
pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
lst = re.findall(pattern, source_13)
print(lst)
m = re.match(pattern, source_13)
print(m.group(), m.group(1), m.group(2), m.group(3))

pattern = re.compile(r'(?:\d{4})-(?:\d{2})-(?:\d{2})')
lst = re.findall(pattern, source_13)
print(lst)
m = re.match(pattern, source_13)

# print(m.group(), m.group(1))
# IndexError: no such group
```
output:
```text
['2022-09-26']
[('2022', '09', '26')]
2022-09-26 2022 09 26
['2022-09-26']
2022-09-26
```

### 前视断言
另一个零宽断言是前视断言。 前视断言有肯定型和否定型两种形式

##### `(?=…)`
`(?=…)`肯定型前视断言。如果内部的表达式（这里用 `...` 来表示）在当前位置可以匹配，则匹配成功，否则匹配失败。 但是内部表达式尝试匹配之后正则引擎并不会向前推进；正则表达式的其余部分依然会在断言开始的地方尝试匹配。
```python
import re
source = '''This is a car, that is a fat cat. '''
pattern = re.compile(r'a(?=r)')
lst = re.findall(pattern, source)
print(lst)
pattern = re.compile(r'a(?=t)')
lst = re.findall(pattern, source)
print(lst)
pattern = re.compile(r'a(?=r|t)')
lst = re.findall(pattern, source)
print(lst)
pattern = re.compile(r'(?=c)a')
lst = re.findall(pattern, source)
print(lst)
```
output
```text
['a']
['a', 'a', 'a']
['a', 'a', 'a', 'a']
[]
```

##### `(?!…)`
`(?!…)`否定型前视断言。 与肯定型断言正好相反，如果内部表达式在字符串中的当前位置不匹配，则成功。

更具体一些，来看一个前视的实用案例。 考虑用一个简单的表达式来匹配文件名并将其拆分为基本名称和扩展名，以 `.` 分隔。 例如，在 `news.rc` 中，`news` 是基本名称，`rc` 是文件名的扩展名。
```python
import re
source = '''news.rc
weibo.com
baidu.com
bnu.edu
'''
pattern = re.compile(r'.*[.].*$', re.M)
lst = re.findall(pattern, source)
print(lst)
```
output:
```text
['news.rc', 'weibo.com', 'baidu.com', 'bnu.edu']
```

现在，考虑使更复杂一点的问题；如果你想匹配扩展名不是 bat 的文件名怎么办？ 一些错误的尝试：

`.*[.][^b].*$` 上面的第一次尝试试图通过要求扩展名的第一个字符不是 b 来排除 bat。 这是错误的，因为模式也与 `foo.bar` 不匹配。

`.*[.]([^b]..|.[^a].|..[^t])$`

当你尝试通过要求以下一种情况匹配来修补第一个解决方案时，表达式变得更加混乱：扩展的第一个字符不是 b。 第二个字符不 a；或者第三个字符不是 t。 这接受 `foo.bar `并拒绝 `autoexec.bat`，但它需要三个字母的扩展名，并且不接受带有两个字母扩展名的文件名，例如 `sendmail.cf`。 为了解决这个问题，我们会再次使模式复杂化。

`.*[.]([^b].?.?|.[^a]?.?|..?[^t]?)$`

在第三次尝试中，第二个和第三个字母都是可选的，以便允许匹配的扩展名短于三个字符，例如 `sendmail.cf`。

模式现在变得非常复杂，这使得它难以阅读和理解。 更糟糕的是，如果问题发生变化并且你想要将 bat 和 exe 排除为扩展，那么该模式将变得更加复杂和混乱。

否定型前视可以解决所有这些困扰：

`.*[.](?!bat$)[^.]*{TX-PL-LABEL}#x60` 否定型前视意味着：如果表达式 bat 在当前位置不能匹配，则可以接着尝试正则表达式的其余部分；如果` bat{TX-PL-LABEL}#x60;` 能匹配，则整个正则表达式将匹配失败。 尾随的 `{TX-PL-LABEL}#x60;` 是必需的，以确保可以匹配到像 `sample.batch` 这样以 bat 开头的文件名。当文件名中有多个点号时， `[^.]*` 可以确保表达式依然有效。
```python
import re
source = '''news.rc
weibo.com
baidu.com
bnu.edu
sample.batch
sendmail.cf
autoexec.bat
exa.
foo.bar
'''
pattern = re.compile(r'.*[.](?!bat$)[^.\n]+$', re.M)
lst = re.findall(pattern, source)
print(lst)
```
output:
```text
['news.rc', 'weibo.com', 'baidu.com', 'bnu.edu', 'sample.batch', 'sendmail.cf', 'foo.bar']
```

现在很容易排除另一个文件扩展名；只需在断言中添加它作为替代。 以下模块排除以 bat 或 exe:

```.*[.](?!bat$|exe$)[^.]*$```

在匹配url的工作中遇到了一个问题，`urlparse()` 仅在 `netloc` 前面正确地附带了 `//` 的情况下才会识别它。 否则输入会被当作是一个相对 URL 因而以路径的组成部分开头。所以我需要在没有 `//` 的 `netloc` q前加入，以此来符合 `urlparse()` 的识别逻辑：
```python
each = 'wwww.baidu.com'
print(each)
each_conf = re.sub('^(?!(?:(?:http[s]?|ftp)://))(?:(?:http[s]?|ftp)://)?', 'add://', each)
print(each_conf)
parsed_href = urlparse(each_conf)
print(parsed_href)
print(parsed_href.netloc.split('.'))
l = '.'.join(parsed_href.netloc.split('.')[-2:])
print(l)
```
output:
```text
www.baidu.com
add://www.baidu.com
ParseResult(scheme='add', netloc='www.baidu.com', path='', params='', query='', fragment='')
['www', 'baidu', 'com']
baidu.com
```
在这个例子里我先使用前置否定断言 `(?!(?:(?:http[s]?|ftp)://))` 在字符串开头匹配，如果url带有

#### `(?(id/name)yes-pattern|no-pattern)`
条件性匹配，如果给定的 `id` 或 `name` 存在，将会尝试匹配 `yes-pattern` ，否则就尝试匹配 `no-pattern`，`no-pattern` 可选，也可以被忽略。比如， `(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)` 是一个email样式匹配，将匹配 `<user@host.com>` 或 `user@host.com` ，但不会匹配 `<user@host.com` ，也不会匹配 `user@host.com>`。
```python
p = re.compile('(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)')
c1 = 'user@host.com'
c2 = '<user@host.com>'

print(re.findall(p, c1))
print(re.findall(p, c2))
```
output:
```text
[('', 'user@host.com')]
[('<', 'user@host.com')]
```
在这个例子中 `<user@host.com>` 匹配 `<` 成功，得到了第一个默认命名组 `\1` 并在之后的条件匹配 `(?(1)>|$)` 中确认存在，所以选择执行 `yes-pattern` 部分。而`user@host.com` 匹配 `<` 不成功，没有获得默认命名组，并在之后的条件匹配 `(?(1)>|$)` 中确认捕获组 `\1` 不存在，所以选择执行 `no-pattern` 部分。

## 函数
| 参数          | 描述       |
|-------------|----------|
| pattern     | 匹配的正则表达式 |
| string  | 要匹配的字符串    |
|    flags         |     标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。     |
#### `re.compile(pattern, flags=0)`
将正则表达式的央视编译为一个正则表达对象（正则对象）可以用使用这个对象的如下方法`match(), search()`
```python
import re
pattern = re.compile(r'abcd')
print(pattern, type(pattern))
```
output:
```text
re.compile('abcd') <class 're.Pattern'>
```
序列
```python
prog = re.compile(pattern)
result = prog.match(string)
```
等价于：
```python
result = re.match(pattern, string)
```
如果需要多次使用这个正则表达式的话，使用 `re.compile()` 和保存这个正则对象以便复用，可以让程序更加高效。

#### `re.search(pattern, string, flags=0)`
扫描整个 字符串 找到匹配样式的第一个位置，并返回一个相应的匹配对象。如果没有匹配，就返回 None ； 注意这和找到一个零长度匹配是不同的。

#### `re.match(pattern, string, flags=0)`
如果 string 开始的0或者多个字符匹配到了正则表达式样式，就返回一个相应的匹配对象 。 如果没有匹配，就返回 None ；注意它跟零长度匹配是不同的。

#### `re.fullmatch(pattern, string, flags=0)`
如果整个 string 匹配到正则表达式样式，就返回一个相应的匹配对象 。 否则就返回 None ；注意这跟零长度匹配是不同的。

#### `re.split(pattern, string, maxsplit=0, flags=0)`
用 `pattern 分开` string 。 如果在 `pattern` 中捕获到括号，那么所有的组里的文字也会包含在列表里。如果 `maxsplit` 非零， 最多进行 `maxsplit` 次分隔， 剩下的字符全部返回到列表的最后一个元素。
```python
l_1 = re.split(r'\W+', 'Words, words, words.')
l_2 = re.split(r'(\W+)', 'Words, words, words.')
l_3 = re.split(r'\W+', 'Words, words, words.', 1)
l_4 = re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
l_5 =  re.split(r'(\W+)', '...words, words...')
print(l_1)
print(l_2)
print(l_3)
print(l_4)
print(l_5)
```
output:
```text
['Words', 'words', 'words', '']
['Words', ', ', 'words', ', ', 'words', '.', '']
['Words', 'words, words.']
['0', '3', '9']
['', '...', 'words', ', ', 'words', '...', '']
```
特别注意的是，样式的空匹配仅在与前一个空匹配不相邻时才会拆分字符串。
```python
l_1 = re.split(r'\b', 'Words, words, words.')
l_2 = re.split(r'\W*', '...words...')
l_3 = re.split(r'(\W*)', '...words...')
print(l_1)
print(l_2)
print(l_3)
```
output:
```text
['', 'Words', ', ', 'words', ', ', 'words', '.']
['', '', 'w', 'o', 'r', 'd', 's', '', '']
['', '...', '', '', 'w', '', 'o', '', 'r', '', 'd', '', 's', '...', '', '', '']
```

#### `re.findall(pattern, string, flags=0)`
返回 pattern 在 string 中的所有非重叠匹配，以字符串列表或字符串元组列表的形式对 string 从左至右扫描，匹配结果按照找到的顺序返回。 空匹配也包括在结果中。

返回结果取决于正则表达式中捕获组的数量。如果没有组，返回与整个模式匹配的字符串列表。如果有且仅有一个组，返回与该组匹配的字符串列表。如果有多个组，返回与这些组匹配的字符串元组列表。非捕获组不影响结果。
```python
l_1 = re.findall(r'\bf[a-z]*', 'which foot or hand fell faster')
l_2 = re.findall(r'(\w+)=(\d+)', 'set width=20 and height=10')
print(l_1)
print(l_2)
```
output:
```text
['foot', 'fell', 'faster']
[('width', '20'), ('height', '10')]
```

#### `re.finditer(pattern, string, flags=0)`
pattern 在 string 里所有的非重复匹配，返回为一个迭代器 iterator 保存了 匹配对象 。 string 从左到右扫描，匹配按顺序排列。空匹配也包含在结果里。
```python
l = re.finditer(r'\bf[a-z]*', 'which foot or hand fell faster')
print(l)
```
output:
```text
<callable_iterator object at 0x000001634D223F40>
```
#### `re.sub(pattern, repl, string, count=0, flags=0)`
返回通过使用 repl 替换在 string 最左边非重叠出现的 pattern 而获得的字符串。 如果样式没有找到，则不加改变地返回 string。 repl 可以是字符串或函数；如为字符串，则其中任何反斜杠转义序列都会被处理。 也就是说，`\n` 会被转换为一个换行符，`\r` 会被转换为一个回车符，依此类推。 未知的 ASCII 字符转义序列保留在未来使用，会被当作错误来处理。 其他未知转义序列例如 `\`& 会保持原样。 向后引用像是 `\6` 会用样式中第 6 组所匹配到的子字符串来替换。 例如:
```python
l = re.sub(r'def\s+([a-zA-Z_][a-zA-Z_0-9]*)\s*\(\s*\):',
           r'static PyObject*\npy_\1(void)\n{',
           'def myfunc():')
print(l)

l_1 = re.sub(r'(\S[^的]*)的(\S[^是]*)是(\S[^?]*)？',
             r'\1的\2是曹操',
             '曹丕的父亲是谁？')
print(l_1)

l_2 = re.sub(r'(\S[^和]*)和(\S[^和]*)是邻国？',
             r'\1和\2接壤',
             r'中国和俄罗斯是邻国？')
print(l_2)
```
output:
```text
static PyObject*
py_myfunc(void)
{
曹丕的父亲是曹操
中国和俄罗斯接壤
[('中国', '俄罗斯')]
```
如果一个一个捕获组被匹配了多次，那么它将按照被匹配的次序输出，我们可以参考下面这个例子：
```python
content = 'GET/designpic/{obsDesignId:3(?:F|f)\w{10}}/{roomId:\w+}'
pattern = re.compile(r"/{[a-zA-Z]+:([^/]*)}")
l = re.findall(pattern, content)
print(l)
content_change = re.sub(pattern, r'/\1', content)
print(content_change)
content_change_test = re.sub(pattern, '/\1', content)
print(content_change_test)
```
output:
```text
['3(?:F|f)\\w{10}', '\\w+']
GET/designpic/3(?:F|f)\w{10}/\w+
GET/designpic//
```
注意，在这个例子中我们可以看到正则表达式 `r"/{[a-zA-Z]+:([^/]*)}"` 一共匹配了两次（分别是 `/{obsDesignId:3(?:F|f)\w{10}}` 和 `/{roomId:\w+}`），每次匹配获得一个捕获组默认命名为 `\1`  ，在 `re.sub()` 的逻辑中从字符串的开头向后每找到一个匹配对象执行一次替换操作，即将第一次匹配到的字符串 `/{obsDesignId:3(?:F|f)\w{10}}` 替换为含有捕获组 `3(?:F|f)\w{10}` 的字符串，将第二次匹配到的字符串 `/{roomId:\w+}` 替换为含有捕获组 `\w+` 的字符串。

需要注意的是，在替换参数 `repl` 中我们要注意使用r取消字符串的转译功能。

如果 repl 是一个函数，那它会对每个非重复的 pattern 的情况调用。这个函数只能有一个 匹配对象 参数，并返回一个替换后的字符串。比如
```python
def dashrepl(matchobj):
    if matchobj.group(0) == '-': return ' '
    else: return '-'
l = re.sub('-{1,2}', dashrepl, 'pro----gram-files')
print(l)
```
output:
```text
pro--gram files
```

可选参数 count 是要替换的最大次数；count 必须是非负整数。如果省略这个参数或设为 0，所有的匹配都会被替换。 

空匹配仅在与前一个空匹配不相邻时才会被替换。在这个例子里`x*`匹配到的对象是零宽位置和字符 x。 
```python
pattern = re.compile(r'x*')
l = re.findall(pattern, 'abxd')
print(l)
l = re.sub('x*', '-', 'abxd')
print(l)
l = re.sub('x*', '-', '  abxd')
print(l)
```
output:
```text
['', '', 'x', '', '']
-a-b--d-
- - -a-b--d-
```
在字符串类型的 repl 参数里，如上所述的转义和向后引用中，`\g<name>` 会使用命名组合 name，（在 `(?P<name>…)` 语法中定义） `\g<number>` 会使用数字组；`\g<2>` 就是 `\2`，但它避免了二义性，如 `\g<2>0`。 `\20` 就会被解释为组20，而不是组2后面跟随一个字符 '0'。向后引用 `\g<0>` 把 pattern 作为一整个组进行引用。

#### `re.subn(pattern, repl, string, count=0, flags=0)`
行为与 `sub()` 相同，但是返回一个元组 (字符串, 替换次数)。
```python
pattern = re.compile(r'x*')
l = re.subn('x*', '-', 'abxd')
print(l)
l = re.subn('x*', '-', '  abxd')
print(l)
```
output:
```text
('-a-b--d-', 5)
('- - -a-b--d-', 7)
```

#### `re.escape(pattern)`
转义 pattern 中的特殊字符。如果你想对任意可能包含正则表达式元字符的文本字符串进行匹配，它就是有用的。只有在正则表达式中具有特殊含义的字符才会被转义,比如：
```python
print(re.escape('https://www.python.org'))
```
output:
```text
https://www\.python\.org
```

#### re.purge()
清除正则表达式的缓存。


## 正则对象

#### `Pattern.search(string[, pos[, endpos]]))`
扫描整个字符串找到匹配样式的第一个位置，并返回一个相应的匹配对象。如果没有匹配，就返回 `None` ； 注意这和找到一个零长度匹配是不同的。可选的第二个参数 `pos` 给出了字符串中开始搜索的位置索引；默认为 0，它不完全等价于字符串切片； `'^'` 样式字符匹配字符串真正的开头，和换行符后面的第一个字符，但不会匹配索引规定开始的位置。

可选参数 `endpos` 限定了字符串搜索的结束；它假定字符串长度到 endpos ， 所以只有从 pos 到 endpos - 1 的字符会被匹配。如果 endpos 小于 pos，就不会有匹配产生；另外，如果 rx 是一个编译后的正则对象， `rx.search(string, 0, 50)` 等价于 `rx.search(string[:50], 0)`。
```python
import re
source = '''aT cdhhuTTogTTTTooTgg
'''
pattern = re.compile(r'T')
position = pattern.search(source)
print(position)
pattern = re.compile(r'TT')
position = pattern.search(source)
print(position)
pattern = re.compile(r'TTT')
position = pattern.search(source)
print(position)
pattern = re.compile(r'A')
position = pattern.search(source)
print(position)
pattern = re.compile(r'$')
position = pattern.search(source)
print(position)
pattern = re.compile(r'a')
position = pattern.search(source)
print(position)
pattern = re.compile(r'a')
position = pattern.search(source, 1)
print(position)
```
output:
```text
# aT cdhhuTTogTTTTooTgg
# 01                   21             
<re.Match object; span=(1, 2), match='T'>       # 意味着从1位置开始到2位置结束（显然是包括1位置不包括2位置）
<re.Match object; span=(8, 10), match='TT'>
<re.Match object; span=(12, 15), match='TTT'>
None
<re.Match object; span=(21, 21), match=''>      # 匹配21位置开始到22位置结束，是一个零宽的位置匹配
<re.Match object; span=(0, 1), match='a'>
None
```
`Pattern.match(string[, pos[, endpos]])`
如果 string 开始的0或者多个字符匹配到了正则表达式样式，就返回一个相应的0匹配对象。如果没有匹配就返回 None ；注意它跟零长度匹配是不同的。`re.match()` 尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，就返回 none。我们可以注意到，匹配成功必须从字符串的最开始。便是 MULTILINE 多行模式， `re.match()` 也只匹配字符串的开始位置，而不匹配每行开始。
```python
source = '''aTT cdhhuTTogTTTTooTgg
'''
pattern = re.compile(r'TT')
position = pattern.match(source)
print(position)
pattern = re.compile(r'\b')
position = pattern.match(source)
print(position)
```
output:
```text
None
<re.Match object; span=(0, 0), match=''>
```
`Pattern.fullmatch(string[, pos[, endpos]])`
如果整个 string 匹配这个正则表达式，就返回一个相应的 匹配对象 。 否则就返回 None ； 注意跟零长度匹配是不同的。 可选参数 pos 和 endpos 与 `search()` 含义相同。

`Pattern.split(string, maxsplit=0)`
等价于 `split()` 函数，使用了编译后的样式。

`Pattern.findall(string[, pos[, endpos]])`
类似函数 `findall()` ， 使用了编译后样式，但也可以接收可选参数 pos 和 endpos ，限制搜索范围，就像 search()。

`Pattern.finditer(string[, pos[, endpos]])`
类似函数 `finditer()` ， 使用了编译后样式，但也可以接收可选参数 pos 和 endpos ，限制搜索范围，就像 search()。

`Pattern.sub(repl, string, count=0)`
等价于 `sub()` 函数，使用了编译后的样式。

`Pattern.subn(repl, string, count=0)`
等价于 `subn()` 函数，使用了编译后的样式。

`Pattern.flags`
正则匹配标记。这是可以传递给 `compile()` 的参数，任何 `(?…)` 内联标记，隐性标记比如 UNICODE 的结合。

`Pattern.groups`
捕获到的模式串中组的数量。

`Pattern.groupindex`
映射由 `(?P<id>)` 定义的命名符号组合和数字组合的字典。如果没有符号组，那字典就是空的。

`Pattern.pattern`
编译对象的原始样式字符串。

添加 copy.copy() 和 copy.deepcopy() 函数的支持。
```python
str = '123456'
pattern = re.compile('\d+')
str_1 = pattern.pattern
print(id(str), id(pattern), id(str_1))
```
output:
```text
1620709458224 1620709120080 1620709205936
```

## 匹配对象

匹配对象总是有一个布尔值 `True`。如果没有匹配的话 `match()` 和 `search()` 返回 None 所以你可以简单的用 `if` 语句来判断是否匹配。
```python
match = re.search(pattern, string)
if match:
    process(match)
```

匹配对象支持以下方法和属性：

#### `Match.expand(template)`
对 template 进行反斜杠转义替换并且返回，就像 `sub()` 方法中一样，只不过是从匹配中执行反向引用替换。数字引用`(\1`, `\2)`和命名组合`(\g<1>`, `\g<name>)` 替换为相应组合的内容。不匹配的组合替换为空字符串。
```python
m = re.match(r'(\d+)', '123\n*zbv*')
print(m.expand(r'是以数字开头的字符串，数字为：\1'))
```
output:
```text
是以数字开头的字符串，数字为：123
```

#### Match.group([group1, ...])
返回一个或者多个匹配的子组。如果只有一个参数，结果就是一个字符串，如果有多个参数，结果就是一个元组（每个参数对应一个项），如果没有参数，组1默认到0（整个匹配都被返回）。 如果一个组N 参数值为 0，相应的返回值就是整个匹配字符串；如果它是一个范围 [1..99]，结果就是相应的括号组字符串。如果一个组号是负数，或者大于样式中定义的组数，就引发一个 IndexError 异常。如果一个组包含是正则表达式的一部分并被匹配多次，就返回最后一个匹配。:
```python
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m.groups())
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.group('first_name'))
print(m.group('last_name'))
```
output:
```text
('Isaac', 'Newton')
Malcolm
Reynolds
```
如果一个组匹配成功多次，就只返回最后一个匹配
```python
m = re.match(r"(..)+", "a1b2c3")  # Matches 3 times
print(m.group(1))
```
output:
```text
c3
```
#### `Match.__getitem__(g)`
等价于 `m.group(g)`。这允许更方便的引用一个匹配。
```python
m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
print(m[1])
```
output:
```text
Isaac
```

#### `Match.groups(default=None)`
返回一个元组，包含所有匹配的子组，在样式中出现的从1到任意多的组合。 `default` 参数用于不参与匹配的情况，默认为 None。
```python
m = re.match(r"(\d+)\.(\d+)", "24.1632")
print(m.groups())
```
output:
```text
('24', '1632')
```

如果我们使小数点可选，那么不是所有的组都会参与到匹配当中。这些组合默认会返回一个 None ，除非指定了 default 参数。
```python
m = re.match(r"(\d+)\.?(\d+)?", "24")
print(m.groups())
print(m.groups('0'))
```
output:
```text
('24', None)
('24', '0')
```

#### `Match.groupdict(default=None)`
返回一个字典，包含了所有的命名子组。key就是组名。 default 参数用于不参与匹配的组合；默认为 None。
```python
m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())
```
output:
```text
{'first_name': 'Malcolm', 'last_name': 'Reynolds'}
```

#### `Match.start([group])   Match.end([group])`
返回 group 匹配到的字串的开始和结束标号。group 默认为0（意思是整个匹配的子串）。如果 group 存在，但未产生匹配，就返回 -1 。对于一个匹配对象 m， 和一个未参与匹配的组 g ，组 g (等价于 m.group(g))产生的匹配是
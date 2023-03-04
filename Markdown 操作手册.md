<!-- MarkdownTOC autoanchor="true" autolink="true" -->

- [Markdown操作手册 MacOS Sublime Text 4](#markdown%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8C-macos-sublime-text-4)
	- [插件安装](#%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85)
		- [Markdown Editing](#markdown-editing)
		- [MarkdownPreview](#markdownpreview)
			- [将.md 文件用浏览器预览](#%E5%B0%86md-%E6%96%87%E4%BB%B6%E7%94%A8%E6%B5%8F%E8%A7%88%E5%99%A8%E9%A2%84%E8%A7%88)
			- [用快捷键打开预览](#%E7%94%A8%E5%BF%AB%E6%8D%B7%E9%94%AE%E6%89%93%E5%BC%80%E9%A2%84%E8%A7%88)
	- [标题](#%E6%A0%87%E9%A2%98)
		- [三级标题](#%E4%B8%89%E7%BA%A7%E6%A0%87%E9%A2%98)
	- [段落](#%E6%AE%B5%E8%90%BD)
	- [换行](#%E6%8D%A2%E8%A1%8C)
	- [强调](#%E5%BC%BA%E8%B0%83)
		- [粗体](#%E7%B2%97%E4%BD%93)
		- [斜体](#%E6%96%9C%E4%BD%93)
		- [粗体和斜体混用](#%E7%B2%97%E4%BD%93%E5%92%8C%E6%96%9C%E4%BD%93%E6%B7%B7%E7%94%A8)
	- [引用](#%E5%BC%95%E7%94%A8)
		- [多个段落的引用](#%E5%A4%9A%E4%B8%AA%E6%AE%B5%E8%90%BD%E7%9A%84%E5%BC%95%E7%94%A8)
		- [嵌套引用](#%E5%B5%8C%E5%A5%97%E5%BC%95%E7%94%A8)
		- [带有其它元素的块引用](#%E5%B8%A6%E6%9C%89%E5%85%B6%E5%AE%83%E5%85%83%E7%B4%A0%E7%9A%84%E5%9D%97%E5%BC%95%E7%94%A8)
	- [列表](#%E5%88%97%E8%A1%A8)
		- [有序列表](#%E6%9C%89%E5%BA%8F%E5%88%97%E8%A1%A8)
		- [无序列表](#%E6%97%A0%E5%BA%8F%E5%88%97%E8%A1%A8)
		- [在列表中嵌套其他元素](#%E5%9C%A8%E5%88%97%E8%A1%A8%E4%B8%AD%E5%B5%8C%E5%A5%97%E5%85%B6%E4%BB%96%E5%85%83%E7%B4%A0)
			- [段落](#%E6%AE%B5%E8%90%BD-1)
			- [引用块](#%E5%BC%95%E7%94%A8%E5%9D%97)
			- [代码块](#%E4%BB%A3%E7%A0%81%E5%9D%97)
			- [图片](#%E5%9B%BE%E7%89%87)
			- [列表](#%E5%88%97%E8%A1%A8-1)
	- [代码](#%E4%BB%A3%E7%A0%81)
		- [转义反引号](#%E8%BD%AC%E4%B9%89%E5%8F%8D%E5%BC%95%E5%8F%B7)
		- [代码块](#%E4%BB%A3%E7%A0%81%E5%9D%97-1)
		- [围栏代码块](#%E5%9B%B4%E6%A0%8F%E4%BB%A3%E7%A0%81%E5%9D%97)
	- [分割线](#%E5%88%86%E5%89%B2%E7%BA%BF)
	- [链接](#%E9%93%BE%E6%8E%A5)
		- [网址和Email地址](#%E7%BD%91%E5%9D%80%E5%92%8Cemail%E5%9C%B0%E5%9D%80)
		- [带格式化的链接](#%E5%B8%A6%E6%A0%BC%E5%BC%8F%E5%8C%96%E7%9A%84%E9%93%BE%E6%8E%A5)
		- [引用类型的链接](#%E5%BC%95%E7%94%A8%E7%B1%BB%E5%9E%8B%E7%9A%84%E9%93%BE%E6%8E%A5)
			- [链接的第一部分形式](#%E9%93%BE%E6%8E%A5%E7%9A%84%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%E5%BD%A2%E5%BC%8F)
			- [链接的第二部分形式](#%E9%93%BE%E6%8E%A5%E7%9A%84%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%E5%BD%A2%E5%BC%8F)
		- [Macdown编辑Markdown文件的内部跳转](#macdown%E7%BC%96%E8%BE%91markdown%E6%96%87%E4%BB%B6%E7%9A%84%E5%86%85%E9%83%A8%E8%B7%B3%E8%BD%AC)
	- [图片](#%E5%9B%BE%E7%89%87-1)
		- [链接图片](#%E9%93%BE%E6%8E%A5%E5%9B%BE%E7%89%87)
	- [转义字符](#%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6)
		- [可作转义字符](#%E5%8F%AF%E4%BD%9C%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6)
		- [特殊字符自动转义](#%E7%89%B9%E6%AE%8A%E5%AD%97%E7%AC%A6%E8%87%AA%E5%8A%A8%E8%BD%AC%E4%B9%89)
	- [内嵌 HTML 标签](#%E5%86%85%E5%B5%8C-html-%E6%A0%87%E7%AD%BE)
		- [行级內联标签](#%E8%A1%8C%E7%BA%A7%E5%85%A7%E8%81%94%E6%A0%87%E7%AD%BE)
		- [区块标签](#%E5%8C%BA%E5%9D%97%E6%A0%87%E7%AD%BE)
		- [HTML 用法最佳实践](#html-%E7%94%A8%E6%B3%95%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5)
	- [表格](#%E8%A1%A8%E6%A0%BC)
		- [对齐](#%E5%AF%B9%E9%BD%90)
		- [格式化表格中的文字](#%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%A1%A8%E6%A0%BC%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97)
		- [在表中转义管道字符](#%E5%9C%A8%E8%A1%A8%E4%B8%AD%E8%BD%AC%E4%B9%89%E7%AE%A1%E9%81%93%E5%AD%97%E7%AC%A6)
	- [围栏代码块](#%E5%9B%B4%E6%A0%8F%E4%BB%A3%E7%A0%81%E5%9D%97-1)
		- [语法高亮](#%E8%AF%AD%E6%B3%95%E9%AB%98%E4%BA%AE)
	- [脚注](#%E8%84%9A%E6%B3%A8)
	- [创建定义](#%E5%88%9B%E5%BB%BA%E5%AE%9A%E4%B9%89)
	- [删除线](#%E5%88%A0%E9%99%A4%E7%BA%BF)
	- [任务列表](#%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8)
	- [目录](#%E7%9B%AE%E5%BD%95)

<!-- /MarkdownTOC -->

<a id="markdown%E6%93%8D%E4%BD%9C%E6%89%8B%E5%86%8C-macos-sublime-text-4"></a>
# Markdown操作手册 MacOS Sublime Text 4


<a id="%E6%8F%92%E4%BB%B6%E5%AE%89%E8%A3%85"></a>
## 插件安装

Sublime Text 有官方的插件网站[Package Control](https://packagecontrol.io/)可以查看各种类型的插件，我们在这里介绍几种编辑 Markdown 文件常用的插件。

<a id="markdown-editing"></a>
### Markdown Editing

Markdown Editing是 Markdown 写作者必备的插件，只针对 md\mdown\mmd\txt 格式文件才启用。可以高亮显示语法、自动匹配星号（`*`）下划线（`
_`）及反引号（`` ` ``）。详细信息及快捷键用法可以查询[MarkdownEditing](https://sublimetext-markdown.github.io/MarkdownEditing/usage/)。

| 快捷键     | 功能 |
|:---:|---|
|⌘ + ⌥ + V	 |创建或粘贴剪贴板的内容作为选定文本的内联链接|
|⌘ + ⌥ + R	 |创建或粘贴剪贴板的内容作为参考链接|
|⌘ + ⇧ + K	 |在选定文本上创建或粘贴剪贴板的内容作为内嵌图像|
|⌥ + ⇧ + 6	 |插入脚注|
|F12	|跳转到参考/脚注定义|
|Shift+F12	|从定义跳转到引用。|
|⌘ + ⌥ + R | 搜索并跳转到标题|

<a id="markdownpreview"></a>
### MarkdownPreview

<a id="%E5%B0%86md-%E6%96%87%E4%BB%B6%E7%94%A8%E6%B5%8F%E8%A7%88%E5%99%A8%E9%A2%84%E8%A7%88"></a>
#### 将.md 文件用浏览器预览

MarkdownPreview 通过将 .md 文件导出为 html 代码在浏览器中预览 Markdown 文件。

1. 组合键 Command + Shift + P 调出命令面板
2. 输入mdp找到并选中 Markdown Preview： Preview in Browser
3. 出现两个选项：github 和 markdown。任选其一即可，github 是利用 GitHub 的在线 API 来解析 .md 文件，支持在线资源的预览；markdown 就是传统的本地打开，不支持在线资源的预览。
4. 默认浏览器中显示预览结果

<a id="%E7%94%A8%E5%BF%AB%E6%8D%B7%E9%94%AE%E6%89%93%E5%BC%80%E9%A2%84%E8%A7%88"></a>
#### 用快捷键打开预览

Sublime Text 支持自定义快捷键，Markdown Preview 默认没有快捷键，我们可以自己为 Markdown Preview： Preview in Browser 设置快捷键。方法是在 Preferences --> Key Bindings 打开的文件的右侧栏的中括号中添加一行代码如下：

	{ "keys": ["option+m"], "command": "markdown_preview", "args": {"target": "browser", "parser":"markdown"}  }

`"option+m"`可设置为自己喜欢的按键。`"parser": "markdown"`也可设置为`"parser":"github"`，改为使用 Github 在线 API 解析 Markdown。

<a id="%E6%A0%87%E9%A2%98"></a>
## 标题
要创建标题，请在单词或短语前面添加井号 (#) 。# 的数量代表了标题的级别。

	### 三级标题

<a id="%E4%B8%89%E7%BA%A7%E6%A0%87%E9%A2%98"></a>
### 三级标题

<a id="%E6%AE%B5%E8%90%BD"></a>
## 段落
要创建段落，请使用空白行将一行或多行文本进行分隔。

新的一段

<a id="%E6%8D%A2%E8%A1%8C"></a>
## 换行

第一行后接上两个空格键然后回车可以换到新的一行。  
新的一行

新的一段。

<a id="%E5%BC%BA%E8%B0%83"></a>
## 强调

<a id="%E7%B2%97%E4%BD%93"></a>
### 粗体

要加粗文本，请在单词或短语的前后各添加两个星号或下划线。如需加粗一个单词或短语的中间部分用以表示强调的话，请在要加粗部分的两侧各添加两个星号。

I just love **bold text**.  
I just love __bold text__.	
Love**is**bold

Markdown 应用程序在如何处理单词或短语中间的下划线上并不一致。为兼容考虑，在单词或短语中间部分加粗的话，请使用星号。

<a id="%E6%96%9C%E4%BD%93"></a>
### 斜体

要用斜体显示文本，请在单词或短语前后添加一个星号或下划线。要斜体突出单词的中间部分，请在字母前后各添加一个星号，中间不要带空格。

Italicized text is the *cat's meow*.  
Italicized text is the _cat's meow_.  
A*cat*meow

<a id="%E7%B2%97%E4%BD%93%E5%92%8C%E6%96%9C%E4%BD%93%E6%B7%B7%E7%94%A8"></a>
### 粗体和斜体混用

要同时用粗体和斜体突出显示文本，请在单词或短语的前后各添加三个星号或下划线。要加粗并用斜体显示单词或短语的中间部分，请在要突出显示的部分前后各添加三个星号，中间不要带空格。

***I love China***.  
___I love China___.  
I love C***hin***a.  
This text is ___really important___.  
This text is __*really important*__.  
This text is **_really important_**.  
This is really***very***important text.  

Markdown 应用程序在处理单词或短语中间添加的下划线上并不一致。为了实现兼容性，请使用星号将单词或短语的中间部分加粗并以斜体显示，以示重要。

<a id="%E5%BC%95%E7%94%A8"></a>
## 引用

要创建块引用，请在段落前添加一个 `>` 符号。

	>这是一段引用

渲染效果如下
>这是一段引用

<a id="%E5%A4%9A%E4%B8%AA%E6%AE%B5%E8%90%BD%E7%9A%84%E5%BC%95%E7%94%A8"></a>
### 多个段落的引用

块引用可以包含多个段落。为段落之间的空白行添加一个 `>` 符号。
	
	>第一段引用
	>
	>第二段引用

渲染结果如下

>第一段引用
>
>第二段引用

<a id="%E5%B5%8C%E5%A5%97%E5%BC%95%E7%94%A8"></a>
### 嵌套引用

块引用可以嵌套。在要嵌套的段落前添加一个 >> 符号。
	
	> 第一层引用
	>
	>>第二层引用

渲染结果如下

>第一层引用
>
>>第二层引用

<a id="%E5%B8%A6%E6%9C%89%E5%85%B6%E5%AE%83%E5%85%83%E7%B4%A0%E7%9A%84%E5%9D%97%E5%BC%95%E7%94%A8"></a>
### 带有其它元素的块引用

块引用可以包含其他 Markdown 格式的元素。并非所有元素都可以使用，你需要进行实验以查看哪些元素有效。

	> #### The quarterly results look great!
	>
	> - Revenue was off the chart.
	> - Profits were higher than ever.
	>
	>  *Everything* is going according to **plan**.

渲染结果如下

> #### 三级标题
>
> - 强调段落1
> - 强调段落2
>
>  *Everything* is going according to **plan**.

<a id="%E5%88%97%E8%A1%A8"></a>
## 列表

可以将多个条目组织成有序或无序列表。

<a id="%E6%9C%89%E5%BA%8F%E5%88%97%E8%A1%A8"></a>
### 有序列表

要创建有序列表，请在每个列表项前添加数字并紧跟一个英文句点。数字不必按数学顺序排列，但是列表应当以数字 1 起始。

	1. First item
	2. Second item
	3. Third item
	4. Fourth item

渲染结果如下

1. First item
2. Second item
3. Third item
4. Fourth item

```
1. First item
1. Second item
1. Third item
1. Fourth item
```
渲染结果如下

1. First item
1. Second item
1. Third item
1. Fourth item

```
1. First item
8. Second item
3. Third item
5. Fourth item
```

渲染结果如下

1. First item
8. Second item
3. Third item
5. Fourth item

```
1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item
```

渲染结果如下

1. First item
2. Second item
3. Third item
    1. Indented item
    2. Indented item
4. Fourth item



<a id="%E6%97%A0%E5%BA%8F%E5%88%97%E8%A1%A8"></a>
### 无序列表

要创建无序列表，请在每个列表项前面添加破折号 (`-`)、星号 (`*`) 或加号 (`+`) 。缩进一个或多个列表项可创建嵌套列表。

```
- First item
- Second item
- Third item
- Fourth item
```
渲染结果如下

- First item
- Second item
- Third item
- Fourth item

```
- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item
```
渲染结果如下

- First item
- Second item
- Third item
    - Indented item
    - Indented item
- Fourth item

<a id="%E5%9C%A8%E5%88%97%E8%A1%A8%E4%B8%AD%E5%B5%8C%E5%A5%97%E5%85%B6%E4%BB%96%E5%85%83%E7%B4%A0"></a>
### 在列表中嵌套其他元素

要在保留列表连续性的同时在列表中添加另一种元素，请将该元素缩进四个空格或一个制表符，如下例所示：


<a id="%E6%AE%B5%E8%90%BD-1"></a>
#### 段落
```
*   This is the first list item.
*   Here's the second list item.

    I need to add another paragraph below the second list item.

*   And here's the third list item.
```
渲染效果如下

- This is the first list item.
- Here's the second list item.

    I need to add another paragraph below the second list item.

- And here's the third list item.

<a id="%E5%BC%95%E7%94%A8%E5%9D%97"></a>
#### 引用块
```
*   This is the first list item.
*   Here's the second list item.

    > A blockquote would look great below the second list item.

*   And here's the third list item.
```

渲染效果如下

*   This is the first list item.
*   Here's the second list item.

    > A blockquote would look great below the second list item.

*   And here's the third list item.

<a id="%E4%BB%A3%E7%A0%81%E5%9D%97"></a>
#### 代码块

```
1.  Open the file.
2.  Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3.  Update the title to match the name of your website.
```

渲染效果如下

1.  Open the file.
2.  Find the following code block on line 21:

        <html>
          <head>
            <title>Test</title>
          </head>

3.  Update the title to match the name of your website.
渲染效果如下：

如果希望在列表后使用代码块，您将在代码块之前和之后的行上使用三个反引号或三个波浪号。

1. 列表1
2. 列表2
3. 列表3


		无法获得独立的新代码块。

代码如下

	1. 列表1
	2. 列表2
	3. 列表3
	
	```
	可以获得独立的新代码块
	可以获得独立的新代码块
	```

渲染结果如下

1. 列表1
2. 列表2
3. 列表3

```
可以获得代码块
可以获得代码块
```

<a id="%E5%9B%BE%E7%89%87"></a>
#### 图片

	1. 插入图片
	
		![Tux, the Linux mascot](/assets/images/tux.png)
	
	2. 插入图片成功


​	
1. 插入图片

	![Tux, the Linux mascot](/assets/images/tux.png)
	
2. 插入图片成功

<a id="%E5%88%97%E8%A1%A8-1"></a>
#### 列表
可以在有序列表中插入无序列表，反之也可以。

	1. 这是一个有序列表
	2. 项目2
	3. 项目3
		- 这是一个无序列表
		- 项目2
	4. 项目4

渲染结果如下

1. 这是一个有序列表
2. 项目2
3. 项目3
	- 这是一个无序列表
	- 项目2
4. 项目4

```
- 这是一个无序列表
- 项目2
- 项目3
	1. 这是一个有序列表
	2. 项目2
- 项目4
```
渲染结果如下

- 这是一个无序列表
- 项目2
- 项目3
	1. 这是一个有序列表
	2. 项目2
- 项目4

<a id="%E4%BB%A3%E7%A0%81"></a>
## 代码

要将单词或短语表示为代码，请将其包裹在反引号中。

	这是一段`代码`。

这是一段`代码`。

<a id="%E8%BD%AC%E4%B9%89%E5%8F%8D%E5%BC%95%E5%8F%B7"></a>
### 转义反引号
如果你要表示为代码的单词或短语中包含一个或多个反引号，则可以通过将单词或短语包裹在双反引号中。注意不要出现三个反引号连用的情况。

	``在代码中使用`反引号```	

``在代码中使用`反引号`.``	

<a id="%E4%BB%A3%E7%A0%81%E5%9D%97-1"></a>
### 代码块
要创建代码块，请将代码块的每一行缩进至少四个空格或一个制表符。

```	
	<html>
		<head>
		</head>
	</html>
```
渲染结果如下

	<html>
		<head>
		</head>
	</html>

<a id="%E5%9B%B4%E6%A0%8F%E4%BB%A3%E7%A0%81%E5%9D%97"></a>
### 围栏代码块
Markdown基本语法允许您通过将行缩进四个空格或一个制表符来创建代码块。如果发现不方便，请尝试使用受保护的代码块。根据Markdown处理器或编辑器的不同，您将在代码块之前和之后的行上使用三个反引号或三个波浪号。参考 [围栏代码块](#weilandaimakuai)

<a id="%E5%88%86%E5%89%B2%E7%BA%BF"></a>
## 分割线

要创建分隔线，请在单独一行上使用三个或多个星号 (`***`)、破折号 (`---`) 或下划线 (`___`) ，并且不能包含其他内容。

```

***

---

___

```

渲染结果如下

***

---

___

为了兼容性，请在分隔线的前后均添加空白行。

<a id="%E9%93%BE%E6%8E%A5"></a>
## 链接

<span id="label"></span>

链接文本放在中括号内，链接地址放在后面的括号中，链接title可选。链接title是当鼠标悬停在链接上时会出现的文字，这个title是可选的，它放在圆括号中链接地址后面，跟链接地址之间以空格分隔。

超链接Markdown语法代码：[超链接显示名](超链接地址 "超链接title")

	这是一个链接 [Markdown语法](https://markdown.com.cn)。

渲染效果如下

这是一个链接 [Markdown语法](https://markdown.com.cn)。

	这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。

渲染效果如下
	
这是一个链接 [Markdown语法](https://markdown.com.cn "最好的markdown教程")。

<a id="%E7%BD%91%E5%9D%80%E5%92%8Cemail%E5%9C%B0%E5%9D%80"></a>
### 网址和Email地址
使用尖括号可以很方便地把URL或者email地址变成可点击的链接。

	<https://markdown.com.cn>
	<fake@example.com>

渲染效果如下

<https://markdown.com.cn>  
<fake@example.com>

<a id="%E5%B8%A6%E6%A0%BC%E5%BC%8F%E5%8C%96%E7%9A%84%E9%93%BE%E6%8E%A5"></a>
### 带格式化的链接

强调链接, 在链接语法前后增加星号。 要将链接表示为代码，请在方括号中添加反引号。

	I love supporting the **[EFF](https://eff.org)**.
	This is the *[Markdown Guide](https://www.markdownguide.org)*.
	See the section on [`code`](#code).	

渲染效果如下

I love supporting the **[EFF](https://eff.org)**.  
This is the *[Markdown Guide](https://www.markdownguide.org)*.  
See the section on [`code`](https://www.markdownguide.org).

<a id="%E5%BC%95%E7%94%A8%E7%B1%BB%E5%9E%8B%E7%9A%84%E9%93%BE%E6%8E%A5"></a>
### 引用类型的链接

引用样式链接是一种特殊的链接，它使URL在Markdown中更易于显示和阅读。参考样式链接分为两部分：与文本保持内联的部分以及存储在文件中其他位置的部分，以使文本易于阅读。

<a id="%E9%93%BE%E6%8E%A5%E7%9A%84%E7%AC%AC%E4%B8%80%E9%83%A8%E5%88%86%E5%BD%A2%E5%BC%8F"></a>
#### 链接的第一部分形式

引用类型的链接的第一部分使用两组括号进行格式设置。第一组方括号包围应显示为链接的文本。第二组括号显示了一个标签，该标签用于指向您存储在文档其他位置的链接。

尽管不是必需的，可以在第一组和第二组括号之间包含一个空格。第二组括号中的标签不区分大小写，可以包含字母，数字，空格或标点符号。

[hobbit] [0]

<a id="%E9%93%BE%E6%8E%A5%E7%9A%84%E7%AC%AC%E4%BA%8C%E9%83%A8%E5%88%86%E5%BD%A2%E5%BC%8F"></a>
#### 链接的第二部分形式

引用类型链接的第二部分使用以下属性设置格式：

1. 放在括号中的标签，其后紧跟一个冒号和至少一个空格（例如`[label]:`）。
2. 链接的URL，可以选择将其括在尖括号中。
3. 链接的可选标题，可以将其括在双引号，单引号或括号中。

- [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle
- [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle "Hobbit lifestyles"
- [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle 'Hobbit lifestyles'
- [1]: https://en.wikipedia.org/wiki/Hobbit#Lifestyle (Hobbit lifestyles)
- [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> "Hobbit lifestyles"
- [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> 'Hobbit lifestyles'
- [1]: <https://en.wikipedia.org/wiki/Hobbit#Lifestyle> (Hobbit lifestyles)

[0]: <https://en.wikipedia.org/wiki/Hobbit> "hobbit - Wikipedia"

可以将链接的第二部分放在Markdown文档中的任何位置。有些人将它们放在出现的段落之后，有些人则将它们放在文档的末尾（例如尾注或脚注）。

不同的 Markdown 应用程序处理URL中间的空格方式不一样。为了兼容性，请尽量使用%20代替空格。

	[link](https://www.example.com/my%20great%20page)
	[link](https://www.example.com/my great page)

<a id="macdown%E7%BC%96%E8%BE%91markdown%E6%96%87%E4%BB%B6%E7%9A%84%E5%86%85%E9%83%A8%E8%B7%B3%E8%BD%AC"></a>
### Macdown编辑Markdown文件的内部跳转

在需要跳转的部分使用`[代替文本](#标签)`，在跳转至的位置写入代码`<span id="标签"></span>`

[这是一个需要跳转的位置，跳转至链接部分的开头](#label)
	
<a id="%E5%9B%BE%E7%89%87-1"></a>
## 图片
要添加图像，请使用感叹号 (`!`), 然后在方括号增加替代文本，图片链接放在圆括号里，括号里的链接后可以增加一个可选的图片标题文本。

插入图片Markdown语法代码：`![图片alt](图片链接 "图片title")`

	![这是图片](/assets/img/philly-magic-garden.jpg "Magic Gardens")

渲染效果如下

![这是图片](/assets/img/philly-magic-garden.jpg "Magic Gardens")

<a id="%E9%93%BE%E6%8E%A5%E5%9B%BE%E7%89%87"></a>
### 链接图片

给图片增加链接，请将图像的Markdown 括在方括号中，然后将链接添加在圆括号中。

	[![沙漠中的岩石图片](/assets/img/shiprock.jpg "Shiprock")](https://markdown.com.cn)

渲染效果如下

[![沙漠中的岩石图片](/assets/img/shiprock.jpg "Shiprock")](https://markdown.com.cn)

<a id="%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6"></a>
## 转义字符

要显示原本用于格式化 Markdown 文档的字符，请在字符前面添加反斜杠字符 \ 。

	\* Without the backslash, this would be a bullet in an unordered list.

渲染效果如下
	
\* Without the backslash, this would be a bullet in an unordered list.

<a id="%E5%8F%AF%E4%BD%9C%E8%BD%AC%E4%B9%89%E5%AD%97%E7%AC%A6"></a>
### 可作转义字符

|Character | Name | 
| :-------:  | -----|
| \ | backslash |
| `	| backtick (see also escaping backticks in code) |
| *	| asterisk|
| _	| underscore|
| { }	| curly braces|
| [ ]	| brackets|
| ( )	| parentheses|
| #	| pound sign|
| +	| plus sign|
| -	| minus sign (hyphen)|
| .	| dot|
| !	| exclamation mark|
| \|	| pipe (see also escaping pipe in tables)|

<a id="%E7%89%B9%E6%AE%8A%E5%AD%97%E7%AC%A6%E8%87%AA%E5%8A%A8%E8%BD%AC%E4%B9%89"></a>
### 特殊字符自动转义

在 HTML 文件中，有两个字符需要特殊处理： `<` 和 `&` 。 `<` 符号用于起始标签，`&` 符号则用于标记 HTML 实体，如果你只是想要使用这些符号，你必须要使用实体的形式，像是 `&lt;` 和 `&amp;`。

`&` 符号其实很容易让写作网页文件的人感到困扰，如果你要打「AT&T」 ，你必须要写成`「AT&amp;T」` ，还得转换网址内的 `&` 符号，如果你要链接到：

	http://images.google.com/images?num=30&q=larry+bird

你必须要把网址转成：

	http://images.google.com/images?num=30&amp;q=larry+bird

才能放到链接标签的 `href` 属性里。不用说也知道这很容易忘记，这也可能是 HTML 标准检查所检查到的错误中，数量最多的。

Markdown 允许你直接使用这些符号，它帮你自动转义字符。如果你使用 `&` 符号的作为 HTML 实体的一部分，那么它不会被转换，而在其它情况下，它则会被转换成 `&amp;`。所以你如果要在文件中插入一个著作权的符号，你可以这样写：`&copy;`，Markdown 将不会对这段文字做修改，但是如果你这样写：`AT&T`，Markdown 就会将它转为：`AT&amp;T`。

类似的状况也会发生在 `<` 符号上，因为 Markdown 支持 行内 HTML ，如果你使用` <` 符号作为 HTML 标签的分隔符，那 Markdown 也不会对它做任何转换，但是如果你是写：`4 < 5`，Markdown 将会把它转换为：`4 &lt; 5`。

需要特别注意的是，在 Markdown 的块级元素和内联元素中， `<` 和 `&` 两个符号都会被自动转换成 HTML 实体，这项特性让你可以很容易地用 Markdown 写 HTML。（在 HTML 语法中，你要手动把所有的 `<` 和 `&` 都转换为 HTML 实体。）

<a id="%E5%86%85%E5%B5%8C-html-%E6%A0%87%E7%AD%BE"></a>
## 内嵌 HTML 标签
对于 Markdown 涵盖范围之外的标签，都可以直接在文件里面用 HTML 本身。如需使用 HTML，不需要额外标注这是 HTML 或是 Markdown，只需 HTML 标签添加到 Markdown 文本中即可。

<a id="%E8%A1%8C%E7%BA%A7%E5%85%A7%E8%81%94%E6%A0%87%E7%AD%BE"></a>
### 行级內联标签

HTML 的行级內联标签如 `<span>`、`<cite>`、`<del>` 不受限制，可以在 Markdown 的段落、列表或是标题里任意使用。依照个人习惯，甚至可以不用 Markdown 格式，而采用 HTML 标签来格式化。例如：如果比较喜欢 HTML 的 `<a>` 或 `<img>` 标签，可以直接使用这些标签，而不用 Markdown 提供的链接或是图片语法。当你需要更改元素的属性时（例如为文本指定颜色或更改图像的宽度），使用 HTML 标签更方便些。

HTML 行级內联标签和区块标签不同，在內联标签的范围内， Markdown 的语法是可以解析

	This **word** is bold. This <em>word</em> is italic.

渲染效果如下:

This **word** is bold. This <em>word</em> is italic.

<a id="%E5%8C%BA%E5%9D%97%E6%A0%87%E7%AD%BE"></a>
### 区块标签

区块元素如 `<div>`、`<table>`、`<pre>`、`<p>` 等标签，必须在前后加上空行，以便于内容区分。而且这些元素的开始与结尾标签，不可以用 tab 或是空白来缩进。Markdown 会自动识别这区块元素，避免在区块标签前后加上没有必要的 `<p>` 标签。

	This is a regular paragraph.
	
	<table>
		<tr>
			<td>Foo</td>
		</tr>
	</table>
	
	This is another regular paragraph.



This is a regular paragraph.

<table>
	<tr>
		<td>Foo</td>
	</tr>
</table>

This is another regular paragraph.

请注意，Markdown 语法在 HTML 区块标签中将不会被进行处理。例如，你无法在 HTML 区块内使用 Markdown 形式的`*强调*`。

<a id="html-%E7%94%A8%E6%B3%95%E6%9C%80%E4%BD%B3%E5%AE%9E%E8%B7%B5"></a>
### HTML 用法最佳实践
出于安全原因，并非所有 Markdown 应用程序都支持在 Markdown 文档中添加 HTML。如有疑问，请查看相应 Markdown 应用程序的手册。某些应用程序只支持 HTML 标签的子集。

对于 HTML 的块级元素 `<div>`、`<table>`、`<pre>` 和 `<p>`，请在其前后使用空行（blank lines）与其它内容进行分隔。尽量不要使用制表符（tabs）或空格（spaces）对 HTML 标签做缩进，否则将影响格式。

在 HTML 块级标签内不能使用 Markdown 语法。例如 `<p>italic and **bold**</p>` 将不起作用。

<a id="%E8%A1%A8%E6%A0%BC"></a>
## 表格

要添加表，请使用三个或多个连字符（---）创建每列的标题，并使用管道（|）分隔每列。您可以选择在表的任一端添加管道。


	| Syntax      | Description |
	| ----------- | ----------- |
	| Header      | Title       |
	| Paragraph   | Text        |

呈现的输出如下所示：

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

单元格宽度可以变化，如下所示。呈现的输出将看起来相同。

	| Syntax      | Description |
	| --- | ---- |
	| Header      | Title       |
	| Paragraph   | Text        |	


呈现的输出如下所示：

| Syntax      | Description |
| --- | --- |
| Header      | Title       |
| Paragraph   | Text        |

**Tip**: 使用连字符和管道创建表可能很麻烦。为了加快该过程，请尝试使用[Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables)。使用图形界面构建表，然后将生成的Markdown格式的文本复制到文件中。

<a id="%E5%AF%B9%E9%BD%90"></a>
### 对齐

您可以通过在标题行中的连字符的左侧，右侧或两侧添加冒号（`:`），将列中的文本对齐到左侧，右侧或中心。

```
| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And       |
```

呈现的输出如下所示：

| Syntax      | Description | Test Text     |
| :---        |    :----:   |          ---: |
| Header      | Title       | Here's this   |
| Paragraph   | Text        | And       |

<a id="%E6%A0%BC%E5%BC%8F%E5%8C%96%E8%A1%A8%E6%A0%BC%E4%B8%AD%E7%9A%84%E6%96%87%E5%AD%97"></a>
### 格式化表格中的文字

您可以在表格中设置文本格式。例如，您可以添加链接，代码（仅反引号（`` ` ``）中的单词或短语，而不是代码块）和强调。
您不能添加标题，块引用，列表，水平规则，图像或HTML标签。

<a id="%E5%9C%A8%E8%A1%A8%E4%B8%AD%E8%BD%AC%E4%B9%89%E7%AE%A1%E9%81%93%E5%AD%97%E7%AC%A6"></a>
### 在表中转义管道字符

您可以使用表格的HTML字符代码（`&#124;`）在表中显示竖线（`|`）字符。

<a id="%E5%9B%B4%E6%A0%8F%E4%BB%A3%E7%A0%81%E5%9D%97-1"></a>
## 围栏代码块

<span id="weilandaimakuai"></span>

Markdown基本语法允许您通过将行缩进四个空格或一个制表符来创建代码块。如果发现不方便，请尝试使用受保护的代码块。根据Markdown处理器或编辑器的不同，您将在代码块之前和之后的行上使用三个反引号或三个波浪号。


	```
	这是一个代码块
	```

呈现的输出如下所示：

```
这是一个代码块
```

<a id="%E8%AF%AD%E6%B3%95%E9%AB%98%E4%BA%AE"></a>
### 语法高亮

许多Markdown处理器都支持受围栏代码块的语法突出显示。使用此功能，您可以为编写代码的任何语言添加颜色突出显示。要添加语法突出显示，请在受防护的代码块之前的反引号旁边指定一种语言。

	```json
	{
		"firstName": "John",
		"lastName": "Smith",
		"age": 25
	}
	```

呈现的输出如下所示：

```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

<a id="%E8%84%9A%E6%B3%A8"></a>
## 脚注

Here's a simple footnote,[^1] and here's a longer one.[^bignote].这是第三条脚注。[^3]

脚注使您可以添加注释和参考，而不会使文档正文混乱。当您创建脚注时，带有脚注的上标数字会出现在您添加脚注参考的位置。读者可以单击链接以跳至页面底部的脚注内容。

要创建脚注参考，请在方括号（`[^1]`）内添加插入符号和标识符。标识符可以是数字或单词，但不能包含空格或制表符。标识符仅将脚注参考与脚注本身相关联，在输出中脚注按顺序编号。

在括号内使用另一个插入符号和数字添加脚注，并用冒号和文本（`[^1]: My footnote.`）。您不必在文档末尾添加脚注。您可以将它们放在除列表，块引号和表之类的其他元素之外的任何位置。



	Here's a simple footnote,[^1] and here's a longer one.[^bignote]
	
	[^1]: This is the first footnote.
	
	[^bignote]: Here's one with multiple paragraphs and code.
	
		Indent paragraphs to include them in the footnote.
	
		`{ my code }`
	
		Add as many paragraphs as you like.
		
	[^3]: 这是第三条脚注


[^1]: This is the first footnote.

[^bignote]: Here's one with multiple paragraphs and code.

    Indent paragraphs to include them in the footnote.
    
    `{ my code }`
    
    Add as many paragraphs as you like.

[^3]: 这是第三条脚注

<a id="%E5%88%9B%E5%BB%BA%E5%AE%9A%E4%B9%89"></a>
## 创建定义

一些Markdown处理器允许您创建术语及其对应定义的定义列表。要创建定义列表，请在第一行上键入术语。在下一行，键入一个冒号，后跟一个空格和定义。

First Term
: This is the definition of the first term.

Second Term
: This is one definition of the second term.
: This is another definition of the second term.


<a id="%E5%88%A0%E9%99%A4%E7%BA%BF"></a>
## 删除线

您可以通过在单词中心放置一条水平线来删除单词。结果看起来像这样。此功能使您可以指示某些单词是一个错误，要从文档中删除。若要删除单词，请在单词前后使用两个波浪号`~~`。

	~~世界是平坦的。~~ 我们现在知道世界是圆的

~~世界是平坦的。~~ 我们现在知道世界是圆的

<a id="%E4%BB%BB%E5%8A%A1%E5%88%97%E8%A1%A8"></a>
## 任务列表

任务列表使您可以创建带有复选框的项目列表。在支持任务列表的Markdown应用程序中，复选框将显示在内容旁边。要创建任务列表，请在任务列表项之前添加破折号`-`和方括号`[ ]`，并在`[ ]`前面加上空格。要选择一个复选框，请在方括号`[x]`之间添加 x 。


	- [x] Write the press release
	+ [ ] Update the website
	+ [ ] Contact the media

呈现的输出如下所示

- [x] Write the press release
- [ ] Update the website
- [ ] Contact the media

<a id="%E7%9B%AE%E5%BD%95"></a>
## 目录

使用 MarkdownTOC 插件自动生成目录树。安装插件后按照 Tools --> MarkdownTOC --> Insert TOC 自动生成目录树。Sublime Text --> Preferences --> Package Settings --> MarkdownTOC --> Setting - Default 文件中默认值设置为：

	"autoanchor": true, #锚点
	"autolink": true,   #自动关联
	"uri_encoding": false,  #锚点编码（开启的时候，会把非英文锚点标记进行urincode编码，此时只有google浏览器支持自动解码，ie,360都不支持，因此建议把这里设置成false，经测试google和ie、360均可，但是锚点是中文的，不知后续是否有影响）
	"style": ordered, #生成的目录带序号，这个很棒，但是确定是不能自定义格式，默认是罗马数字

通过在自动生成的目录表头中添加设置如下可以生成带有跳转链接的目录

	<!-- MarkdownTOC autoanchor="true" autolink="true" -->

每次保存文件时可以自动刷新目录，其他问题可以点击[MaekdownTOC](https://packagecontrol.io/packages/MarkdownTOC#how-to-remove-anchors-added-by-markdowntoc)查看详细信息和用法。






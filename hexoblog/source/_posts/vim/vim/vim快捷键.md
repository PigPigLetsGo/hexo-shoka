---
title: vim
date: 2026-09-26 18:46:43
categories:
    - [vim]
tags:
    - vim
---

# Vim Markdown 快捷键速查手册

> 这份配置主要用于 **Markdown 笔记**。
>
> Leader 键：
>
> **`Space`（空格）**
>
> 例如：
>
> `Space + n` = `NERDTree`

------

# 一、最重要的 Vim 基础

## 1. 三种最常用模式

| 模式             | 进入方式        | 用途                       |
| ---------------- | --------------- | -------------------------- |
| Normal 普通模式  | `Esc`           | 移动、删除、复制、执行命令 |
| Insert 插入模式  | `i` / `a` / `o` | 输入文字                   |
| Command 命令模式 | `:`             | 执行 Vim 命令              |

### 最重要的原则

**不确定自己现在在哪个模式 → 直接按 `Esc`。**

你的 `Esc` 还有一个自定义功能：

```text
Esc
↓
取消搜索高亮
↓
让当前行居中
```

因为你还设置了：

```vim
nnoremap <esc> :noh<cr>zz
```

所以你经常按 `Esc` 就对了。

------

# 二、移动光标

## 基础移动

```text
h   ←
j   ↓
k   ↑
l   →
```

你的 `j/k` 被重新定义成：

```text
j → gj + 居中
k → gk + 居中
```

所以在自动换行的长文本中：

```text
j
k
```

移动的是**屏幕上的实际显示行**，写 Markdown 很方便。

------

## 自定义快速移动

```text
U       向上 3 行
E       向下 3 行
```

也就是：

```text
U → 3k
E → 3j
```

并且移动后自动居中。

------

## 半页滚动

```text
Space + d    向下半页
Space + u    向上半页
```

对应：

```vim
<C-d>
<C-u>
```

------

# 三、搜索

## 搜索文字

Normal 模式：

```text
/关键词
```

例如：

```text
/SDL
```

然后：

```text
Enter
```

跳到下一个：

```text
n
```

跳到上一个：

```text
Shift + n
```

你的 `Shift + n` 会自动居中。

------

## 当前单词搜索

把光标放在一个单词上：

```text
*
```

搜索下一个相同单词。

```text
#
```

搜索上一个相同单词。

你的 `*` / `#` 也会自动居中。

------

## 取消搜索高亮

```text
Esc
```

你的配置会自动执行：

```vim
:noh
```

所以不用记：

```text
:nohlsearch
```

------

# 四、跳转历史

Vim 会记录你的光标跳转位置。

```text
Ctrl + o
```

回到上一个位置。

```text
Ctrl + i
```

前进到下一个位置。

你的配置会自动居中。

------

# 五、插入文字

最常用：

```text
i       在光标前插入
a       在光标后插入
o       下一行新建并进入插入模式
O       上一行新建并进入插入模式
```

------

## 你的特殊快捷键

```text
Shift + Enter
```

相当于：

```text
o
Esc
```

也就是：

**在下一行创建新行，但马上回到 Normal 模式。**

------

## Enter 的自定义行为

你配置了：

```vim
nnoremap <CR> a<CR><Esc>k$
```

所以在 Normal 模式按：

```text
Enter
```

会：

1. 在当前行后面换行
2. 回到 Normal
3. 回到上一行
4. 光标移动到行尾

------

# 六、删除 / 修改 / 复制

这些是 Vim 原生快捷键，建议重新熟悉。

## 删除

```text
x       删除当前字符
dd      删除整行
dw      删除一个单词
D       删除到行尾
```

------

## 修改

```text
cw      修改一个单词
cc      修改整行
C       修改到行尾
```

------

## 复制

```text
yy      复制当前行
yw      复制一个单词
```

粘贴：

```text
p       在后面粘贴
P       在前面粘贴
```

------

# 七、撤销 / 重做

```text
u
```

撤销。

```text
Ctrl + r
```

重做。

------

# 八、窗口 / 分屏

你的配置：

```text
Space + q
```

关闭当前窗口。

------

## 创建竖向分屏

```text
sv
```

相当于：

```vim
<C-w>v
```

------

## 创建横向分屏

```text
ss
```

相当于：

```vim
<C-w>s
```

------

## 切换窗口

Vim 原生：

```text
Ctrl + w
h
```

切到左边。

```text
Ctrl + w
j
```

切到下面。

```text
Ctrl + w
k
```

切到上面。

```text
Ctrl + w
l
```

切到右边。

------

## 调整当前分屏大小

你的方向键被设置成了：

```text
↑       高度 +5
↓       高度 -5
←       宽度 -5
→       宽度 +5
```

所以：

```text
↑ ↓ ← →
```

在分屏状态下非常方便。

------

# 九、NERDTree 文件管理

你的配置：

```text
Ctrl + n
```

打开 NERDTree。

```text
Ctrl + t
```

打开 / 关闭 NERDTree。

```text
Ctrl + f
```

在 NERDTree 中定位当前文件。

------

## Leader 版本

```text
Space + n
```

把焦点切换到 NERDTree。

------

# 十、EasyMotion

你的 Leader：

```text
Space
```

所以：

```text
Space + l
```

向右跳。

```text
Space + h
```

向左跳。

```text
Space + j
```

向下跳。

```text
Space + k
```

向上跳。

------

使用方式大概是：

```text
Space + j
```

然后屏幕会出现一些提示字符。

按提示字符，就能快速跳到对应位置。

------

# 十一、Markdown 快捷键 ⭐

这是你这套配置最重要的部分。

按,f快速移动到<++>位置

这些快捷键**只在 Markdown 文件中生效**。

------

## 1. 粗体

Insert 模式：

```text
,b
```

得到：

```markdown
**** 
```

然后光标会进入中间。

例如：

```markdown
**重要内容**
```

------

# 2. 删除线

```text
,s
```

得到：

```markdown
~~~~
```

最终：

```markdown
~~删除的内容~~
```

------

# 3. 斜体

```text
,i
```

得到：

```markdown
**
```

用于：

```markdown
*斜体*
```

------

# 4. 行内代码

```text
,d
```

得到：

```markdown
`代码`
```

例如：

```markdown
`player.move()`
```

------

# 5. 代码块

```text
,c
```

自动生成：

~~~markdown
```


```
~~~

然后可以直接输入代码。

例如：

~~~markdown
```cpp
int main()
{
    return 0;
}
```
~~~

------

# 6. 一级标题

```text
,1
```

生成：

```markdown
# 
```

------

# 7. 二级标题

```text
,2
```

生成：

```markdown
##
```

------

# 8. 三级标题

```text
,3
```

生成：

```markdown
###
```

------

# 9. 四级标题

```text
,4
```

------

# 10. 五级标题

```text
,5
```

------

# 11. 图片

```text
,p
```

生成：

```markdown
![]()
```

------

# 12. 链接

```text
,a
```

生成：

```markdown
[]()
```

------

# 13. 分割线

```text
,l
```

生成：

```markdown
--------
```

------

# 14. 插入 `---`

```text
,n
```

会创建：

```markdown
---
```

适合快速分隔 Markdown 内容。

------

# 15. 快速创建链接

Normal 模式：

```text
Space + w
```

你的配置会执行类似：

```text
当前单词
↓
[当前单词](链接)
```

适合快速把文字变成 Markdown 链接。

------

# 十二、Markdown 图片粘贴 ⭐

你的配置：

```text
Space + i
```

调用：

```text
md-img-paste.vim
```

用于把剪贴板中的图片直接插入 Markdown。

配置说明：

dkx_img1.txt此文件为标识文件，放到要存储的img目录的根目录下注意必须明明为此错一个字就不能用了

![image-20260929221856089](../../img/image-20260929221856089.png)

```text
" source 根目录的唯一标记文件
let g:blog_source_marker = 'dkx_img1.txt'

" 图片实际保存目录
let g:blog_image_dir = 'img'
```

典型使用：

```text
截图
↓
复制图片
↓
Vim Markdown
↓
Space + i
↓
自动插入图片 Markdown
```

------

# 十三、Markdown 实时预览 ⭐

打开：

```text
README.md
```

然后执行：

```vim
:MarkdownPreview
```

就会打开浏览器实时预览。

停止预览：

```vim
:MarkdownPreviewStop
```

------

# 十四、Markdown 表格

你安装了：

```text
vim-table-mode
```

快捷键：空格 + tn

提示创建n行n列表格

快捷键：空格 + tm

打开/关闭表格模式

默认：

打开表格模式：

```vim
:TableModeToggle
```

之后可以方便地编辑：

```markdown
| 名称 | 类型 |
|------|------|
| 玩家 | Player |
| 敌人 | Enemy |
```

关闭：

```vim
:TableModeToggle
```

------

# 十五、Bullets 列表

你安装了：

```text
bullets.vim
```

主要用于：

```markdown
- 第一项
- 第二项
- 第三项
```

以及嵌套列表：

```markdown
- 第一项
  - 子项目
    - 子项目
```

------

# 十六、文件路径

你的：

```text
Space + fp
```

显示当前文件的完整路径。

例如：

```text
C:\Users\18516\Documents\Notes\game-dev.md
```

------

# 十七、保存 / 退出

虽然你没有改这些快捷键，但这几个一定要记。

## 保存

```text
:w
```

或者：

```text
:w Enter
```

------

## 保存并退出

```text
:wq
```

------

## 不保存退出

```text
:q!
```

------

## 强制保存

```text
:w!
```

------

# 十八、你最应该重新记住的快捷键

如果你不想一下子背几十个，先记下面这些。

## ⭐ 第一优先级

```text
Esc             回 Normal
i               开始输入
u               撤销
Ctrl + r        重做
dd              删除行
yy              复制行
p               粘贴
```

------

## ⭐ 第二优先级：你的个人习惯

```text
U               上 3 行
E               下 3 行

j / k           上下移动 + 居中

Space + d       下半页
Space + u       上半页

Space + q       关闭窗口

sv              竖向分屏
ss              横向分屏

↑ ↓ ← →         调整分屏大小
```

------

## ⭐ 第三优先级：Markdown

```text
,b              粗体
,i              斜体
,s              删除线
,d              行内代码
,c              代码块

,1              一级标题
,2              二级标题
,3              三级标题
,4              四级标题
,5              五级标题

,p              图片
,a              链接
,l              分割线
,n              Markdown 分隔

Space + i       粘贴图片
Space + w       当前文字 → Markdown 链接
```

------

## ⭐ 第四优先级：工具

```text
Ctrl + n        NERDTree
Ctrl + t        NERDTree 开关
Ctrl + f        定位当前文件

Space + n       NERDTree Focus

Space + h       EasyMotion 左
Space + j       EasyMotion 下
Space + k       EasyMotion 上
Space + l       EasyMotion 右

:MarkdownPreview
                Markdown 预览

:TableModeToggle
                表格模式
```

------

# 十九、一个实际的 Markdown 写作流程

以后你打开一个 Markdown 笔记，可以按照这个流程：

```text
vim game-dev.md
        │
        ↓
      Normal
        │
        ├── i       开始写
        │
        ├── ,1      创建标题
        │
        ├── ,2      创建二级标题
        │
        ├── ,b      粗体
        │
        ├── ,i      斜体
        │
        ├── ,c      代码块
        │
        ├── ,p      图片
        │
        ├── ,a      链接
        │
        ├── Space+i 图片粘贴
        │
        └── :MarkdownPreview
                    │
                    ↓
                浏览器预览
```

------

# 二十、最终速查表

| 快捷键             | 功能                      |
| ------------------ | ------------------------- |
| `Esc`              | 回 Normal / 清搜索 / 居中 |
| `i`                | 插入                      |
| `a`                | 光标后插入                |
| `o`                | 下一行插入                |
| `U`                | 上 3 行                   |
| `E`                | 下 3 行                   |
| `j/k`              | 上下移动 + 居中           |
| `Space+d`          | 下半页                    |
| `Space+u`          | 上半页                    |
| `*`                | 搜索当前单词              |
| `#`                | 反向搜索当前单词          |
| `n`                | 下一个搜索结果            |
| `Shift+n`          | 上一个搜索结果            |
| `Ctrl+o`           | 返回跳转位置              |
| `Ctrl+i`           | 前进跳转位置              |
| `u`                | 撤销                      |
| `Ctrl+r`           | 重做                      |
| `dd`               | 删除行                    |
| `yy`               | 复制行                    |
| `p`                | 粘贴                      |
| `sv`               | 竖向分屏                  |
| `ss`               | 横向分屏                  |
| `Space+q`          | 关闭窗口                  |
| `↑↓←→`             | 调整分屏                  |
| `Ctrl+n`           | NERDTree                  |
| `Ctrl+t`           | NERDTree 开关             |
| `Ctrl+f`           | NERDTree 定位             |
| `Space+n`          | NERDTree Focus            |
| `Space+h/j/k/l`    | EasyMotion                |
| `,b`               | 粗体                      |
| `,i`               | 斜体                      |
| `,s`               | 删除线                    |
| `,d`               | 行内代码                  |
| `,c`               | 代码块                    |
| `,1~5`             | 标题 1~5                  |
| `,p`               | 图片                      |
| `,a`               | 链接                      |
| `,l`               | 分割线                    |
| `,n`               | Markdown 分隔             |
| `Space+i`          | 粘贴图片                  |
| `Space+w`          | 当前文字转链接            |
| `:MarkdownPreview` | Markdown 预览             |
| `:TableModeToggle` | 表格模式                  |
| `:w`               | 保存                      |
| `:q`               | 退出                      |
| `:wq`              | 保存并退出                |
| `:q!`              | 不保存退出                |

------

# 记忆口诀

你的这套 Vim 可以简单记成：

```text
Space = 我的功能键

U / E       = 快速上下
j / k       = 正常上下
d / u       = 半页上下

sv / ss     = 分屏
Space + q   = 关窗口

Space + n   = 文件树
Space+h/j/k/l = 快速跳

,b = Bold
,i = Italic
,s = Strike
,d = Code
,c = Code Block

,1~5 = 标题
,p   = Picture
,a   = Anchor
,l   = Line
,n   = New separator

Space+i = 图片
Space+w = 链接
```

**最开始甚至不用背全部。**重新使用一两天后，`j/k`、`U/E`、`,1~5`、`,b/i/c`、`Space+i` 这些就会慢慢恢复肌肉记忆。
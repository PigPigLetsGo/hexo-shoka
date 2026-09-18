---
title: shoka-git初始化项目ai回复
categories:
    - [hexo,shoka]
tags:
    - hexo
    - shoka
---

查看.gitignore是否排除一下不必要文件夹及文件

```
.DS_Store
Thumbs.db
db.json
*.log

public/
node_modules/
.deploy*/
_multiconfig.yml
```

可以。你这个仓库：

[PigPigLetsGo/hexo-shoka](https://github.com/PigPigLetsGo/hexo-shoka.git?utm_source=chatgpt.com)

就是用来保存你这个 **Hexo + Shoka 博客源代码** 的。

你现在就在：

```
~/Desktop/hexogerenboke/hexoblog
```

而且刚才 `git status` 已经确认 `.gitignore` 正常。

### 直接按下面执行

**第 1 步：添加所有修改**

```
git add .
```

**第 2 步：检查**

```
git status
```

确认看到你刚才那 7 个文件：

```
.gitignore
_config.yml
package-lock.json
package.json
source/_data/images.yml
themes/shoka/_config.yml
themes/shoka/_images.yml
```

并且**没有**：

```
node_modules/
public/
.deploy_git/
```

------

### 第 3 步：提交

```
git commit -m "初始化 Hexo Shoka 博客"
```

------

### 第 4 步：连接你的 GitHub 仓库

先执行：

```
git remote -v
```

如果**没有任何输出**，执行：

```
git remote add origin git@github.com:PigPigLetsGo/hexo-shoka.git
```

然后检查：

```
git remote -v
```

应该显示：

```
origin  git@github.com:PigPigLetsGo/hexo-shoka.git (fetch)
origin  git@github.com:PigPigLetsGo/hexo-shoka.git (push)
```

------

### 如果已经有 `origin`

如果 `git remote -v` 显示的是其他仓库，例如：

```
origin git@github.com:PigPigLetsGo/PigPigLetsGo.github.io.git
```

**不要再执行 `git remote add origin`**，否则会提示：

```
remote origin already exists
```

直接改成你的新仓库：

```
git remote set-url origin git@github.com:PigPigLetsGo/hexo-shoka.git
```

然后：

```
git remote -v
```

确认已经变成：

```
git@github.com:PigPigLetsGo/hexo-shoka.git
```

------

### 第 5 步：把 `master` 改成 `main`

你现在显示：

```
On branch master
```

建议统一使用 `main`：

```
git branch -M main
```

------

### 第 6 步：推送到 GitHub

```
git push -u origin main
```

如果 SSH 已经配置好了，就会直接上传。

------

## 最终你整个操作就是

如果目前**没有 origin**：

```
git add .
git status
git commit -m "初始化 Hexo Shoka 博客"
git remote add origin git@github.com:PigPigLetsGo/hexo-shoka.git
git branch -M main
git push -u origin main
```

如果**已经有 origin**：

```
git add .
git status
git commit -m "初始化 Hexo Shoka 博客"
git remote set-url origin git@github.com:PigPigLetsGo/hexo-shoka.git
git branch -M main
git push -u origin main
```

### ⭐ 上传完成以后

以后你改了博客，只需要：

```
git add .
git commit -m "更新博客"
git push
```

你的 `hexo-shoka` 就是**博客源代码备份仓库**。

而你之前的：

```
PigPigLetsGo.github.io
```

继续负责 **GitHub Pages 网站部署**。

这两个仓库分开管理是很合适的

## git push -u origin main报错解决

直接执行：

```
git pull origin main --allow-unrelated-histories
```

如果出现合并界面或者提示冲突，**先不要继续操作，把完整输出发给我**。

如果执行后没有冲突，并且成功合并，再执行：

```
git push -u origin main
```

------

### ⚠️ 不要现在用 `git push --force`

虽然：

```
git push -f origin main
```

也能解决，但它会**强制覆盖 GitHub 远程仓库现有内容**。

如果 `hexo-shoka` 仓库里面只是 GitHub 创建时自动生成的 README，那么也可以直接覆盖；但目前我们还不知道远程仓库里面到底有什么，所以**先 pull 合并更安全**

很好，**已经成功合并了**。✅

从这里可以确认：

```
Merge made by the 'ort' strategy.
README.md | 2 ++
create mode 100644 README.md
```

说明 GitHub 远程仓库原本只有一个 `README.md`，现在已经和你的本地 Hexo 项目合并，没有冲突。

### 现在最后一步

直接执行：

```
git push -u origin main
```

这次应该就可以正常上传。

成功后通常会看到类似：

```
To github.com:PigPigLetsGo/hexo-shoka.git
   xxxxxxx..xxxxxxx  main -> main
branch 'main' set up to track 'origin/main'.
```

### 上传完成后

你的仓库：

```
PigPigLetsGo/hexo-shoka
```

里面应该会有你的：

```
_config.yml
package.json
package-lock.json
source/
themes/
.gitignore
README.md
```

而这些**不会上传**：

```
node_modules/
public/
.deploy_git/
```

因为已经被 `.gitignore` 排除了。

现在直接运行：

```
git push -u origin main
```

然后把结果发我，我可以帮你确认 **整个 Hexo Shoka 源码是否已经完整上传**

# 新电脑git使用

我每次将博客源文件上传github的hexo-shoka时不需要先拉后推 而是直接推送对吗？

对，**但有一个前提**：只有当远程 `hexo-shoka` 仓库没有别人/其他电脑产生的新提交时，你才可以直接推送。

你现在是自己一个人维护这个源码仓库，而且平时都是**当前电脑修改 → 上传 GitHub**，那么日常完全可以直接：

```
git add .
git commit -m "更新博客"
git push
```

不需要每次：

```
git pull
git push
```

### 你可以这样理解

你的工作流程：

```
修改博客
   ↓
git add .
   ↓
git commit -m "更新博客"
   ↓
git push
   ↓
GitHub：hexo-shoka
```

就够了。

------

### ⚠️ 什么时候必须先 `pull`？

如果出现这种情况：

```
电脑A → push → GitHub
                  ↑
电脑B → 现在也要 push
```

电脑 B 本地没有电脑 A 最新的提交，这时候直接：

```
git push
```

可能会出现：

```
rejected
fetch first
```

这时才需要：

```
git pull --rebase
```

然后再：

```
git push
```

------

### 对你来说最重要的是

你以后**同一台电脑持续写博客**：

```
git add .
git commit -m "更新博客"
git push
```

就行。

**换电脑之后**，第一次：

```
git clone git@github.com:PigPigLetsGo/hexo-shoka.git
```

之后在新电脑继续修改，也可以直接：

```
git add .
git commit -m "更新博客"
git push
```

但是如果你在**旧电脑和新电脑交替修改**，就要养成习惯：

```
git pull --rebase
```

再开始修改/推送，避免两台电脑的提交发生分叉。

另外要注意：**`git push` 是上传源码到 `hexo-shoka`，`npx hexo d` 才是发布网站到 `PigPigLetsGo.github.io`。** 两个操作不是一回事
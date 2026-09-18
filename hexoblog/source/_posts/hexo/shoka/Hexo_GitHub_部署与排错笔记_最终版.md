---
title: Hexo_GitHub_部署与排错笔记_最终版
categories:
    - [hexo,shoka]
tags:
    - hexo
    - shoka
---

# Hexo + GitHub 部署与排错终极小白版

> 适用：Windows + Hexo 4.2.1 +node.jsv10.24.1+ Shoka 主题 + GitHub Pages  
> 目标：**遇到问题照着对应步骤复制命令，最后成功部署。**
>
> ⚠️ 说明：下面命令默认在你的 Hexo 博客根目录执行，例如：
> `C:\Users\18516\Desktop\hexogerenboke\hexoblog`

---

# 一、先记住最常用的 4 个命令

```powershell
npx hexo clean
npx hexo g
npx hexo s
npx hexo d
```

含义：

| 命令 | 作用 |
|---|---|
| `npx hexo clean` | 清理旧生成文件 |
| `npx hexo g` | 重新生成网站 |
| `npx hexo s` | 本地启动预览 |
| `npx hexo d` | 部署到 GitHub |

### 最常用流程

修改博客后：

```powershell
npx hexo clean
npx hexo g
npx hexo s
```

确认本地没问题后：

```powershell
npx hexo d
```

---

# 二、问题 1：hexo-theme-landscape 插件报错

## 看到这个错误

```text
ERROR Plugin load failed: hexo-theme-landscape
Error: EISDIR: illegal operation on a directory, read
```

## 原因

你的博客实际使用的是 **Shoka 主题**，但项目里还加载了不需要的：

```text
hexo-theme-landscape
```

这个插件/主题导致 Hexo 启动时加载失败。

## 直接修复

在 Hexo 根目录执行：

```powershell
npm uninstall hexo-theme-landscape
```

然后：

```powershell
npx hexo clean
npx hexo g
```

如果没有报错，再启动：

```powershell
npx hexo s
```

### 一句话记忆

> **看到 `hexo-theme-landscape` + `EISDIR` → 删除 `hexo-theme-landscape`。**

---

# 三、问题 2：Cannot find module 'stylus'

## 看到这个错误

```text
Cannot find module 'stylus'
```

## 原因

主题需要 `stylus`，但项目没有安装这个依赖。

## 直接修复

执行：

```powershell
npm install stylus@0.54.8 --save
```

然后：

```powershell
npx hexo clean
npx hexo g
```

再启动：

```powershell
npx hexo s
```

### 一句话记忆

> **看到 `Cannot find module 'stylus'` → 安装 `stylus@0.54.8`。**

---

# 四、问题 3：`git` 不是内部或外部命令 / spawn git ENOENT

## 看到这个错误

```text
'git' 不是内部或外部命令，也不是可运行的程序
```

或者：

```text
Error: spawn git ENOENT
```

## 原因

Windows 没有安装 Git，或者 Git 没有加入 PATH。

## 修复

先安装 Git for Windows。

安装完成后，**关闭当前 PowerShell，再重新打开**。

检查：

```powershell
git --version
```

如果出现类似：

```text
git version 2.xx.x
```

说明 Git 正常。

然后：

```powershell
npx hexo d
```

---

# 五、问题 4：GitHub SSH Permission denied (publickey)

## 看到这个错误

```text
git@github.com: Permission denied (publickey).
fatal: Could not read from the remote repository.
```

## 原因

SSH 密钥已经生成，但 GitHub 还没有信任你的公钥。

---

## 第一步：生成 SSH 密钥

如果还没有密钥：

```powershell
ssh-keygen -t ed25519 -C "你的GitHub邮箱"
```

一路按 Enter 即可。

例如：

```powershell
ssh-keygen -t ed25519 -C "1851644015@qq.com"
```

通常会生成：

```text
C:\Users\你的用户名\.ssh\id_ed25519
C:\Users\你的用户名\.ssh\id_ed25519.pub
```

---

## 第二步：复制公钥

执行：

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

复制显示出来的**整整一行**。

注意：

> 复制的是 `id_ed25519.pub`  
> **不是** `id_ed25519`

⚠️ **绝对不要把私钥 `id_ed25519` 发给别人。**

---

## 第三步：添加到 GitHub

进入 GitHub：

`Settings → SSH and GPG keys → New SSH key`

填写：

```text
Title:
Windows Hexo
```

Key type：

```text
Authentication Key
```

把刚才复制的公钥粘贴进去并保存。

---

## 第四步：测试 SSH

执行：

```powershell
ssh -i $env:USERPROFILE\.ssh\id_ed25519 -T git@github.com
```

成功一般会看到：

```text
Hi 用户名! You've successfully authenticated, but GitHub does not provide shell access.
```

看到这句话：

> **说明 GitHub SSH 已经成功。**

然后执行：

```powershell
npx hexo d
```

---

# 六、问题 5：ssh-agent 启动失败 / Access is denied

## 可能看到

```text
Access is denied
```

或者：

```text
Start-Service ssh-agent
```

无法启动。

## 小白最简单处理

**不用折腾 ssh-agent。**

直接指定 SSH 私钥：

```powershell
ssh -i $env:USERPROFILE\.ssh\id_ed25519 -T git@github.com
```

如果成功，再：

```powershell
npx hexo d
```

---

# 七、问题 6：第一次连接 GitHub 出现真实性确认

第一次执行 SSH 时可能看到：

```text
The authenticity of host 'github.com' can't be established.
```

以及：

```text
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

确认你连接的是 GitHub 后输入：

```text
yes
```

之后通常会保存 GitHub 的主机密钥，不需要每次输入。

---

# 八、Hexo 搜索报错：Identifier 't' has already been declared

## 看到浏览器报错

```text
Uncaught SyntaxError: Identifier 't' has already been declared
```

## 原因

之前项目中的 Algolia 搜索相关脚本与当前搜索代码发生冲突。

你的项目实际使用的是：

```text
search.json
```

本地搜索，不需要继续加载 Algolia。

## 修复 `_config.yml`

找到：

```yaml
plugins:
  - hexo-algoliasearch
```

改成：

```yaml
plugins: []
```

同时检查 `vendors.js` 配置。

如果里面有：

```yaml
algolia:
instantsearch:
```

相关配置，可以删除或注释掉。

然后：

```powershell
npx hexo clean
npx hexo g
npx hexo s
```

---

# 九、MiniValine / Valine 评论区 404

## 看到类似错误

```text
GET https://cdn.jsdelivr.net/gh/MiniValine/minivaline-i18n@latest/zh-CN/index.json 404
```

或者：

```text
GET https://cdn.jsdelivr.net/gh/MiniValine/minivaline-i18n@latest/en/index.json 404
```

## 原因

这是旧版 MiniValine 的国际化资源请求问题。

即使把：

```yaml
lang: zh-CN
```

改成：

```yaml
lang: en
```

仍然可能 404。

## 当时采用的处理方式

**不继续修 MiniValine，直接关闭 Valine。**

把 `_config.yml` 里的整个：

```yaml
valine:
```

配置块注释掉。

同时把 `vendors.js` 中的：

```yaml
valine: gh/amehime/MiniValine@4.2.2-beta10/dist/MiniValine.min.js
```

注释掉：

```yaml
# valine: gh/amehime/MiniValine@4.2.2-beta10/dist/MiniValine.min.js
```

然后：

```powershell
npx hexo clean
npx hexo g
npx hexo s
```

### 一句话记忆

> **MiniValine i18n 404 → 不想修旧评论系统，就直接关闭 Valine。**

---

# 十、Live2D deprecated 警告

## 看到

```text
Live2D widget version 0 is deprecated, please use version 1 instead
```

## 这是什么？

这是：

> **旧版本提示，不一定是运行错误。**

如果 Live2D 还能正常显示，可以暂时不处理。

以后需要升级时，再把：

```text
live2d-widgets
```

升级到新版即可。

### 一句话记忆

> **能正常显示 → 暂时不用管。**

---

# 十一、Hexo 本地启动的标准排错顺序

如果你不知道到底哪里出了问题，按照下面顺序执行。

## ① 清理

```powershell
npx hexo clean
```

## ② 重新生成

```powershell
npx hexo g
```

## ③ 启动

```powershell
npx hexo s
```

---

## 如果 `hexo clean` / `hexo g` 报错

### A. 出现

```text
hexo-theme-landscape
```

执行：

```powershell
npm uninstall hexo-theme-landscape
```

### B. 出现

```text
Cannot find module 'stylus'
```

执行：

```powershell
npm install stylus@0.54.8 --save
```

然后重新：

```powershell
npx hexo clean
npx hexo g
npx hexo s
```

---

# 十二、部署 GitHub Pages

本地确认正常后：

```powershell
npx hexo d
```

正常流程应该类似：

```text
INFO  Deploying: git
...
INFO  Deploy done
```

看到：

```text
Deploy done
```

基本就说明 Hexo 部署完成。

---

# 十三、`hexo d` 和 `git push` 不一样

这是非常容易搞混的地方。

## `npx hexo d`

作用：

> **把生成好的网站部署到 GitHub Pages。**

一般用于让网站更新。

---

## `git push`

作用：

> **把你的 Hexo 源代码仓库上传到 GitHub。**

例如：

```powershell
git add .
git commit -m "更新博客"
git push
```

### 简单理解

```text
Hexo源代码
   ↓
npx hexo g
   ↓
生成网站
   ↓
npx hexo d
   ↓
GitHub Pages网站
```

而：

```text
Hexo源代码
   ↓
git add
   ↓
git commit
   ↓
git push
   ↓
GitHub源代码仓库
```

两者用途不同。

---

# 十四、第一次上传 Hexo 源代码到 GitHub

如果还没有 Git 仓库：

```powershell
git init
```

查看状态：

```powershell
git status
```

添加文件：

```powershell
git add .
```

提交：

```powershell
git commit -m "初始化博客"
```

设置主分支：

```powershell
git branch -M main
```

添加 GitHub 仓库：

```powershell
git remote add origin git@github.com:用户名/仓库名.git
```

检查：

```powershell
git remote -v
```

最后：

```powershell
git push -u origin main
```

---

# 十五、建议 `.gitignore`

Hexo 源代码仓库建议添加：

```gitignore
node_modules/
public/
.deploy_git/
db.json
.DS_Store
Thumbs.db
```

然后：

```powershell
git add .
git commit -m "更新博客"
git push
```

---

# 十六、非常重要：不要上传 SSH 私钥

下面这个文件：

```text
C:\Users\你的用户名\.ssh\id_ed25519
```

是：

> **SSH 私钥**

绝对不要上传到 GitHub，也不要发给别人。

可以公开的是：

```text
id_ed25519.pub
```

但一般也没必要公开展示。

---

# 十七、`_config.yml` 里的密钥也要注意

如果 `_config.yml` 里存在：

```yaml
appId:
appKey:
```

或者其他 API Key / Secret：

> 上传 GitHub 前一定检查是否应该公开。

`.gitignore` 只能防止**以后被提交**。

如果密钥以前已经提交进 Git 历史：

> 单纯删除文件或加入 `.gitignore` **不能自动清除历史记录**。

---

# 十八、最简单的“无脑部署流程”

以后改完博客，直接按照这个顺序。

## 第 1 步：进入博客目录

例如：

```powershell
cd C:\Users\18516\Desktop\hexogerenboke\hexoblog
```

## 第 2 步：清理

```powershell
npx hexo clean
```

## 第 3 步：生成

```powershell
npx hexo g
```

## 第 4 步：本地测试

```powershell
npx hexo s
```

浏览器打开 Hexo 提示的本地地址。

确认：

- 页面正常
- 文章正常
- 图片正常
- 搜索正常
- 没有明显报错

然后按 `Ctrl + C` 停止本地服务。

## 第 5 步：部署

```powershell
npx hexo d
```

完成。

---

# 十九、如果部署失败，先看是哪一类

| 错误关键词 | 直接处理 |
|---|---|
| `hexo-theme-landscape` | `npm uninstall hexo-theme-landscape` |
| `EISDIR` + `hexo-theme-landscape` | 删除 `hexo-theme-landscape` |
| `Cannot find module 'stylus'` | `npm install stylus@0.54.8 --save` |
| `'git' 不是内部或外部命令` | 安装 Git / 检查 PATH |
| `spawn git ENOENT` | 安装 Git / 检查 PATH |
| `Permission denied (publickey)` | 检查 GitHub SSH 公钥 |
| `authenticity of host` | 首次连接输入 `yes` |
| `Identifier 't' has already been declared` | 检查/关闭 Algolia 冲突 |
| `MiniValine ... 404` | 关闭旧版 Valine |
| `Live2D ... deprecated` | 能正常运行可暂时忽略 |

---

# 二十、终极排错口诀

```text
Hexo 启动失败
↓
先看错误关键词
↓
landscape → 删除
stylus → 安装
↓
重新 clean + g
↓
本地 s 测试
↓
Git 报错
↓
git --version
↓
SSH 报错
↓
检查 GitHub 公钥
↓
ssh -i 私钥 -T git@github.com
↓
认证成功
↓
npx hexo d
↓
部署完成
```

---

# 二十一、最终备用命令清单

### Hexo

```powershell
npx hexo clean
npx hexo g
npx hexo s
npx hexo d
```

### 删除错误主题插件

```powershell
npm uninstall hexo-theme-landscape
```

### 安装 Stylus

```powershell
npm install stylus@0.54.8 --save
```

### 检查 Git

```powershell
git --version
```

### 查看 SSH 公钥

```powershell
Get-Content $env:USERPROFILE\.ssh\id_ed25519.pub
```

### 测试 GitHub SSH

```powershell
ssh -i $env:USERPROFILE\.ssh\id_ed25519 -T git@github.com
```

### 查看 Git 远程仓库

```powershell
git remote -v
```

### 上传源代码

```powershell
git add .
git commit -m "更新博客"
git push
```

---

# 二十二、成功标准

最后只需要记住这几个结果。

### Hexo 能生成

```text
INFO  Generated:
```

### Hexo 能启动

```text
INFO  Hexo is running
```

### SSH 成功

```text
Hi 用户名! You've successfully authenticated
```

### Hexo 部署成功

```text
INFO  Deploy done
```

如果这几个都正常：

> **你的 Hexo + GitHub Pages 基本就部署成功了。**

---

# 最后给小白的一句话

遇到问题不要乱删文件。

**先看报错里的关键词 → 对照本笔记 → 执行对应命令 → `clean` → `g` → `s` → 确认正常 → `d`。**

这样排错最安全，也最不容易把 Hexo 项目弄坏。

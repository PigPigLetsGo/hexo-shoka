---
title: shoka更换电脑私钥使用已有配置
categories:
    - [hexo,shoka]
tags:
    - hexo
    - shoka
---

下面这份你可以直接保存成 `GitHub_SSH私钥_换电脑使用.md`。

```
# GitHub SSH 私钥备份与换电脑使用教程

> 适用于 Windows + Git + GitHub + Hexo 博客项目

---

## 一、目前的 SSH 文件

当前电脑的 SSH 文件位于：

```text
C:\Users\18516\.ssh\
├── id_ed25519
└── id_ed25519.pub
```

其中：

| 文件             | 作用     | 是否可以公开   |
| ---------------- | -------- | -------------- |
| `id_ed25519`     | SSH 私钥 | ❌ 绝对不能公开 |
| `id_ed25519.pub` | SSH 公钥 | ✅ 可以公开     |

### 特别注意

**`id_ed25519` 是最重要的私钥文件。**

不要：

- 上传到 GitHub
- 发给别人
- 放进 Hexo 项目
- 放进博客 `source` 目录
- 放进 Git 仓库
- 发到 QQ、微信、论坛等公开位置

------

# 二、备份 SSH 私钥到 U 盘

## 1. 打开 SSH 文件夹

在 Windows 文件资源管理器地址栏输入：

```
C:\Users\18516\.ssh
```

里面应该能看到：

```
id_ed25519
id_ed25519.pub
```

------

## 2. 在 U 盘建立备份文件夹

例如：

```
U盘
└── GitHub-SSH-备份
```

把下面两个文件复制进去：

```
id_ed25519
id_ed25519.pub
```

最终：

```
U盘
└── GitHub-SSH-备份
    ├── id_ed25519
    └── id_ed25519.pub
```

------

# 三、强烈建议给私钥做加密备份

因为：

```
id_ed25519
```

属于私密凭证。

建议不要让它以普通文件形式长期放在容易丢失的 U 盘中。

可以将：

```
id_ed25519
id_ed25519.pub
```

放入一个带密码的加密压缩包。

例如：

```
GitHub-SSH-备份.7z
```

并设置一个只有自己知道的强密码。

------

# 四、换新电脑后的操作

假设新电脑已经安装：

- Git
- Node.js

------

## 1. 创建 SSH 文件夹

打开 Git Bash：

```
mkdir -p ~/.ssh
```

------

## 2. 从 U 盘复制 SSH 文件

把：

```
U盘\GitHub-SSH-备份\id_ed25519
U盘\GitHub-SSH-备份\id_ed25519.pub
```

复制到新电脑：

```
C:\Users\你的用户名\.ssh\
```

最终：

```
C:\Users\你的用户名\.ssh\
├── id_ed25519
└── id_ed25519.pub
```

------

# 五、设置私钥权限

打开 Git Bash：

```
chmod 600 ~/.ssh/id_ed25519
```

这样可以限制私钥文件的访问权限。

------

# 六、测试 GitHub SSH

执行：

```
ssh -i ~/.ssh/id_ed25519 -T git@github.com
```

第一次连接 GitHub 时可能出现：

```
The authenticity of host 'github.com' can't be established.
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

输入：

```
yes
```

然后回车。

------

## 七、看到这个就说明成功

如果出现：

```
Hi PigPigLetsGo! You've successfully authenticated, but GitHub does not provide shell access.
```

说明：

```
新电脑
   ↓
SSH 私钥
   ↓
GitHub
   ↓
认证成功
```

此时不需要重新生成 SSH Key。

------

# 八、测试 GitHub 仓库

进入你准备存放 Hexo 项目的目录，例如：

```
cd ~/Desktop
```

然后：

```
git clone git@github.com:PigPigLetsGo/hexo-shoka.git
```

成功后会得到：

```
hexo-shoka/
├── source/
├── themes/
├── scaffolds/
├── _config.yml
├── package.json
├── package-lock.json
├── .gitignore
└── README.md
```

------

# 九、安装 Hexo 项目依赖

进入项目：

```
cd hexo-shoka
```

然后：

```
npm install
```

这一步会根据：

```
package.json
package-lock.json
```

重新安装项目依赖。

**不需要把旧电脑的 `node_modules` 复制过来。**

------

# 十、测试 Hexo

执行：

```
npx hexo clean
```

然后：

```
npx hexo g
```

最后：

```
npx hexo s
```

浏览器打开：

```
http://localhost:4000
```

如果博客正常显示，就说明换电脑恢复成功。

------

# 十一、继续写博客

以后就可以正常创建文章：

```
npx hexo new "我的新笔记"
```

编辑：

```
source/_posts/
```

里面的 Markdown 文件。

------

# 十二、部署博客网站

写完文章以后：

```
npx hexo clean
npx hexo g
npx hexo d
```

其中：

```
hexo g
```

负责生成网站。

```
hexo d
```

负责部署到 GitHub Pages。

------

# 十三、同步博客源代码

修改了博客源代码、文章、配置等内容以后，同时提交到自己的源代码仓库：

```
git add .
```

然后：

```
git commit -m "更新博客"
```

最后：

```
git push
```

源代码仓库：

```
https://github.com/PigPigLetsGo/hexo-shoka
```

------

# 十四、我的两个 GitHub 仓库分别是什么

## 1. Hexo 源代码仓库

```
hexo-shoka
```

地址：

```
git@github.com:PigPigLetsGo/hexo-shoka.git
```

用途：

```
保存 Hexo 博客源代码
保存文章
保存 Shoka 主题
保存配置文件
保存 package.json
保存博客资源
```

------

## 2. GitHub Pages 网站仓库

```
PigPigLetsGo.github.io
```

用途：

```
保存 Hexo 生成后的网页
```

也就是最终访问的博客网站。

------

# 十五、换电脑后的完整流程

以后换电脑，可以按照下面顺序：

```
① 安装 Git
       ↓
② 安装 Node.js
       ↓
③ 从 U 盘恢复 SSH 私钥
       ↓
④ 测试 GitHub SSH
       ↓
⑤ git clone hexo-shoka
       ↓
⑥ npm install
       ↓
⑦ npx hexo g
       ↓
⑧ npx hexo s
       ↓
⑨ 检查博客
       ↓
⑩ 继续写文章
```

------

# 十六、最重要的安全注意事项

## ❌ 不要上传私钥

绝对不要把：

```
id_ed25519
```

放进：

```
hexo-shoka/
```

也不要执行：

```
git add id_ed25519
```

------

## ❌ 不要把私钥上传 GitHub

GitHub 上应该只有：

```
SSH 公钥
```

而不是：

```
SSH 私钥
```

------

## ❌ 不要把私钥发给任何人

不要通过：

```
QQ
微信
邮箱
GitHub Issue
论坛
聊天软件
```

发送：

```
id_ed25519
```

------

# 十七、如果 U 盘丢失怎么办？

如果只是 U 盘丢失，但：

```
id_ed25519
```

没有泄露，则问题不大。

如果怀疑私钥已经被别人获得，应立即到 GitHub：

```
Settings
→ SSH and GPG keys
```

找到对应的 SSH Key 并删除。

然后在新电脑重新生成 SSH Key：

```
ssh-keygen -t ed25519 -C "你的邮箱"
```

再把新的：

```
id_ed25519.pub
```

添加到 GitHub。

------

# 十八、当前我的 SSH Key 信息

当前使用：

```
算法：Ed25519
邮箱：1851644015@qq.com
```

私钥：

```
id_ed25519
```

公钥：

```
id_ed25519.pub
```

GitHub 用户：

```
PigPigLetsGo
```

源代码仓库：

```
git@github.com:PigPigLetsGo/hexo-shoka.git
```

------

# 十九、最终记住这句话

> **GitHub 保存代码，U 盘备份 SSH 私钥，新电脑安装 Git + Node.js 后恢复私钥，再 clone 项目，就可以继续写博客。**

```
旧电脑
   │
   ├── GitHub：保存 Hexo 源代码
   │
   └── U盘：安全备份 SSH 私钥
             ↓
          换新电脑
             ↓
       安装 Git + Node.js
             ↓
       恢复 SSH 私钥
             ↓
       git clone
             ↓
         npm install
             ↓
       Hexo 博客恢复
             ↓
         继续写笔记
```
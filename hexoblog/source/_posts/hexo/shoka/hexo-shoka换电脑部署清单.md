---
title: hexo-shoka换电脑部署清单
categories:
    - [hexo,shoka]
tags:
    - hexo
    - shoka
---

我换电脑后hexo-4.2.1.tgz我应该解压到哪里？

不用解压。**`hexo-4.2.1.tgz` 是 npm 安装包，不是让你手动解压到某个文件夹里的。**

你换电脑后，推荐这样做：

### ① 先把你的博客源码克隆下来

例如：

```
cd C:\Users\你的用户名\Desktop
git clone git@github.com:PigPigLetsGo/hexo-shoka.git
cd hexo-shoka
```

### ② 安装项目依赖

你的项目里已经有：

```
package.json
package-lock.json
```

所以正常情况下直接：

```
npm install
```

就会按照 `package-lock.json` 安装对应版本。

------

### ③ 如果你要使用自己备份的 `hexo-4.2.1.tgz`

假设你把 U 盘里的：

```
hexo-4.2.1.tgz
```

复制到了博客目录：

```
C:\Users\你的用户名\Desktop\hexo-shoka\
```

那么**不要解压**，直接：

```
npm install .\hexo-4.2.1.tgz --save
```

它会自动把 Hexo 安装到：

```
hexo-shoka\node_modules\hexo\
```

------

### ④ 你的情况我更推荐这样

因为你已经有完整的 `package.json + package-lock.json`，所以换电脑时：

```
git clone git@github.com:PigPigLetsGo/hexo-shoka.git
cd hexo-shoka
npm install
npx hexo -v
```

如果显示：

```
hexo: 4.2.1
```

就说明恢复好了。

如果 `npm install` 因为旧依赖下载失败，再使用你备份的 `hexo-4.2.1.tgz`。

------

### 你可以记住一个关键点

```
hexo-4.2.1.tgz
        ↓
   不要手动解压
        ↓
npm install .\hexo-4.2.1.tgz
        ↓
node_modules\hexo\
```

而你的博客源码应该放在：

```
hexo-shoka\
├── _config.yml
├── package.json
├── package-lock.json
├── source\
├── themes\
└── node_modules\
```

**所以 `.tgz` 只是安装包备份，不需要放进博客项目长期保存。** 安装成功后可以把它放回 U 盘保存。

另外，你之前的 **Node.js 10.24.1** 和 **hexo-cli 4.3.2** 也最好一起备份；这样换电脑后可以把整个环境尽可能恢复到现在这个状态

# 🖥️ Hexo 换电脑完整恢复流程

你的最终目标是恢复成：

```
Windows 10
Node.js 10.24.1
npm 6.14.12
Hexo 4.2.1
hexo-cli 4.3.2
Shoka
```

并继续使用：

```
GitHub 源码仓库
git@github.com:PigPigLetsGo/hexo-shoka.git

GitHub Pages
git@github.com:PigPigLetsGo/PigPigLetsGo.github.io.git
```

------

## 一、准备 U 盘备份

建议 U 盘整理成：

```
Hexo博客完整备份
│
├─01-Node环境
│   └─node-v10.24.1-x64.msi
│
├─02-Hexo安装包
│   ├─hexo-4.2.1.tgz
│   └─hexo-cli-4.3.2.tgz
│
├─03-版本记录
│   ├─hexo-version.txt
│   └─hexo-environment-packages.txt
│
└─04-SSH
    ├─id_ed25519
    └─id_ed25519.pub
```

其中：

⚠️ `id_ed25519` 是**私钥**，不要上传 GitHub、不要发给别人。

------

# 二、新电脑安装 Node.js

安装：

```
node-v10.24.1-x64.msi
```

安装完成后打开 PowerShell：

```
node -v
```

应该得到：

```
v10.24.1
```

再：

```
npm -v
```

应该得到：

```
6.14.12
```

------

# 三、安装 Git

安装 Git for Windows。

然后检查：

```
git --version
```

例如：

```
git version 2.xx.x
```

Git 的具体小版本不用和旧电脑完全一样。

------

# 四、恢复 SSH

新电脑打开 PowerShell：

```
New-Item -ItemType Directory -Force "$env:USERPROFILE\.ssh"
```

然后把 U 盘里的：

```
id_ed25519
id_ed25519.pub
```

复制到：

```
C:\Users\你的用户名\.ssh\
```

最终：

```
C:\Users\你的用户名\.ssh\id_ed25519
C:\Users\你的用户名\.ssh\id_ed25519.pub
```

然后测试：

```
ssh -T git@github.com
```

第一次可能出现：

```
Are you sure you want to continue connecting (yes/no/[fingerprint])?
```

输入：

```
yes
```

成功应该看到类似：

```
Hi PigPigLetsGo! You've successfully authenticated, but GitHub does not provide shell access.
```

看到这个就说明 SSH 恢复成功。

------

# 五、克隆你的博客源码

例如放到桌面：

```
cd "$env:USERPROFILE\Desktop"
```

然后：

```
git clone git@github.com:PigPigLetsGo/hexo-shoka.git
```

进入：

```
cd hexo-shoka
```

检查：

```
dir
```

应该能看到：

```
_config.yml
package.json
package-lock.json
source
themes
...
```

------

# 六、安装博客依赖

这是最重要的一步。

直接：

```
npm install
```

因为你已经有：

```
package.json
package-lock.json
```

npm 会按照项目记录安装依赖。

------

# 七、检查 Hexo

运行：

```
npx hexo -v
```

你应该看到：

```
hexo: 4.2.1
hexo-cli: 4.3.2
os: win32 ...
node: 10.24.1
...
```

这里重点检查：

```
hexo: 4.2.1
hexo-cli: 4.3.2
node: 10.24.1
```

------

# 八、如果 npm install 出现依赖问题

这时候再使用你备份的：

```
hexo-4.2.1.tgz
```

例如把它复制到博客根目录：

```
hexo-shoka\
├── hexo-4.2.1.tgz
├── package.json
├── package-lock.json
└── ...
```

然后：

```
npm install .\hexo-4.2.1.tgz --save
```

再检查：

```
npx hexo -v
```

------

# 九、恢复 Hexo CLI

如果新电脑没有：

```
hexo-cli: 4.3.2
```

可以安装：

```
npm install -g hexo-cli@4.3.2
```

然后：

```
hexo -v
```

如果你备份了：

```
hexo-cli-4.3.2.tgz
```

也可以离线安装：

```
npm install -g .\hexo-cli-4.3.2.tgz
```

------

# 十、第一次生成博客

进入博客目录：

```
cd "$env:USERPROFILE\Desktop\hexo-shoka"
```

然后：

```
npx hexo clean
```

再：

```
npx hexo g
```

如果成功，会出现类似：

```
INFO  Start processing
INFO  Files loaded in ...
INFO  0 files generated
```

或者生成大量页面。

------

# 十一、启动本地博客

```
npx hexo s
```

看到：

```
Hexo is running at http://localhost:4000/
```

浏览器打开：

```
http://localhost:4000/
```

检查：

- 首页
- 文章
- 图片
- Shoka 主题
- 搜索
- 音乐播放器
- Live2D
- 评论相关功能
- 其他你目前已经修改过的效果

------

# 十二、确认没问题后部署

先生成：

```
npx hexo clean
npx hexo g
```

然后：

```
npx hexo d
```

你的 `_config.yml` 中部署仓库已经是：

```
git@github.com:PigPigLetsGo/PigPigLetsGo.github.io.git
```

所以 `hexo d` 会把生成后的博客部署到 GitHub Pages。

------

# 十三、以后正常写博客只需要这几步

以后换电脑恢复好以后，日常其实非常简单。

### 写文章

```
npx hexo new "文章标题"
```

编辑：

```
source\_posts\
```

### 本地预览

```
npx hexo s
```

### 发布

```
npx hexo clean
npx hexo g
npx hexo d
```

### 保存源码到 GitHub

```
git add .
git commit -m "更新博客"
git push
```

------

# 十四、以后最重要的两个命令

你这个项目有**两个 GitHub 仓库**，不要搞混：

### ① 保存博客源码

```
git add .
git commit -m "更新博客"
git push
```

推送到：

```
PigPigLetsGo/hexo-shoka
```

### ② 发布网站

```
npx hexo g
npx hexo d
```

发布到：

```
PigPigLetsGo/PigPigLetsGo.github.io
```

也就是说：

```
                你的电脑
                   │
          ┌────────┴────────┐
          ↓                 ↓
     git push             hexo d
          │                 │
          ↓                 ↓
   hexo-shoka        PigPigLetsGo.github.io
   【源码备份】          【网站成品】
```

------

# 十五、最后做一次完整验证

换电脑恢复完成后，建议执行这一整套：

```
node -v
npm -v
git --version
npx hexo -v
```

然后：

```
git remote -v
```

应该看到源码仓库：

```
origin  git@github.com:PigPigLetsGo/hexo-shoka.git
```

然后：

```
npx hexo clean
npx hexo g
npx hexo s
```

浏览器确认：

```
http://localhost:4000/
```

确认无误后：

```
npx hexo d
```

这样你这套博客基本就实现了**“电脑坏了也能从 GitHub + U 盘恢复”**。

------

## ⭐ 你现在还差一个备份

你刚才已经确认了所有 npm 依赖：

```
hexo 4.2.1
hexo-autoprefixer 2.0.0
hexo-deployer-git 2.1.0
hexo-feed 1.1.1
hexo-generator-archive 2.0.0
hexo-generator-category 1.0.0
hexo-generator-index 3.0.0
hexo-generator-searchdb 1.4.1
hexo-generator-tag 1.0.0
hexo-renderer-ejs 1.0.0
hexo-renderer-multi-markdown-it 0.1.5
hexo-renderer-stylus 2.1.0
hexo-server 2.0.0
hexo-symbols-count-time 0.7.1
quicklink 2.3.0
stylus 0.54.8
webpack-route-manifest 1.3.0
```

现在在**旧电脑**再执行：

```
npm pack hexo-cli@4.3.2
```

这样你就同时有：

```
hexo-4.2.1.tgz
hexo-cli-4.3.2.tgz
```

然后再执行：

```
npm list --depth=0 > hexo-environment-packages.txt
```

这份文件也放进 U 盘。

**这样你这套 Hexo 4.2.1 环境的恢复资料就比较完整了**
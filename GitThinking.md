# Git手册

## 为什么用Git

用于记录项目的每一次修改历史，管理多个版本和分支。在形成最终结果之前会有许多历史版本以及可能的分支，这些历史版本和分支或许能指向一个不同的结果，利用Git可以回退到任何一个阶段，类似于游戏存档。

## 基础操作

### init

将一个文件夹变成Git仓库repository，多出.git隐藏文件夹用于存放所有历史版本

### status

查看当前工作区、暂存区的状态，了解每个文件都发生了什么变化或者没变化，工作区相对于暂存区是否有新的修改。

### add

把本次要提交的修改放到暂存区

### commit

把暂存区保存成为一个新的历史版本

**思考**
如果跳过add直接commit可能会判定暂存区没有要修改的东西从而不进行修改。为什么要有暂存区呢？让用户可以精确选择本次到底要提交哪些修改

### log

会列出当前分支的所有历史存档，如果要看到分叉关系log --all --graph
包括commit ID、产生时间、修改内容、母commit

### commit tree

commit记录着母commit的ID，以便于回溯。普通commit通常只有一个parent，但merge commit可以有多个parent。多个commit可以有同一个parent。

### branch ref

随着提交移动的名字，标识不同的分支

### HEAD

branch指向commit，而HEAD指向branch，为了告诉Git现在我在哪个分支上

**注意**
Working Tree是工作区；Index是暂存区；Commit是存档

rebase
merge
reset
cherry-pick
pull
force push

## 字节内部的Git手册

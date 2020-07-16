### 创建版本库

---

找一个非中文目录，进入`git bash`

---

创建版本库.git

```git
git init
```

---

### 文件修改与提交（以下操作均在本地）

---

```
git add filename(.表示所有修改文件)
```

此阶段表示将文件的修改提交到了暂存区

```
git commit -m "explanations"
```

此阶段表示将暂存区所有的文件修改提交到.git保存的版本库当中，作为了最新版本。



### 版本回退

---

```
git log (--pretty==oneline)
```

可以知道提交记录，如果从未来返回，则看不到未来的记录.

`--pretty==oneline`将每条操作指令压缩成一行，显著提高清晰度。

```
git reflog
```

可以查看整个库的所有提交记录

查看提交记录的目的在于想要查看每次提交的注释、提交编号以便回退

```
git reset --hard 版本号
```

回退到版本号对应的操作时的版本

#### 补充：版本号的HEAD代替

HEAD指log调用后的第一个版本，HEAD^表示第二个，HEAD~100表示第100个，其可以用HEAD来代替版本号进行回退。



### 查看状态

---

```
git status
```

可以查看当前暂存区和版本库的状态，以便决定下一步操作。



### 撤销修改

---

##### 情况1：不小心改错了，但还没有add

```
get restore filename
```

将文件恢复到上一次的commit版本

##### 情况2：add之后，不小心进行了改动

```
get restore filename
```

将文件恢复到上一次的add版本

##### 情况3：不小心改错了，而且已经add了

```
get reset HEAD filename
```

将暂存区的文件撤回到工作区。



### 删除文件

---

##### 情况1：想删除库里文件

```
git rm filename
git commit -m "xxx"
```

即可删除库里的文件且工作区的相应文件也消失。

或者先手动删除工作区文件，然后使用

```
git rm/add filename
git commit -m "xxx"
```

即可将删除同步到库当中

---

##### 情况2：不小心手动删除了工作区的，但好像删错了

```
git restore filename
```

即可将库里filename的同名文件恢复到工作区。



### 远程库关联+远程库交互

---

将本地库与远程库进行关联：

```
git remote add origin 库网址:https://……
```

origin默认为远程库的库名

##### 从远程库更新下载本地库

```
git pull origin master
```

##### 从本地库更新提交远程库

```
git push origin master
```



### 直接克隆远程库至本地

---

可以不用git init，直接把远程库来一份在本地

```
git clone 库网址
```

可以在当前文件夹自动创建一个和库名字相同的文件夹装克隆库的信息。



### GIT库分支操作

---

每个分支有自己的版本库。

#### 创建并跳转到分支（当前分支可在命令行末尾看到）

```
git switch -c name
```

![](C:\Users\dell\AppData\Roaming\Typora\typora-user-images\image-20200715220337298.png)

---

#### 分支跳转

当某一个分支的文件没有修改且未提交、暂存区还有文件的情况下，可以跳转到其他分支。

```
git switch target
```

而如果当前分支有修改但没提交，或者暂存区还有文件没有commit,却想跳转时

```
git stash
```

将当前的全部工作状态缓存，跳转之后完成工作后，又想回来恢复

```
git stash list
```

查看stash中的所有缓存状态，使用

```
git stash apply （缓存编号）
git stash drop
```

将恢复List顶端的第一个缓存状态，但并不会删除该状态，而drop则会删除最顶端状态。

如果加了缓存编号则恢复相应的状态。

```
git stash apply + git stash drop == git stash pop
```

**所以不妨将分支状态的stash当做压栈操作**

---

#### 分支合并

当某一个分支进行了修改，可以将其合并到另外一个分支当中。

```
git merge name
```

可以将name分支合并到当前分支，但不会在Log, reflog当中留下任何信息。

如果想要保留合并信息，则需要使用如下语句

```
git merge --no-ff -m "xxx" name
```

表明将合并操作记录，且添加注释为"xxx"。

---

#### 分支合并冲突

当某一个分支进行了某文件的修改，master进行了另外一个修改，则两个分支的同一文件无法进行合并，将会报错，此时需要先merge，之后再次add并提交将完成正确合并。

---

#### 分支删除

当某个分支没有进行任何对master分支的修改，或者修改之后全部已经完成合并，则

```
git branch -d name
```

进行删除，注意：name不能是当前分支的名字！

但如果某个分支还有未合并的内容，则使用-d进行合并将出现错误，则

```
git branch -D name
```

进行强制删除即可，记得当前的合并应为已经不需要的修改。

---

#### 查看分支

```
git branch
```

查看当前已有分支，当前分支前有*





### GIT标签管理

时常会觉得从乱七八糟的编号去找一个版本的库也太痛苦了……,还好有标签帮忙

---

#### 创建标签

```
git tag name (编号)
```

如果不加编号，则是为当前分支的当前版本标注了tag

如果加入了编号，则是为编号库标注了tag

当然，还可以添加有说明的标签

```
git tag -a name -m "xxx" (编号)
```

---

#### 查看已有标签

```
git tag
```

只能告诉你有哪几个标签

---

#### 查看相应标签的版本信息

```
git show tag
```

可以查看对应版本库的信息，比如作者、注释、标签说明等等。

---

#### 删除标签

```
git tag -d name
```

**从此所有使用编号的地方，都可以用相应的标签去代表，十分方便。**



### GIT自定义命令设置

```
git config --global alias.newname rowcommand
```

如果rowcommand是好几个单词，则加上单引号。

注意：row command为git后面的命令，newname不要覆盖。
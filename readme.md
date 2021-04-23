# "知疫"疫情可视化平台

以yzm分支为例进行说明

- 开发之前

  从远程仓库拉取最新的代码，然后`merge`到个人分支，流程如下：

  ```
  git checkout master    #切换到master分支
  git pull       #拉取最新代码
  git checkout yzm    #切换到个人分支
  git merge master           #同步代码到个人分支
  ```

- 接下来就能愉快开发啦

- 开发告一段落

在各分支完成独立内容并确保内容无误之后，希望将它合并主分支，以保持主分支永远是最新版本时，可以使用git merge命令操作：

以yzm分支为例，一般情况下，命令如下：

```
git checkout yzm    #切换到自己的分支
git add --all       #--all 添加所有文件，也可以换成其他参数
git commit -m "the info"    #提交
git push origin yzm   #上传到对应远程分支
git checkout master  #切换到master主分支
git merge yzm           #使用git merge命令把yzm分支合并过来
git push origin master  #上传到远程分支master
```

若上传失败，可能是在上传过程中远程分支master已经被修改，需要重新git pull 远程主分支，再进行上述操作。



##### 希望大家开发愉快！

##### 没有bug!!!




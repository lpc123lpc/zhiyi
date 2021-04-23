# "知疫"疫情可视化平台

## git分支合并

在各分支完成独立内容并确保内容无误之后，希望将它合并主分支，以保持主分支永远是最新版本时，

可以使用`git merge`命令操作：

以`yzm`分支为例，**一般情况下**，命令如下：

```cmd
git checkout yzm    #切换到自己的分支
git add --all 		#--all 添加所有文件，也可以换成其他参数
git commit -m "the info"    #提交
git push origin yzm   #上传到对应远程分支
git checkout master  #切换到master主分支
git merge yzm			#使用git merge命令把yzm分支合并过来
git push origin master  #上传到远程分支master
```

若上传失败，可能是在上传过程中远程分支master已经被修改，需要重新git pull 远程主分支，再进行上述操作。









希望大家开发愉快！

没有bug!!!




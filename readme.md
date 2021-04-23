# "知疫"疫情可视化平台

## git分支合并

在各分支完成独立内容并确保内容无误之后，希望将它合并主分支，以保持主分支永远是最新版本时，

可以使用`git merge`命令操作：

以`yzm`分支为例，**一般情况下**，命令如下：

```cmd
git checkout yzm
git add --all 
git commit -m "the info"
git push origin yzm
git checkout master
git merge yzm
git push origin master
```





希望大家开发愉快！

没有bug!!!




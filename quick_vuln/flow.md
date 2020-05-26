```flow
start=>start: Start
end=>end: End
op=>operation: My Operation
sub=>subroutine: My Subroutine
cond=>condition: Yes or No?
io=>inputoutput: catch something...
start->op->cond
cond(yes)->io->end
cond(no)->sub(right)->op
```

```flow
start=>start: 确定漏洞环境
cond_vulrange=>condition: 靶场是否有相关环境？
cond_dockerhub=>condition: Docker Hub 是否有相关环境？
cond_fofa=>condition: FOFA 能否搜索到相关环境？
cond_build=>condition: 本地能否搭建成功？
fail=>end: 获取漏洞环境失败
success=>end: 获取漏洞环境成功
start->cond_vulrange(no)->cond_dockerhub(no)->cond_fofa(no)->cond_build(no)->fail
cond_vulrange(yes)->success
cond_dockerhub(yes)->success
cond_fofa(yes)->success
cond_build(yes)->success
```




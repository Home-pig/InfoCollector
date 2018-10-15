# InfoCollector
<br/>
本工具用于对网站信息收集，对于脚本和网站查询结果进行合成，最后形成一个查询文件

# 已支持查询工具
- [subDomainsBrute](https://github.com/lijiejie/subDomainsBrute)

# 支持查询网站
- [w3tchs](https://w3techs.com/sites)
- [whatWeb](https://www.whatweb.net/)
- [yunSee资产](http://www.yunsee.cn/info.html)

# 目录结构
```
infoCollector.py文件入口
chooser.json文件对是否执行功能进行控制，也可以用户自定义调用工具的参数
action:功能点
codeDemo:模板
config:配置文件
depend:其他工具下载存放位置
lib:程序用到的一些函数
output:输出内容
```

# 程序流程：
infoCollector入口-->查看同级目录的chooser.json-->获取action中可以调用的大模块-->进入模块中，查看chooser.json可以调用的功能-->调用功能

# 改进
- 多线程
- 增加功能
- 异常处理

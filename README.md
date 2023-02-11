# net_elder
一个在网上瞎转，没有具体目标的pyhton爬虫；用来探索世界上到底有多少奇奇怪怪的网站~

项目的灵感已经太过久远不可考了，可能是想捡起来荒废已久的python、或者是想尝试一下spring以外的框架写起来是甚么感觉、也可能是冲浪到了什么奇怪的网站想要探索更多互联网角落吧~
## 功能
从一个网页出发，遇到这个网页中指向其他网站的链接就点进去并将网页信息（title，description之类）存进数据库，就这样漫无目的的在互联网上乱逛
## 实现
这个爬虫本身仍然逃不脱所谓的*爬虫循环*：
1. 通过给定的URL生成一个初始request，并指定一个用于处理response的回调函数
2. 在回调函数中拆分response（网页）并返回[ref]可以使用yield关键字实现多个返回，scrapy会自动判断返回值类型，如果是request则加入待请求队列，如果是item则加入pipeline[/ref]：
	a. scrapy中定义的item ~~我看就是一个dict~~ 
	b. 一个类似步骤一中的指定回调的request；scrapy会继续发送这个request并交由回调处理 （net_elder 实现互联网上遛弯的核心，~~DFS遍整个互联网~~）
3. 在回调函数中使用scrapy提供的CSS选择器将目标数据提取出来并组合成item；在这个项目中只需要提取标签a相关的信息即可
4. 最后通过ItemPipLine将item信息持久化进数据库即可


![file](https://tars-knock.cn/wp-content/uploads/2023/01/image-1675433819525.png)

更多相关信息可[点击跳转到我的博客](https://tars-knock.cn/archives/263)了解~

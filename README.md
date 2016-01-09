#CSUAcademicSpider
This is a spider basd on [Scrapy](https://github.com/scrapy/scrapy) to crawl some academic informations from  academies' offical websites.
##Academic Item Definition
- url:爬取页面地址
- title:讲座标题
- time:实际举办时间
- date_sort:处理后的用于排序的日期时间
- location:举办地点
- location_id:匹配地点 id（处理经纬度及地图标注）　
- academy:学院名
- type:讲座类型
- html_content:实际html代码，用于移动端显示

##Location List

##Create Table SQL
###academic
###location
###jobs

##Academies list
###单页型
- [信息院](http://sise.csu.edu.cn/index/xsbg.htm)
- [物理院](http://wl.csu.edu.cn/Firspage.aspx?strid=a88f17dd-f1ad-4148-90ce-8e22a464197a&id=20)
- [机电工程学院](http://cmee.csu.edu.cn/Content.aspx?moduleid=deba87c1-a197-4047-82bd-f9d7006418d7&id=7)
- [公共管理学院](http://csuspa.csu.edu.cn/catalog/25/index_1.htm)
- [数学与统计学院](http://math.csu.edu.cn/lb.jsp?urltype=tree.TreeTempUrl&wbtreeid=1217)
- [粉末冶金研究院](http://pmri.csu.edu.cn/News/DefaultNews.aspx?NewsTypeID=120130) keywords:【预告】  
- [土木工程学院](http://civil.csu.edu.cn/Content.aspx?moduleid=0104&id=8)
- [冶金与环境学院](http://smse.csu.edu.cn/Firspage.aspx?strId=8d553b06-83bd-4273-9942-477ab75616c9&id=0)
- [公共卫生学院](http://sph.csu.edu.cn/info/1031/2224.htm)
- [药学院](http://yxy.csu.edu.cn/index/xshd.htm)  features:图片 PDF 文字混杂  


###混杂型  
- [文学院](http://wxy.csu.edu.cn/index/xygg.htm)
- [商学院](http://bs.csu.edu.cn/plus/list.php?tid=15) keyword:经管大讲堂第XX期  [英文版]( http://bse.csu.edu.cn/seminars/) 
- [法学院](http://law.csu.edu.cn/Secondarypage.aspx?moduleid=0501&id=0) 动态页面 【名家讲坛】图片形式 【讲座预告】
- [化工学院](http://ccce.csu.edu.cn/index.html)  左侧中部 【学术讲座】
- [资源与安全工程学院](http://srse.csu.edu.cn/channels/596.html) 【学术】
- [生命科学学院](http://life.csu.edu.cn/index.php/category/%E9%80%9A%E7%9F%A5%E5%85%AC%E5%91%8A/) 【学术】
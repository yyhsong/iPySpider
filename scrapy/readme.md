# Scrapy爬虫框架

Scrapy是一个支持高并发的网络爬虫框架

## 框架结构 - 5+2结构

5个模块
- Spiders 
    - 框架入口，提供初始的爬取请求，用户编写（配置）
    - 解析Downloader返回的响应
    - 产生爬取项
    - 产生额外的爬取请求
- Engine 
    - 已有实现
    - 控制各模块之间的数据流
    - 根据条件触发事件
    - 不间断从Scheduler处获得爬取请求，直至请求为空
- Scheduler 
    - 已有实现
    - 对所有爬虫请求进行调度管理
- Downloader 
    - 已有实现
    - 根据请求下载页面
- Item pipelines 
    - 框架出口，用户编写（配置）
    - 以流水线方式处理Spider产生的爬取项
    - 由一组操作顺序组成，类似流水线，每个操作是一个Item Pipeline类型
    - 清理、检验和查重爬取项中的HTML数据，将数据存储到数据库

2个中间件
- Spiders和Engine之间
    - 对请求和爬取项的再处理
    - 修改、丢弃、新增请求或爬取项
    - 用户可以编写配置代码
- Downloader和Engine之间
    - 实施Engine、Scheduler和Downloader之间进行用户可配置的控制
    - 修改、丢弃、新增请求或响应
    - 用户可以编写配置代码

![Scrapy框架结构](./scrapy_structure.jpg)

## 数据流的三条路径

- 第一条路径
    - Engine从Spiders处获得爬取请求(Request)
    - Engine将爬取请求转发给Scheduler，用于调度
- 第二条路径
    - Engine从Scheduler处获得下一个要爬取的请求
    - Engine将爬取请求通过中间件发送给Downloader
    - 爬取网页后，Downloader形成响应(Response)，通过中间件发给Engine
    - Engine将收到的响应通过中间件发送给Spider处理
- 第三条路径
    - Spider处理响应后产生爬取项(Scraped Item)和新的爬取请求给Engine
    - Engine将爬取项发送给Item Pipeline
    - Engine将爬取请求发送给Scheduler

## 与requests库的比较

相同点
- 都可以进行对页面的请求和爬取，是Python爬虫的两条常用技术路线
- 都没有处理js、提交表单、应对验证码等功能（可扩展）

不同点

| requests | Scrapy |
| --- | --- |
| 功能库 | 框架 |
| 页面级爬虫 | 网站级爬虫 |
| 重点在于页面下载 | 重点在于爬虫结构 |
| 并发考虑不足，性能较差 | 并发较好，性能较高 |
| 定制灵活 | 一般定制灵活，深度定制困难 |

## Scrapy框架的使用步骤

1. 创建一个工程
2. 创建Spider模板
3. 编写Spider
4. 编写Item Pipeline
5. 优化配置策略

## Scrapy命令

Scrapy采用命令行的方式进行创建项目、生成及启动爬虫等操作

```
# 基本格式
> scrapy <command> [options] [args]

# 常用命令
# Create new project
> scrapy startproject <name> [dir]

# Generate new spider using pre-defined templates
> scrapy genspider [options] <name> [domain]

# Start a spider
> scrapy crawl <name>
```

## Scrapy工程目录

- projectname/             项目外层目录   
    - scrapy.cfg           部署Scrapy爬虫的配置文件
    - projectname/         项目内层目录，存放用户自定义代码
        - __init__.py      初始化文件
        - items.py         Items代码模板（继承类）
        - middlewares.py   Middlewares代码模板（继承类）
        - pipelines.py     Piplines代码模板（继承类）
        - settings.py      Scrapy爬虫的配置文件
        - spiders/         Spiders代码目录
            - __init__.py  初始化文件
            - __pycache__/ 缓存目录
        - __pycache__/     缓存目录

## Scrapy中的数据类型

- scrapy.http.Request类
    表示一个HTTP请求，由Spider生成，由Downloader执行
    主要属性和方法：
    - url 请求的url地址
    - method 请求方式，如GET、POST等
    - headers 请求的头信息，字典类型
    - body 请求的主体内容，字符串类型
    - meta 自定义的扩展信息，可在Scrapy内部模块间传递信息
    - copy() 复制该请求
- scrapy.http.Response类
    表示一个HTTP响应，由Downloader生成，由Spider处理
    主要属性和方法：
    - url Response对应的URL地址
    - status HTTP状态码，成功为200
    - headers 响应的头部信息
    - body 响应的内容信息，字符串类型
    - flags 一组标记
    - request 本次响应对应的Request类
    - copy() 复制该响应
- scrapy.item.Item类
    表示一个从HTML中提取的信息内容
    由Spider生成，由Item Pipeline处理
    类字典类型，可以当作字典类型进行处理

## Scrapy支持多种信息提取方式

- beautifulsoup
- lxml
- re
- XPath Selector
- CSS Selector













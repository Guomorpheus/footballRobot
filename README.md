# Football Robot via Python, AIML and Neo4J

## 背景

最近学习了Neo4J图数据库的相关知识，Neo4j是一个高性能的,NOSQL图形数据库，它将结构化数据存储在网络上而不是表中。Neo4j也可以被看作是一个高性能的图引擎，该引擎具有成熟数据库的所有特性。程序员工作在一个面向对象的、灵活的网络结构下而不是严格、静态的表中——但是他们可以享受到具备完全的事务特性、企业级的数据库的所有好处。Neo4j因其嵌入式、高性能、轻量级等优势，越来越受到关注。

从前，研究人员把RDF/OWL数据存储在Virtuoso或者Fuseki等RDF数据库，但是随着Neo4J的出现，将知识图谱存储在Neo4J成了除了RDF数据库外另外一种选择性，给知识图谱的存储提出了一个新的思路，利用图数据库来存储本体相关知识。

此文将利用Neo4j存储了英超联赛的测试数据，并且使用neo2py库使用python对英超知识图谱经行查询，并且配合AIML打造一个自动问答系统。



## 环境

**Neo4j : 3.3.7**

**Python : 3.X**

**python-aiml : 0.9.1**

**neo2py : 4.1.0**

**IDE : Pycharm**



## 如何搭建自动问答系统

### python虚拟环境

项目中，使用虚拟环境让项目独立运行，并且使用pip安装上文中所提到的各种包。

如何启动虚拟环境:

```

```



### 创建Aiml机器人

```python
1.fRobot = aiml.Kernel()
2.fRobot.learn("startup.xml")
3.fRobot.respond('LOAD FTR')
```

详解：

1: 启动aiml机器人的核心代码，并且赋值给fRobort

2: startup.xml 是 初始化入口，此XML文件里主要是机器人启动的指令，并且告诉机器人要学习哪些知识库。

3: 告诉程序，启动机器人。

### 连接Neo4J图数据库

自动机器人已经初始化完毕，现在需要通过机器人的回调，使用python去访问Neo4j图数据库的数据。

```python
#Neo4j图数据库检索
def footballQuery(input):
    #连接数据库
    footballGraph = Graph("http:localhost:7474",username="neo4j",password="111111")
    #查找节点
    if input == 'football club':
        result = footballGraph.run("MATCH (n:football_club) RETURN n ")
    else:
        result1 = footballGraph.run("MATCH (n:football_club{name:\""+input+"\"}) RETURN n ")
        result = result1.data()
    return result
```

以上的函数包含了数据库的连接，已经CQL数据的查询，由于时间关系，这个程序仅仅是示例，并没有过于复杂的数据。

### 结果

```
Loading startup.xml...done (0.00 seconds)
Loading redirection.aiml...done (0.00 seconds)
Loading ai.aiml...done (0.02 seconds)
Loading tuling.aiml...done (0.85 seconds)
Loading basic_chat.aiml...done (0.00 seconds)
Enter your message>> 哈哈哈
FRobot:嘿嘿，心情还不错
Enter your message>> 你好啊
FRobot:您好，是，有什么可以帮您的吗？
Enter your message>> 曼联 kg
[{'n': (_0:football_club {image: 'manu.png', name: '\u66fc\u8054'})}]
```


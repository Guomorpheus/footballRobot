# -*- coding utf-8 -*-
import aiml
import sys
import os
from py2neo import Graph, Node, Relationship

#得到模块路径
def getModuleDir(name):
    path = getattr(sys.modules[name], '__file__', None)
    if not path:
        raise AttributeError('module %s has not attribute __file__' % name)
    return os.path.dirname(os.path.abspath(path))

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

if __name__ == '__main__':
    alicePath = getModuleDir('aiml') + '\\botdata\\alice'
    # 切换到语料库所在工作目录
    os.chdir(alicePath)
    fRobot = aiml.Kernel()
    fRobot.learn("startup.xml")
    fRobot.respond('LOAD FTR')
    #print(alicePath)
    while True:
        inputMessage = input("Enter your message>> ")
        if len(inputMessage) > 60:
            print(fRobot.respond("input is too long > 60"))
            continue
        elif inputMessage.strip() == '':
            print(fRobot.respond('空'))
            continue

        if inputMessage == 'q':
            exit()
        else:
            response = fRobot.respond(inputMessage)
            if response == "":
                ans = fRobot.respond("找不到答案")
                print(ans)
            #通过neo4j查询
            elif response[0] == '#':
                if response.__contains__("neo4j"):
                    res = response.split(':')
                    entity = str(res[1].replace(" ",""))
                    ans = footballQuery(entity)
                    print(ans)
                #匹配不到模版，通用查询
                elif response.__contains__("NoMatchingTemplate"):
                    print("没有发现匹配项")
                    print("没搜索到，此功能暂不支持")
                #多答案
                if len(ans) == 0:
                    ans = fRobot.respond("找不到答案")
                    print('FRobot:' + ans)
                elif len(ans) > 1 and type(ans) == list:
                    print("不确定候选答案")
                    print('FRobot:')
                    for a in ans:
                        print(a)
                else:
                    print('FRobot:' + ans)
            else:
                print("FRobot:" + response)


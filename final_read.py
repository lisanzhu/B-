import copy
import xml.sax
import linecache
import os
import pickle
import sys
from bisect import bisect_right, bisect_left
from collections import deque
import xml.sax
import string
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication

sys.setrecursionlimit(1000000000)


class has_find_Exception(Exception):
    pass


class InitError(Exception):
    pass


class Bptree(object):
    # 定义内部结点类，内部结点的数据包括该树的阶数M，确定存放区间，已存放的索引
    class InterNode(object):

        def __init__(self, M):
            self.__M = M

            self.clist = []  # 存放区间

            self.ilist = []  # 存放索引/序号

            self.par = None  # 父节点

        # 判断结点是否是叶子
        def isleaf(self):
            return False

        # 判断该结点是否以及存放满
        def isfull(self):
            return len(self.ilist) >= self.M - 1

        # 判断该结点是否是空的
        def isempty(self):
            return len(self.ilist) <= (self.M + 1) / 2 - 1

        @property
        # 返回阶数M
        def M(self):
            return self.__M

    # 叶子
    class Leaf(object):
        # 叶子初始化，确定
        def __init__(self, L):
            # 叶子可存放的最大的数量
            self.__L = L
            # 叶子中已经存放的数据
            self.vlist = []

            self.bro = None  # 兄弟结点

            self.par = None  # 父结点

        # 判断是否叶子
        def isleaf(self):
            return True

        # 判断叶子存放的数据是否已满
        def isfull(self):
            return len(self.vlist) > self.L

        # 判断叶子是否是空的
        def isempty(self):
            return len(self.vlist) <= (self.L + 1) / 2

        @property
        # 返回叶子中数据的数量
        def L(self):
            return self.__L

    # 初始化
    # 这里是B+树的大类的初始化
    def __init__(self, M, L):
        # 这里是要确定B+树的叶子结点都包含L个元素，而且必须保证M/2<L<M
        if L > M:
            print(1)
            # raise InitError('L must be less or equal then M')

        else:

            self.__M = M

            self.__L = L

            self.__root = Bptree.Leaf(L)

            self.__leaf = self.__root

    @property
    # 该函数返回B+数的阶数
    def M(self):

        return self.__M

    @property
    # 返回叶子最大的存放元素的数量
    def L(self):

        return self.__L

    # 插入
    def insert(self, key_value):
        # 取当前插入的树的根
        node = self.__root

        # 这里是插入元素之后如果存放满了，元素上升到结点的位置，对结点进行处理
        def split_node(n1):

            mid = self.M // 2  # 此处注意，可能出错

            newnode = Bptree.InterNode(self.M)
            # 这里的mid是用来保证如果n1已经存放的数据个数大于M/2,则把该结点分裂，将这个节点中间往右所有的元素拿出并建立一个新的节点
            newnode.ilist = n1.ilist[mid:]

            newnode.clist = n1.clist[mid:]

            newnode.par = n1.par
            # 此时newnode和n1已经成为兄弟结点，两者是同一个父亲
            for c in newnode.clist:
                c.par = newnode
            # n1的父亲是空的情况
            if n1.par is None:
                # 没有父(这里意思是没有根结点)节点则新建一个根结点
                newroot = Bptree.InterNode(self.M)
                # 此时父节点的元素存放的是n1的存放元素中的最后一个(也就是最大的那一个)
                newroot.ilist = [n1.ilist[mid - 1]]
                # 确定父节点的范围(范围就是n1和newnode所有的元素)
                newroot.clist = [n1, newnode]
                # n1和newnode拥有共同的父节点,即newroot
                n1.par = newnode.par = newroot

                self.__root = newroot
            # n1的父节点是非空的情况
            else:
                # 以下为结点分裂之后把左孩子的最后一个元素存入其父节点的存储数组中
                i = n1.par.clist.index(n1)

                n1.par.ilist.insert(i, n1.ilist[mid - 1])

                n1.par.clist.insert(i + 1, newnode)
            # 与上面的newnode的存放元素对应,共同存放已经存储的元素
            n1.ilist = n1.ilist[:mid - 1]

            n1.clist = n1.clist[:mid]

            return n1.par

        # 这里是插入元素之后对叶子分裂的情况进行处理
        def split_leaf(n2):

            mid = (self.L + 1) // 2

            newleaf = Bptree.Leaf(self.L)

            newleaf.vlist = n2.vlist[mid:]

            if n2.par == None:

                newroot = Bptree.InterNode(self.M)

                newroot.ilist = [n2.vlist[mid].key]

                newroot.clist = [n2, newleaf]

                n2.par = newleaf.par = newroot

                self.__root = newroot

            else:

                i = n2.par.clist.index(n2)

                n2.par.ilist.insert(i, n2.vlist[mid].key)

                n2.par.clist.insert(i + 1, newleaf)

                newleaf.par = n2.par

            n2.vlist = n2.vlist[:mid]

            n2.bro = newleaf

        def insert_node(n):
            # 如果n不是叶子
            if not n.isleaf():
                # 如果n满了，就把结点n分裂，利用上面写的结点分裂函数
                if n.isfull():

                    insert_node(split_node(n))
                # 如果n没满，就把key_value将在ilist中的位置赋值给p，然后将其插入结点
                else:

                    p = bisect_right(n.ilist, key_value)

                    insert_node(n.clist[p])
            # 如果n是叶子就把key_value将在叶子中vlist中的位置赋值给p，然后将真正地其插入vlist中
            else:

                p = bisect_right(n.vlist, key_value)

                n.vlist.insert(p, key_value)
                # 如果叶子满了就将其分裂，否则插入完就退出
                if n.isfull():

                    split_leaf(n)

                else:

                    return

        insert_node(node)

    # 搜索
    # 范围搜索，搜索mi到ma范围内的键，若mi为空，则进行右查找，若ma为空，则进行左查找
    def search(self, mi=None, ma=None):

        result = []

        node = self.__root

        leaf = self.__leaf

        def search_key(n, k):
            # 如果n已经是叶子,则直接从叶子中寻找k在叶子中的位置
            if n.isleaf():

                p = bisect_left(n.vlist, k)

                return (p, n)
            # 如果n不是叶子，则从结点的子节点中找
            else:
                p = bisect_right(n.ilist, k)
                return search_key(n.clist[p], k)

        # 如果mi是空的，下列代码表示从所有叶子结点中寻找小于ma的key，直至全部被找出来
        if mi is None:
            while True:
                for kv in leaf.vlist:
                    if kv <= ma:
                        result.append(kv)
                    else:
                        return result
                if leaf.bro == None:
                    return result
                else:
                    leaf = leaf.bro
        # 否则，如果ma是空的，mi不是空的，则从等于mi的那个下标开始添加，把所有大于mi的元素添加
        elif ma is None:
            # 表示寻找等于mi的index
            index, leaf = search_key(node, mi)
            result.extend(leaf.vlist[index:])
            while True:
                if leaf.bro == None:
                    return result
                else:
                    leaf = leaf.bro
                    result.extend(leaf.vlist)
        # mi和ma均赋值的情况
        else:
            # mi==ma时
            if mi == ma:
                i, l = search_key(node, mi)
                try:
                    # 只寻找等于mi的那个值
                    if l.vlist[i] == mi:
                        result.append(l.vlist[i])
                        return result
                    else:
                        return result
                except IndexError:
                    return result
            # mi和ma均存在，且mi<ma
            else:
                # 以下过程飙车用i1存储mi的下标，用i2存储ma的下标
                i1, l1 = search_key(node, mi)
                i2, l2 = search_key(node, ma)
                if l1 is l2:
                    if i1 == i2:
                        return result
                    else:
                        result.extend(l2.vlist[i1:i2])
                        return result
                else:
                    result.extend(l1.vlist[i1:])
                    l = l1
                    while True:
                        if l.bro == l2:
                            result.extend(l2.vlist[:i2])
                            return result
                        elif l.bro != None:
                            result.extend(l.bro.vlist)
                            l = l.bro
                        else:
                            return result

    # 遍历叶子的所有存储的元素
    def traversal(self):
        result = []
        l = self.__leaf
        while True:
            result.extend(l.vlist)
            if l.bro == None:
                return result
            else:
                l = l.bro

    # 输出所有叶子中的键和值
    def show(self):
        print('this b+tree is:\n')
        q = deque()
        h = 0
        q.append([self.__root, h])
        while True:
            try:
                w, hei = q.popleft()
            except IndexError:
                return
            else:
                # 如果此时结点不是叶子，则每过一个循环加一层(表示第hei层结点)
                if not w.isleaf():
                    print(w.ilist, 'the height is', hei)
                    if hei == h:
                        h += 1
                    q.extend([[i, h] for i in w.clist])
                else:
                    print([(v.key, v.value) for v in w.vlist], 'the leaf is ', hei)


# 生成键值对

class KeyValue(object):

    def __init__(self, key, value):
        self.__slots__ = ('key', 'value')

        self.key = key  # 一定要保证键值是整型

        self.value = value

    def __str__(self):

        return str((self.key, self.value))

    # 比较当前的Key和输入的key
    def __cmp__(self, key):

        if self.key > key:

            return 1

        elif self.key < key:

            return -1

        else:

            return 0

    # 比较的结果   小于
    def __lt__(self, other):

        if (type(self) == type(other)):

            return self.key < other.key

        else:

            return self.key < other

    # 等于
    def __eq__(self, other):

        if (type(self) == type(other)):

            return self.key == other.key

        else:

            return self.key == other

    # 大于
    def __gt__(self, other):

        return not self < other


def getContent(lis):  # 通过获取XML文件中行数之后进行信息获取

    class Read(xml.sax.ContentHandler):
        # 静态变量

        def __init__(self):

            self.n = 0  # 文本格式化之后，确定文章第几个
            self.target = []
            self.now = []
            self.attr = {}
            self.size = 0
            self.res = {}
            # 存放首字母

            self.numA = 0
            self.numH = 0

            self.author_dic = {}  # 建立作者名为索引时将其所有的放入到一个字典之中，直到最后读取至dblp时将其插入到B+树中
            self.title_list = []
            self.CurrentData = ""
            # 与article同级的标签，代表文章的开始
            self.article_level_tag = ["article", "book", "proceedings", "inproceedings", "www", "mastersthesis",
                                      "incollection", "phdthesis"]
            # 用于存放文章信息的字典
            self.dic = {}

            # 用于存放作者论文数的字典
            self.author = {}
            self.name_string = ""  # 存放拼接的作者名字符串
            self.title_siring = ""  # 存放拼接的标题字符串
            self.hot_word = {}  # 存放各年份的高频词
            self.ignore = {'For', 'for', 'And', 'and', 'On', 'on', 'the', 'The', 'a', 'A', 'Of', 'of', 'With', 'with',
                           'An',
                           'an', 'In', 'in', 'At', 'at', 'Have', 'have', 'Is', 'is', 'Are', 'are', 'Has', 'has', 'Not',
                           'not', 'By', 'by', 'Into', 'into', 'Through', 'through', 'Off', 'off', 'Out',
                           'out'}  # 忽视掉的热点词

        # 元素开始调用
        def startElement(self, tag, attributes):
            self.CurrentData = tag

            if tag in self.article_level_tag:  # 判断该标签是否为文章或与其同等级的开头
                self.n = self.n + 1

                if len(self.target) == len(self.now):
                    raise has_find_Exception
                self.CurrentData = tag

                if self.n in self.target:
                    self.now.append(self.n)
                    self.dic.clear()
                    self.dic['type'] = tag
                    mdate = attributes["mdate"]
                    key = attributes["key"]
                    self.dic["mdate"] = mdate
                    self.dic["key"] = key

        # 元素结束调用
        def endElement(self, tag):
            # if tag in self.article_level_tag:  # 如果标签在和article同一个标签之下

            if self.n in self.target:
                if tag in self.article_level_tag:  # 如果标签在和article同一个标签之下
                    self.res[self.n] = copy.deepcopy(self.dic)
                if tag == "author":  # 把拼接完的作者名记录到字典中
                    if self.name_string not in self.author:  # 记录作者写的文章数
                        self.author[self.name_string] = 1
                    else:
                        self.author[self.name_string] = self.author[self.name_string] + 1
                    if "author" not in self.dic:
                        self.dic["author"] = [self.name_string]
                        self.name_string = ""
                    else:
                        self.dic["author"].append(self.name_string)
                        self.name_string = ""
                elif tag == "title":  # 把拼接完的标题名记录到字典中
                    if "title" not in self.dic:
                        self.dic["title"] = [self.title_siring]
                        self.title_siring = ""
                    else:
                        self.dic["author"].append(self.title_siring)
                        self.title_siring = ""
                self.CurrentData = ""

        # 读取字符时调用
        def characters(self, content):
            if self.n in self.target:
                # print(1)
                # print(content)
                # print(2)
                # print(self.CurrentData)
                # print(3)
                if self.CurrentData not in self.article_level_tag:
                    if content != '\n':

                        if self.CurrentData:

                            if self.CurrentData == "author":
                                self.name_string = self.name_string + content

                            elif self.CurrentData == "title":
                                self.title_siring = self.title_siring + content
                            else:
                                # 上面两个if条件式是为了防止某个未知BUG的发生
                                if self.CurrentData not in self.dic:
                                    self.dic[self.CurrentData] = [content]
                                else:
                                    self.dic[self.CurrentData].append(content)

    # 创建一个 XMLReader
    parser = xml.sax.make_parser()
    # 关闭命名空间
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写 ContextHandler

    r = Read()
    parser.setContentHandler(r)
    r.target = lis
    try:
        parser.parse("./dblp.xml")
    except has_find_Exception:
        pass

    return r.res




from math import tanh
from sqlite3 import dbapi2 as sqlite

class searchnet:
    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    def maketables(self):
        # 创建代表隐藏层的表
        self.con.execute('create table hiddennode(create_key)')
        # 创建反映网络节点连接状况的表（单词到隐藏层）
        self.con.execute('create table wordhidden(fromid, toid, strength)')
        # 创建反映网络节点连接状况的表（隐藏层到输出层）
        self.con.execute('create table hiddenurl(fromid, toid, strength)')
        self.con.commit()


    # 判断当前连接的强度，如果返回为空，单词层到隐藏层的默认值设为-0.2，对于隐藏层到URL的默认值为0
    def getstrength(self, fromid, toid, layer):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.con.execute('select strength from %s where fromid=%d and toid=%d' % (table, fromid, toid)).fetchone()
        if res == None:
            if layer == 0:
                return -0.2
            if layer == 1:
                return 0
        return res[0]



    # 用以判断连接是否已存在，并利新的强度值更新连接或创建连接
    def setstrength(self, fromid, toid, layer, strength):
        if layer == 0:
            table = 'wordhidden'
        else:
            table = 'hiddenurl'
        res = self.con.execute('select strength from %s where fromid=%d and toid=%d' % (table, fromid, toid)).fetchone()
        if res == None:
            self.con.execute('insert into %s (fromid,toid,strength) values (%d,%d,%f)' % (table, fromid, toid, strength))
        else:
            rowid = res[0]
            self.con.execute('update %s set strength=%f where rowid=%d' % (table, strength, rowid))


    def generatehiddennode(self, wordids, urls):
        if len(wordids)>3:
            return None
        # 检查是否已经为这组单词建好了一个节点
        createkey='_'.join(sorted([str(wi) for wi in wordids]))
        res = self.con.execute(
            "select rowid from hiddennode where create_key='%s'" % createkey).fetchone()

        # 如果没有，则建立
        if res == None:
            cur = self.con.execute(
                "insert into hiddennode (create_key) values ('%s')" % createkey)
            hiddenid = cur.lastrowid

            # 设置默认权重
            for wordid in wordids:
                self.setstrength(wordid, hiddenid, 0, 1.0/len(wordids))
            for urlid in urls:
                self.setstrength(hiddenid, urlid, 1, 0.1)
            self.con.commit()






















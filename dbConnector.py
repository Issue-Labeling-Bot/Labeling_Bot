import pymysql

class DBConnector:
    def __init__(self):
        self.server_ip = '203.255.57.108'
        self.server_port = 3306
        self.user = 'root'
        self.pw = '1234'
        self.db = 'test'

    def _base(self, func):
        conn = pymysql.connect(host=self.server_ip, port=self.server_port,\
            user=self.user, password=self.pw, db=self.db, charset='utf8')
        cur = conn.cursor()

        res = func(cur)

        conn.commit()
        conn.close()
        return res

    def storeRepositoryInformation(self, data):
        ## data = [[repository, access_token, labels], [repository, access_token, labels], ...]
        table = 'repository_information'
        col0, col1, col2 = 'repository', 'access_token', 'labels'
        def store(cur):
            for information in data:
                sql = 'select {} from {} where {}="{}"'.format('*', table, col0, information[0])
                cur.execute(sql)
                res = cur.fetchone()
                if res is None:
                    sql = 'insert into {} ({}, {}, {}) values ("{}", "{}", "{}")'.format(table, col0, col1, col2, information[0], information[1], ','.join(information[2]))
                else:
                    sql = 'update {} set {}="{}", {}="{}" where {}="{}"'.format(table, col1, information[1], col2, ','.join(information[2]), col0, information[0])
                cur.execute(sql)
        self._base(store)

    def storeSelectedLabels(self, data):
        ## data = {repository: [label, label, ...], repository: [label, label, ...], ...}
        table = 'repository_information'
        col0, col3 = 'repository', 'selected_labels'
        def store(cur):
            for repository, labels in data.items():
                sql = 'update {} set {}="{}" where {}="{}"'.format(table, col3, ','.join(labels), col0, repository)
                cur.execute(sql)
        self._base(store)

    def loadAccessToken(self, repository):
        ## repository = full_name
        table = 'repository_information'
        col0, col1 = 'repository', 'access_token'
        def load(cur):
            sql = 'select {} from {} where {}="{}"'.format(col1, table, col0, repository)
            cur.execute(sql)
            access_token = cur.fetchone()[0]
            return access_token
        return self._base(load)

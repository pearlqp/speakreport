# 所有和数据库有关的函数方法
import pymysql
# 定义和数据库的连接
conn = pymysql.connect(
    host="rm-2zeu2bup91le1scnbpo.mysql.rds.aliyuncs.com",
    port=3306,
    user="Phiin_1",
    passwd="439587426Yn",
    db="lgw",
    charset='utf8',
    cursorclass=pymysql.cursors.DictCursor
)

# 根据用户名查询用户是否存在的函数
def query_user_by_username(username):
    sql = "select * from sys_user where username = %s"
    cur = conn.cursor()
    cur.execute(sql, [username])
    result = cur.fetchone()
    return result
    #if result is None:
        #return True
    #else:
        #return False

# 根据用户名和密码添加数据的函数
def add_user(username,password):
    sql = "insert into sys_user (username,password) values (%s,%s)"
    cur = conn.cursor()
    cur.execute(sql, [username,password])
    conn.commit()


# 3、根据用户id查询当前用户的AI助手聊天信息的函数
def query_message_by_user_id(user_id):
    sql = "select * from chat_message where user_id = %s order by message_time asc"
    cur = conn.cursor()
    cur.execute(sql, [user_id])
    # 字典类型的列表[{},{},{}]
    list = cur.fetchall()
    return list

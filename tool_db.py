import pymysql,yaml

def db_Connect():
    try:
        with open('config.yml', 'r') as f:
            result = yaml.load(f, Loader=yaml.FullLoader)
            mysqlresult = result['mysql']
        connect = pymysql.connect(host=mysqlresult['host'], user=mysqlresult['username'], password=int(mysqlresult['password']), db=mysqlresult['database'], port=int(mysqlresult['port']))
        return connect
    except Exception as e:
        print( e )

def getConnect():
        connection = pymysql.connect(host='localhost',
                             user='root',
                             password='237356573',
                             db='devops',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return connection


def selectByParameters( sql, params = None ):
    try:
        connect = getConnect()
        cursor = connect.cursor()
        cursor.execute( sql, params )
        result = cursor.fetchall()
        return result
    except Exception as e:
        print( e )
    finally:
        try:
            cursor.close()
        except Exception as e:
            print(e)
        try:
            connect.close()
        except Exception as e:
            print(e)

def updateByParameters( sql, params = None ):
    try:
        connect = getConnect()
        cursor = connect.cursor()
        count = cursor.execute( sql, params )
        connect.commit()
        return count
    except Exception as e:
        connect.rollback()
        print( e )
    finally:
        try:
            cursor.close()
        except Exception as e:
            print(e)
        try:
            connect.close()
        except Exception as e:
            print(e)

if __name__ == "__main__":
    sql = "delete from servers where id = %s"
    result = updateByParameters(sql, params=( 3, ))
    print( result )

#     db=db_Connect()
#     print (type(db))
#     print (db) 

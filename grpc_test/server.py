import grpc
from concurrent import futures
from grpc_test.proto import hello_pb2, hello_pb2_grpc
import pymysql


class BookStub(hello_pb2_grpc.BookManagerServicer):
    def connect_to_database(self):
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='your password',
            db='your database name',
            charset='utf8',
            autocommit=True,    # 如果插入数据，， 是否自动提交? 和conn.commit()功能一致。
        )
        return conn

    def add(self, request, context):
        conn = self.connect_to_database()
        cursor = conn.cursor()
        ID = request.bookID
        name = request.Name
        try:
            cursor.execute(f"insert into booklist values ({ID},'{name}');")
            conn.commit()
        except Exception as e:
            print(e)
            return hello_pb2.State(IsSuccess=False)
        return hello_pb2.State(IsSuccess=True)

    def queryByID(self, request, context):
        conn = self.connect_to_database()
        cursor = conn.cursor()
        ID = request.bookID
        try:
            cursor.execute(f"select * from booklist where ID='{ID}';")
            mylist = cursor.fetchall()
            name = mylist[0][1]
            cursor.close()
            conn.close()
        except Exception as e:
            return hello_pb2.Book(bookID=ID, Name=f'not found the book')
        return hello_pb2.Book(bookID=ID, Name=f'{name}')

    def queryByName(self, request, context):
        conn = self.connect_to_database()
        cursor = conn.cursor()
        name = request.Bookname
        Booklist = []
        try:
            cursor.execute(f"select * from booklist where name like '{name}';")
            mylist = cursor.fetchall()
            for elem in mylist:
                Booklist.append(hello_pb2.Book(bookID=elem[0], Name=f"{elem[1]}"))
        except Exception as e:
            Book = hello_pb2.Book(bookID=1, Name='not found file')
            return hello_pb2.BookList(list=[Book])
        return hello_pb2.BookList(list=Booklist)

    def delete(self, request, context):
        conn = self.connect_to_database()
        cursor = conn.cursor()
        ID = request.bookID
        try:
            cursor.execute(f"delete from booklist where ID={ID};")
            conn.commit()
        except Exception as e:
            return hello_pb2.State(IsSuccess=False)
        return hello_pb2.State(IsSuccess=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(10))
    hello_pb2_grpc.add_BookManagerServicer_to_server(BookStub(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()

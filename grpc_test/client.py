from grpc_test.proto import hello_pb2, hello_pb2_grpc
import grpc

def help_func():
    print('''if you want to add a book please input add command and other info about book
            eg. add BookID BookName
            if you want to query a book by name please input query_by_name command
            eg. query_by_name BookName
            if you want to query a book by ID please input query_by_ID command
            eg. query_by_ID BookID
            if you want to delete a book by ID please input delete command
            eg. delete BookID
            if you want to quit, just input quit
    ''')


def run():
    with grpc.insecure_channel('localhost:50052') as channel:
        stub = hello_pb2_grpc.BookManagerStub(channel)
        print('welcome to book manager, if you need help,please input help')
        while True:
            cmd = input('please input your command:').split()
            if cmd[0] == 'help':
                help_func()
            elif cmd[0] == 'add' and len(cmd) >= 3:
                print(stub.add(hello_pb2.Book(bookID=int(cmd[1]), Name=cmd[2])))
            elif cmd[0] == 'query_by_name' and len(cmd) >=2:
                print(stub.queryByName(hello_pb2.Bookname(Bookname=cmd[1])))
            elif cmd[0] == 'query_by_ID' and len(cmd) >= 2:
                print(stub.queryByID(hello_pb2.bookID(bookID=int(cmd[1]))))
            elif cmd[0] == 'delete' and len(cmd) >= 2:
                print(stub.delete(hello_pb2.bookID(bookID=int(cmd[1]))))
            elif cmd[0] == 'quit':
                break
            else:
                print('error parameters')


if __name__ == "__main__":
    run()



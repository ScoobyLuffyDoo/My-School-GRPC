import grpc
import myschool_pb2_grpc as pb2_grpc
import myschool_pb2 as pb2
import time 
import threading
threadList =[]
def getStudentDetails(i_studen):
    start_time= time.perf_counter()
    with grpc.insecure_channel('localhost:50051')as channel:
        stub = pb2_grpc.MyStudentsStub(channel)
        reponse = stub.student_details(pb2.Student_ID(student_Id_number=i_studen))
        end_time = time.perf_counter()
        # print(f"Student Call Time : {str(end_time-start_time)}" )
        return reponse
    
def client():
    print("Client has Started and is listining:\n\n")
    while True:
        
        studentnumber = input("What is your Student Number ? \n")
        try:
            start_time= time.perf_counter()
            for i in range(0,1000):
             thread= threading.Thread(target=getStudentDetails,args=(studentnumber,))   
             threadList.append(thread)
            # studentinfo =getStudentDetails(studentnumber)
            # print(studentinfo)
            for thread in threadList:
                thread.start()
            for thread in threadList:
                thread.join()
            # for i in range(0,1000):
            #     studentinfo =getStudentDetails(studentnumber)
            #     # print(studentinfo)
        except Exception as e:
            print (e)
        end_time = time.perf_counter()
        print(f'Main Call Time : {str(end_time-start_time)}' )
client()
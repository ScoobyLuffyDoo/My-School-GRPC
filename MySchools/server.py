from concurrent import futures
from unittest import result
import grpc
import myschool_pb2 as pb2
import myschool_pb2_grpc as pb2_grpc


StudentDb={'SM5017':{'Name':'Scooby1','Surname':'Doo1','DOB':'2020-01-01'},
'SM5018':{'Name':'Scooby2','Surname':'Doo2','DOB':'2020-01-02'},
'SM5019':{'Name':'Scooby3','Surname':'Doo3','DOB':'2020-01-03'},
}
def GetStudentInfo(ID_Number):
    if ID_Number in StudentDb.keys():
        studentInfo={'result':True,
            'name':StudentDb[ID_Number]['Name'],
        'surname':StudentDb[ID_Number]['Surname'],
        'date_of_birth':StudentDb[ID_Number]['DOB']
        }
        return studentInfo
    else:
        return{"result":False} 
class MyStudents(pb2_grpc.MyStudentsServicer):

    def student_details(self, request,context):
        print(f"Student Request Received :{request.student_Id_number}")
        studentID = request.student_Id_number
        print(studentID)
        o_response = GetStudentInfo(studentID)
        print(o_response)
        return pb2.Student_Data(result=o_response['result'],
        name=o_response['name'],surname=o_response['surname'],
        Date_of_birth= o_response['date_of_birth'])



def server():
    print("Starting Server")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_MyStudentsServicer_to_server(MyStudents(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print('Server is running on port :50051')
    server.wait_for_termination()
  

if __name__ == '__main__':
    server()

    # https://github.com/danielgtaylor/python-betterproto
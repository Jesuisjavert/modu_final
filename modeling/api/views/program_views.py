from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import Program
from ..serializers import ProgramSerialiezer, ClientSerializer, ProgramUserSerialiezr
from django.http import Http404

class ProgramView(generics.ListCreateAPIView):
    # 프로그램 GET 정보가져오기
    queryset = Program.objects.all()
    serializer_class = ProgramSerialiezer

    # 프로그램 생성
    def post(self, request):
        serializer = ProgramSerialiezer(data=request.data)
        if request.user.is_first!=1:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid(raise_exception=True):
            serializer.save(trainer_id=request.user.trainer.first().id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProgramDetailView(APIView):
    def get_object(self, pk):
        try:
            return Program.objects.get(pk=pk)
        except Program.DoesNotExist:
            raise Http404

    # 프로그램 디테일
    def get(self, request, pk):
        program = self.get_object(pk)
        serializer = ProgramSerialiezer(program)
        return Response(serializer.data)

    # 프로그램 삭제
    def delete(self, request, pk):
        program = self.get_object(pk)
        if program.trainer.user.id == request.user.id:
            program.delete()
            return Response({"messgae": "삭제 완료"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 프로그램 수정
    def put(self, request, pk):
        program = self.get_object(pk)
        if program.trainer.user.id == request.user.id:
            serializer = ProgramSerialiezer(program, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(trainer_id=request.user.id)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({"message": "수정 실패"}, status=status.HTTP_400_BAD_REQUEST)

class TrainerProgramView(APIView):
    def get(self, request):
        try:
            trainer = request.user.trainer.first()
            programs = trainer.program.all()
            serializer = ProgramSerialiezer(programs, many=True)
            return Response(serializer.data)
        except:
            return Response({"message": "트레이너가 아닙니다"},status=status.HTTP_400_BAD_REQUEST)

class ProgramUserView(APIView):
    def get(self, request, pk):
        program = Program.objects.get(pk=pk)
        clients = program.programpayment.all()
        serializer = ProgramUserSerialiezr(clients, many=True)
        return Response(serializer.data)

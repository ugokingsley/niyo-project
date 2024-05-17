from django.shortcuts import render
from rest_framework import viewsets, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from .models import *
from authApi.models import *
from .producer import publish

class TaskManagerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for task.
    """
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        try:
            # Check to see if task exists for a particular user
            # and display it/them
            allTasks = TaskManager.objects.filter(user=request.user) 
            if allTasks.exists():
                serializer = self.get_serializer(allTasks, many=True)
                publish('task Listing', serializer.data) # create a socket stream
                return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response
            else:
                return Response(
                    {"message": ["User has no task yet"]},
                    status=status.HTTP_400_BAD_REQUEST,
                ) # return error response

        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST) # return error response

    def create(self, request):
        # create a new task object
        # check to see if data from the serializer is valid before saving 
        serializer = TaskManagerSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        serializer.save(user=self.request.user)
        publish('Task Created Successfully', serializer.data) # create a socket stream
        return Response({
            "status": 201,
            "message": ["Task Created Successfully"]},
            status=status.HTTP_201_CREATED,
            ) # return task oject response

    def retrieve(self, request, *args, **kwargs):
        # retrieve/read task by id created by a particular user 
        # check if task exists, throw an error is it doesn't
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_204_NO_CONTENT,) # return error response
        else:
            #any additional logic
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response

    def update(self, request, *args, **kwargs):
        # update task by id created by a particular user 
        # check if task exists, throw an error is it doesn't
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_204_NO_CONTENT,) # return error response
        else:
            serializer = self.get_serializer(instance)
            super().update(request, *args, **kwargs)
            publish('Task Updated Successfully', serializer.data) # create a socket stream
            return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response
    
    def destroy(self, request, *args, **kwargs):
        # Delete task by id created by a particular user 
        # check if task exists, throw an error is it doesn't
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_204_NO_CONTENT,) # return error response
        else:
            serializer = self.get_serializer(instance)
            instance.delete()
            #publish('Task Deleted Successfully', serializer.data) # create a socket stream
            return Response({'message':'Task Deleted'}, status=status.HTTP_204_NO_CONTENT) # return task oject response
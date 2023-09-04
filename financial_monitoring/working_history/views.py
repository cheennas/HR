# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
# from .models import WorkingHistory
# from .serializers import WorkingHistorySerializer
#
#
# class WorkingHistoryListView(ListAPIView):
#     serializer_class = WorkingHistorySerializer
#     lookup_field = 'iin'
#
#     def get_queryset(self):
#         iin = self.kwargs.get(self.lookup_field)
#         queryset = WorkingHistory.objects.filter(iin=iin)
#         return queryset
#
#
# class WorkingHistoryCreateView(CreateAPIView):
#     queryset = WorkingHistory.objects.all()
#     serializer_class = WorkingHistorySerializer
#
#
# class WorkingHistoryUpdateView(APIView):
#     def patch(self, request, iin, format=None):
#         current_data = request.data.get('working_history')
#
#         for data in current_data:
#             id = data.pop('id', None)
#
#             if id:
#                 WorkingHistory.objects.filter(id=id).update(**data)
#
#         return Response({"message": "Object updated successfully"}, status=200)
#
#
# class WorkingHistoryDestroyView(DestroyAPIView):
#     queryset = WorkingHistory.objects.all()
#     serializer_class = WorkingHistory
#     lookup_field = 'iin'
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WorkingHistory
from .serializers import WorkingHistorySerializer


class WorkingHistoryView(APIView):

    def get(self, request, iin=None):
        if iin is None:
            orders = WorkingHistory.objects.all()
            serializer = WorkingHistorySerializer(orders, many=True)
        else:
            try:
                orders = WorkingHistory.objects.filter(iin__id=iin)
                serializer = WorkingHistorySerializer(orders, many=True)
            except WorkingHistory.DoesNotExist:
                return Response({"detail": "Working Histories not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def post(self, request):
        serializer = WorkingHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            order = WorkingHistory.objects.get(pk=pk)
        except WorkingHistory.DoesNotExist:
            return Response({"detail": "Working History not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = WorkingHistorySerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            order = WorkingHistory.objects.get(pk=pk)
        except WorkingHistory.DoesNotExist:
            return Response({"detail": "Working History not found"}, status=status.HTTP_404_NOT_FOUND)

        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView, ListAPIView
from rest_framework.views import APIView
from .models import OrdersList
from .serializers import OrdersListSerializer
from rest_framework.response import Response


# class OrdersListView(ListAPIView):
#     serializer_class = OrdersListSerializer
#     lookup_field = 'iin'
#
#     def get_queryset(self):
#         iin = self.kwargs.get(self.lookup_field)
#         queryset = OrdersList.objects.filter(iin=iin)
#         return queryset
#
#
# class OrdersListCreateView(CreateAPIView):
#     queryset = OrdersList.objects.all()
#     serializer_class = OrdersListSerializer
#
#
# class OrdersListUpdateView(APIView):
#     def patch(self, request, iin, format=None):
#         current_data = request.data.get('orders_list')
#
#         for data in current_data:
#             id = data.pop('id', None)
#
#             if id:
#                 OrdersList.objects.filter(id=id).update(**data)
#
#         return Response({"message": "Object updated successfully"}, status=200)
#
#
# class OrdersListDestroyView(DestroyAPIView):
#     queryset = OrdersList.objects.all()
#     serializer_class = OrdersListSerializer

# UNCOMMENT ONLY WHEN IT IS 100% WORKING

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import OrdersList
from .serializers import OrdersListSerializer


class OrdersListView(APIView):

    def get(self, request, iin=None):
        if iin is None:
            orders = OrdersList.objects.all()
            serializer = OrdersListSerializer(orders, many=True)
        else:
            try:
                orders = OrdersList.objects.filter(iin__id=iin)
                serializer = OrdersListSerializer(orders, many=True)
            except OrdersList.DoesNotExist:
                return Response({"detail": "Orders not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdersListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        try:
            order = OrdersList.objects.get(pk=pk)
        except OrdersList.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrdersListSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            order = OrdersList.objects.get(pk=pk)
        except OrdersList.DoesNotExist:
            return Response({"detail": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

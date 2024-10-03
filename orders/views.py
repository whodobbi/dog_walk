from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        date = self.request.query_params.get("date", None)
        if date:
            return Order.objects.filter(walk_date=date)
        return Order.objects.none()


class OrderCreateView(generics.CreateAPIView):
    serializer_class = OrderSerializer

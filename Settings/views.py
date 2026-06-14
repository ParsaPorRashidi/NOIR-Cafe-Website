from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import BaristaOffer, Banner, FavoriteProduct, Category, Product, Event , WaiterCall
from .serializers import (
    BaristaOfferSerializer,
    BannerSerializer,
    FavoriteProductSerializer,
    CategorySerializer,
    ProductSerializer,
    EventSerializer,
    WaiterCallSerializer
)


class HomeAPIView(APIView):

    def get(self, request, *args, **kwargs):
        barista_offer = BaristaOffer.objects.order_by('-created_at').first()

        banners = Banner.objects.all()

        favorite_products = FavoriteProduct.objects.select_related('product', 'product__category').all()[:3]

        categories = Category.objects.all()

        menu_products = Product.objects.select_related('category').all()

        events = Event.objects.all()[:3]

        serializer_context = {'request': request}

        barista_serializer = BaristaOfferSerializer(barista_offer,
                                                    context=serializer_context).data if barista_offer else None
        banners_serializer = BannerSerializer(banners, many=True, context=serializer_context).data
        favorites_serializer = FavoriteProductSerializer(favorite_products, many=True, context=serializer_context).data
        categories_serializer = CategorySerializer(categories, many=True, context=serializer_context).data
        products_serializer = ProductSerializer(menu_products, many=True, context=serializer_context).data
        events_serializer = EventSerializer(events, many=True, context=serializer_context).data

        active_calls_count = WaiterCall.objects.filter(is_resolved=False).count()
        total_products = Product.objects.count()

        response_data = {
            "barista_offer": barista_serializer,
            "banners": banners_serializer,
            "special_products": favorites_serializer,
            "categories": categories_serializer,
            "menu_products": products_serializer,
            "events": events_serializer,
            "stats": {
                "active_waiter_calls": active_calls_count,
                "total_products": total_products
            }
        }

        return Response(response_data, status=status.HTTP_200_OK)

class WaiterCallCreateView(APIView):
    """ثبت درخواست جدید فراخوان گارسون"""
    def post(self, request):
        serializer = WaiterCallSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'success', 'message': 'گارسون صدا زده شد.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ActiveWaiterCallsView(APIView):
    """لیست درخواست‌های در انتظار (برای پولینگ ادمین)"""
    def get(self, request):
        active_calls = WaiterCall.objects.filter(is_resolved=False).order_by('-created_at')
        serializer = WaiterCallSerializer(active_calls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ResolveWaiterCallView(APIView):
    """تغییر وضعیت به دیده شد"""
    def post(self, request, pk):
        try:
            call = WaiterCall.objects.get(pk=pk)
            call.is_resolved = True
            call.save()
            return Response({'status': 'success', 'message': 'درخواست بایگانی شد.'}, status=status.HTTP_200_OK)
        except WaiterCall.DoesNotExist:
            return Response({'status': 'error', 'message': 'درخواست یافت نشد.'}, status=status.HTTP_404_NOT_FOUND)
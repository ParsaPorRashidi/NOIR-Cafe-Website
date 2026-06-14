from rest_framework import serializers
from .models import BaristaOffer, Banner, Category, Product, Event , FavoriteProduct , WaiterCall

class BaristaOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaristaOffer
        fields = '__all__'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='slug', read_only=True)

    class Meta:
        model = Product
        fields = '__all__'


class FavoriteProductSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = FavoriteProduct
        fields = ['id', 'product', 'created_at']

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class WaiterCallSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaiterCall
        fields = ['id', 'table_id', 'table_label', 'is_resolved', 'created_at']
        # این فیلدها موقع ساختن به صورت اتوماتیک پر میشن و نیازی نیست کاربر بفرسته
        read_only_fields = ['id', 'is_resolved', 'created_at']
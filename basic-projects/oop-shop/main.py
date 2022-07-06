from shop.models import Product
from abstract.serializers import BaseSerializer

obj1 = Product("iphone", 234, "...", 2)
obj2 = Product("samsung", 4334, "...", 4)
obj3 = Product("nokia", 5343, "...", 10)
res = BaseSerializer().serialize_queryset([obj1, obj2, obj3])
print(res)
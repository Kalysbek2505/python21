'=============Миксины==============='
# Миксины - классб который будет использоваться для наследования. от миксинов не создаются объекты
class CreateMixin:
    def product_create(self, title, price):
        obj = model()
        model = model.__class__
        _id = model._id
        obj.title = title
        obj.price = price
        obj.id = _id
        model.objects[_id] = obj
        model._id += 1

class ReadMixin:
    def product_detail(self, p_id):
        model = self.__class__
        obj = model.objects.get(p_id)
        print({'id':obj.id, 'title':obj.title, 'price': obj.price})

class UpdateMixin:
    pass



class DeleteMixin:
    def delete_product(self, p_id):
        model = self.__class__
        model.objects.pop(p_id)

class ProductCRUD(CreateMixin, UpdateMixin, ReadMixin, DeleteMixin):
    objects = {}
    _id = 1
    
crud = ProductCRUD()
crud.product_create('obj1', 45)
crud.product_create('obj2', 2321)
print(crud.objects)
crud.product_detail(1)
crud.delete_product(1)
print(crud.objects)
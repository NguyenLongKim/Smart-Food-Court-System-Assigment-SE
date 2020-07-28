from model.models.user import Cook
from model.models.order import OrderItem

class CookServices:
    @staticmethod
    def GetOrdersList(cook):
        orders_list = []
        for item in OrderItem.objects.all():
            if item.food.vendor == cook.work_for:
                orders_list.append(item)
        return orders_list

    @staticmethod
    def ChangeOrderStatus(order_id, new_status):
        order = OrderItem.objects.get(id=order_id)
        order.status = new_status
        order.save()
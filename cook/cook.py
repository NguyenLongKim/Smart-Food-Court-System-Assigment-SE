from model.models.user import Cook
from model.models.order import OrderItem

class CookServices:
    @staticmethod
    def GetOrdersList(cook):
        orders_list = []
        for item in OrderItem.objects.all():
            if item.food.vendor == cook.work_for and item.status!='finish':
                orders_list.append(item)
        if not orders_list:
            return None
        else:
            orders_list.reverse()
            return orders_list

    @staticmethod
    def ChangeOrderStatus(cook, new_statuses):
        order_items = CookServices.GetOrdersList(cook)
        i=0
        for item in order_items:
            item.status = new_statuses[i]
            item.save()
            i+=1
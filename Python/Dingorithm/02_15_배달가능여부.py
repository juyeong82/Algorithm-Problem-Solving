shop_menus = ["만두", "떡볶이", "오뎅", "사이다", "콜라"]
shop_orders = ["오뎅", "콜라", "만두"]

# 재귀(가능은 하나 틀린 접근)
def is_available_to_order(menus, orders):
    menus.sort()
    orders.sort()
    menu_cnt = 0
    for menu in menus:
        menu_cnt += 1
        if menu == orders[0]:
            if len(orders) == 1:
                return True
            else:
                return is_available_to_order(menus[:menu_cnt-1]+menus[menu_cnt:], orders[1:])
                
    return False

# set
def is_available_to_order(menus, orders):
    orders = set(orders)
    for menu in menus:
        if menu not in orders:
            return False
    return True

# 이분탐색 + for-else
def is_available_to_order(menus, orders):
    
    menus.sort()
    
    for order in orders:
        min = 0
        max = len(menus)-1
        
        while min <= max:
            cur = (min + max)//2
            if order == menus[cur]:
                break
            elif order > menus[cur]:
                min = cur + 1
            elif order < menus[cur]:
                max = cur - 1
        else:
            return False
    return True


result = is_available_to_order(shop_menus, shop_orders)
print(result)
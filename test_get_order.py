import creqate_order

def test_get_order_info():
    response = creqate_order.get_order_info()
    assert response.status_code == 200
#Елизавета Никитина 11-я когорта финальный проект инженер по тестированию плюс
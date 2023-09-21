import sending_requests


def get_track_number():  # Создание заказа и сохранение номера трека заказа
    track_number = sending_requests.post_new_order()
    return track_number.json()["track"]


def test_create_order_get_success_response():  # Получение заказа по треку заказа, проверка, что код ответа равен 200
    track_number = get_track_number()
    response = sending_requests.get_order_info(track_number)
    assert response.status_code == 200

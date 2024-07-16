# Суконченко Кристина, 18-я когорта — Финальный проект. Инженер по тестированию плюс

import sender_stand_request
import data


def test_positive_assert():
    track_response = sender_stand_request.post_new_order(data.order_body)
    track = track_response.json()["track"]
    order_response = sender_stand_request.get_order(track)

    assert order_response.status_code == 200


def data_from_response(response: dict) -> dict:
    """response에 문제가 없다면 response의 payload를 반환
    - reponse 사전의 예제::
    {
        "status": 200, # <int>
        "timestamp": "....", # 현재 시간의 ISO 포맷 문자열
        "payload": { ... } # 반환하려는 사전 데이터
    }

    - 반환 사전 값의 예제::
    {"data": { .. } }

    - 발생 가능한 예외:
    - HTTP status가 200이 아닌 경우 ValueError 발생
    """
    if responce["status"] != 200:
        raise ValueError
    return {"data": response["payload"]}

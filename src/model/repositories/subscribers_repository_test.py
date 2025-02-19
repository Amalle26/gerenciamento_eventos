from .subscribers_repository import SubscribersRepository


def test_insert():
    subscriber_info = {
        "name": "meuNome",
        "email": "email@email.com",
        "evento_id": 2
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)
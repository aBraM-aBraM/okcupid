from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
    photos: list[dict]
    targetLikesSender: bool
    user_id: str
    user_content: dict[str, str]

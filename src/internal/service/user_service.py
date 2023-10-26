"""
Module containing code related to a user service.
"""
from internal.database import Session
from internal.database.query import delete_batch_by_uid


class UserService:
    """
    A service class for handling logic connected to users.
    """

    def delete_users_data(self, user_id: str) -> None:
        """
        Method for deleting all user's data.
        """
        session = Session()
        session.execute(delete_batch_by_uid(user_id))
        session.commit()

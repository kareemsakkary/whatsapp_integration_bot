import abc
from models import Message

class ChatAppIntegration:
    @abc.abstractmethod
    def return_message(self, message: str):
        """Send a message to the chat application."""
        pass

    @abc.abstractmethod
    def receive_message(self) -> Message:
        """Receive a message from the chat application."""
        pass



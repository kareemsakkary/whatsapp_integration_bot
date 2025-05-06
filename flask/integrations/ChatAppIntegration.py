import abc
class ChatAppIntegration:
    @abc.abstractmethod
    def send_message(self, message: str) -> None:
        """Send a message to the chat application."""
        pass

    @abc.abstractmethod
    def receive_message(self) -> str:
        """Receive a message from the chat application."""
        pass



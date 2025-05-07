import abc
from models import Message
"""
Abstract base class for bots.
"""
class Bot(abc.ABC):

    @abc.abstractmethod
    def extract_data(self, data: str) -> str:
        """
        Extract relevant data from the input string.
        """
        pass

    @abc.abstractmethod
    def process(self, data: str) -> str:
        """
        Process the given data and return the result.
        """
        pass

    @abc.abstractmethod
    def build_response(self, message:Message, extracted_data:str, answer:str) -> Message:
        """
        Build a response based on the processed data.
        """
        pass

    def run(self, data: Message) -> Message:
        """
        Run the bot on the given data.
        """
        extracted_data = self.extract_data(data)
        answer = self.process(extracted_data)
        response = self.build_response(data, extracted_data, answer)
        return response

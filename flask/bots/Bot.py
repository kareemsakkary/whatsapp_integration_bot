import abc

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

    def run(self, data: str) -> str:
        """
        Run the bot on the given data.
        """
        extracted_data = self.extract_data(data)
        return self.process(extracted_data)
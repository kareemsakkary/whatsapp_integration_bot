import re
from Bot import Bot

class MathmaticalBot(Bot):
    """
    A bot that performs mathematical operations.
    """
    
    def extract_data(self, data: str) -> str:
        """
        Extract relevant data from the input string.
        Input string could be a text containing a mathematical expression.
        This method uses regex to find numbers and operators.
        Assume there is one Equation in the string if there are more will excute the first one.
        """

        # Regex to find a mathematical expression in the string
        pattern = r'([-+]?\d*\.?\d+|\+|\-|\*|\/|\(|\))+'
        matches = re.findall(pattern, data)
        
        # Join the matches to form a valid mathematical expression
        if matches:
            return ''.join(matches)
        return ''
    
    def process(self, data: str) -> str:
        """
        Process the given data and return the result.
        """
        try:
            # Evaluate the mathematical expression safely
            result = eval(data)
            return str(result)
        except Exception as e:
            return f"Error processing data: {e}"


# test
if __name__ == "__main__":
    bot = MathmaticalBot()
    test_data = "What is the result of 3+5*(2-8)?"
    extracted_data = bot.extract_data(test_data)
    # result = bot.process(extracted_data)
    print(f"Extracted Data: {extracted_data}")
    # print(f"Result: {result}")
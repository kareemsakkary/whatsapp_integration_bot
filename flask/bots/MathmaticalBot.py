import re
from bots import Bot
from models import Message



class MathmaticalBot(Bot):
    """
    A bot that performs mathematical operations.
    """
    
    def extract_data(self, message: Message) -> str:
        """
        Extract relevant equation from the message.
        message could be a text containing a mathematical expression.
        This method uses regex to find numbers and operators.
        Assume there is one Equation in the string if there are more will excute the first one.
        """
        if message.is_audio:
            # If the message is audio, we cannot process it as a mathematical expression
            return ""
        else:
            if not message.body:
                raise ValueError("يرجى تقديم معادلة رياضية.")
            # Regex to find a mathematical expression in the string
            pattern = r'((?:\s*[-+]?\d+(?:\.\d+)?\s*[\+\-\*/\(\)\×\÷]\s*)+[-+]?\d+(?:\.\d+)?)'
            match = re.search(pattern, message.body)
            if match:
                # Remove all spaces to return a clean expression
                equation = match.group(0).replace(' ', '')
                if not equation:
                    raise ValueError("يرجى تقديم معادلة رياضية.")
                equation = equation.replace('×', '*').replace('÷', '/')
                return equation
            raise ValueError("لم أتمكن من العثور على معادلة رياضية صحيحة في الرسالة.")    
    
    def process(self, equation: str) -> str:
        """
        Process the given equation and return the result.
        """
        if not equation:
            return ""
        try:
            result = eval(equation)
            result = round(result, 2)
        except Exception as e:
            print(f"{equation}")
            raise ValueError(f"خطأ في المعادلة: {equation}")
        return f"{result}"
   
    def build_response(self, message:Message, equation : str,  answer: str) -> Message:
        """
        Build a response based on the processed equation.
        """
        response_message = Message()
        response_message.sender_phone = message.sender_phone
        if message.is_audio:
            response_message.is_audio = True
            response_message.audio_url = "static/response.mp3"
        else:
            response_message.body =  """
            *المعادلة:*\n {equation}\n
            *النتيجة:*\n {answer}
            """.format(equation=equation, answer=answer)
        
        return response_message
    
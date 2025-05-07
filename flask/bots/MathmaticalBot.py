import re
from bots import Bot
from models import Message



class MathmaticalBot(Bot):
    """
    A bot that performs mathematical operations.
    """
    
    def extract_data(self, message: Message) -> str:
        """
        Extract relevant expression from the message.
        message could be a text containing a mathematical expression.
        This method uses regex to find numbers and operators.
        Assume there is one Expression in the string if there are more will excute the first one.
        """
        if message.is_audio:
            # If the message is audio, we cannot process it as a mathematical expression
            return ""
        else:
            if not message.body:
                raise ValueError("يرجى تقديم صيغة رياضية.")
            # Regex to find a mathematical expression in the string
            pattern = r'((?:\s*[-+]?\d+(?:\.\d+)?\s*[\+\-\*/\(\)\×\÷]\s*)+[-+]?\d+(?:\.\d+)?)'
            match = re.search(pattern, message.body)
            if match:
                # Remove all spaces to return a clean expression
                expression = match.group(0).replace(' ', '')
                if not expression:
                    raise ValueError("يرجى تقديم صيغة رياضية.")
                expression = expression.replace('×', '*').replace('÷', '/')
                return expression
            raise ValueError("لم أتمكن من العثور على صيغة رياضية صحيحة في الرسالة.")    
    
    def process(self, expression: str) -> str:
        """
        Process the given expression and return the result.
        """
        if not expression:
            return ""
        try:
            result = eval(expression)
            result = round(result, 2)
        except Exception as e:
            print(f"{expression}")
            raise ValueError(f"خطأ في الصيغة: {expression}")
        return f"{result}"
   
    def build_response(self, message:Message, expression : str,  answer: str) -> Message:
        """
        Build a response based on the processed expression.
        """
        response_message = Message()
        response_message.sender_phone = message.sender_phone
        if message.is_audio:
            response_message.is_audio = True
            response_message.audio_url = "static/response.m4a"
        else:
            response_message.body =  """
            *الصيغة:*\n {expression}\n
            *النتيجة:*\n {answer}
            """.format(expression=expression, answer=answer)
        
        return response_message
    
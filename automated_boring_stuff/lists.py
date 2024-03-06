# Comma Code
import logging

logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")

def comma_code(spam: list) -> str:
    
    result = ', '.join(spam[:-1]) + f", and {spam[-1]}"
    
    return result
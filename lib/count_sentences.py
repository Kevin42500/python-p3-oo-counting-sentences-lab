import re

class MyString:
    def __init__(self):
        self.value = ""

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("Value must be a string")

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
       
        sentences = re.split(r'[.!?]', self._value)
      
        sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
        
        return len(sentences)

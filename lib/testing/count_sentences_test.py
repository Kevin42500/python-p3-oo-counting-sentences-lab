import io
import sys
import pytest
from lib.count_sentences import MyString

class TestMyString:
    def test_value_string(self):
        '''prints "The value must be a string." if not string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        string = MyString()
        string.value = "123" 
        assert captured_out.getvalue().strip() == "The value must be a string"


        sys.stdout = sys.__stdout__

    def test_is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        string = MyString()
        string.value = "Hello World."
        assert string.is_sentence() == True

    def test_is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        string = MyString()
        string.value = "Is anybody there?"
        assert string.is_question() == True

    def test_is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        string = MyString()
        string.value = "It's me!"
        assert string.is_exclamation() == True

def count_sentences(self):
  
    sentences = re.split(r'[.!?]', self._value)
    
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return len(sentences)


if __name__ == '__main__':
    pytest.main()

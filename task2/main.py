from lexer import Lexer
from interpreter import Interpreter
from parser import Parser

def main():
    while True:
        try:
            text = input('Please enter the expression or exit to quit: ')
            
            if text.lower() == 'exit':
                print('Exit the program')
                break
            
            lexer = Lexer(text)
            parser = Parser(lexer)
            interpreter = Interpreter(parser)
            result = interpreter.interpret()
            print(result)
            
        except Exception as e:
            print(e)
            
if __name__ == '__main__':
    main()
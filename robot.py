import termcolor

DEFAULT_ROBOT_NAME = 'Roboko'

class Robot(object):
    
    def __init__(self, user_name=None, name=DEFAULT_ROBOT_NAME):
        self.user_name = user_name
        self.name = name
    
    def hello(self):
        with open('hello.txt') as file:
           hello_content = file.read()
           user_name_replace = hello_content.replace('$robot_name', self.name)
           show_file = input(termcolor.colored(user_name_replace, 'red'))
        print(termcolor.colored(show_file, 'red'))
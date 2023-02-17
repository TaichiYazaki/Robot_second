import ranking
import console


DEFAULT_ROBOT_NAME = 'Roboko'
RANKING_COLUMN_NAME = 'NAME'

is_file = 'ranking.csv'
header = ['name', 'count']


class Robot(object):
    
    def __init__(self, user_name='', name=DEFAULT_ROBOT_NAME, speak_color='green'):
        self.user_name = user_name
        self.name = name
        self.speak_color = speak_color
    
    def hello(self):
        while True:
            template = console.get_template('hello.txt', self.speak_color)
            user_name = input(template.substitute({
                'robot_name': self.name}))

            if user_name:
                self.user_name = user_name.title()
                break


class RestaurantRobot(Robot):

    def __init__(self, user_name='', name=DEFAULT_ROBOT_NAME, speak_color='green'):
        super().__init__(user_name, name, speak_color)
        self.ranking_model = ranking.RankingModel()

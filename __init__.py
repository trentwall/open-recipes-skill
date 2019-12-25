from mycroft import MycroftSkill, intent_file_handler


class OpenRecipes(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('recipes.open.intent')
    def handle_recipes_open(self, message):
        self.speak_dialog('recipes.open')


def create_skill():
    return OpenRecipes()


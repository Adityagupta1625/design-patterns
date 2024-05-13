
class Button:
    def render(self):
        pass

class LightButton(Button):
    def render(self):
        return "Light Button"

class DarkButton(Button):
    def render(self):
        return "Dark Button"


class UIFactory:
    def create_button():
        pass

class LightThemeFactory(UIFactory):
    def create_button(self):
        return LightButton()

class DarkThemeFactory(UIFactory):
    def create_button(self):
        return DarkButton()

light_factory = LightThemeFactory()
light_button = light_factory.create_button()
print(light_button.render())

dark_factory = DarkThemeFactory()
dark_button = dark_factory.create_button()
print(dark_button.render())

# Reference Link:
# https://www.linkedin.com/pulse/design-patterns-real-examples-go-part-3-abstract-factory-araujo/?lipi=urn%3Ali%3Apage%3Ad_flagship3_pulse_read%3BQSOW4jyuTSWQVZCw2SOZlA%3D%3D
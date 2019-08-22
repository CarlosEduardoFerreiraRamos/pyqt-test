from jinja2 import Template

# Something

class Reader(object):

    def __init__(self):
        self.template = None
        self.values = {}

    def parse(self, file):
        self.template = Template(file)

    def set_values(self, values):
        self.values = values

    def render(self):
        self.template.render(self.value)

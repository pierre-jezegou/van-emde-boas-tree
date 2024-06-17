''' Aim of this file :
    - Use json export from word_challenge to plot performances charts/plots
'''
from jinja2 import Template

EXPORT_PATH = "documentation/images/visualizations/"
TEMPLATE_PATH = "resources/class_description_template.tex.jinja"

printable_methods = [
    "__init__",
    "__repr__",
    "__eq__",
    "__lt__",
    "__hash__",
]

class ObjectClassToTikz():
    '''Draw TiKz images from class to show graphically the class construction'''
    def __init__(self, object, template_path: str = TEMPLATE_PATH, hidden_methods: bool = False) -> None:
        self.object = object
        self.classname = self.object.__class__.__name__
        self.attributes = self.object.__dict__.keys()
        self.methods = [method for method in dir(self.object)
                        if callable(getattr(self.object, method))
                        and (not method.startswith('__') if hidden_methods==False else (method in printable_methods or not method.startswith('__')))]
        self.template_path = template_path
        self.hidden_methods = hidden_methods


    def build_elements(self, elements) -> str:
        '''Parse attributes/methods from a class'''
        attributes_code = ""
        for i, key in enumerate(list(elements)):
            # Check if hidden method
            attributes_code += r"\small{%d}: \verb|%s|" % (i, key)
            if i != len(list(elements)) - 1:
                attributes_code += "\\\\\n"
        return attributes_code

    def save_drawing(self) -> None:
        '''Use classes attributes/methods and write in a TiKz template'''
        filename = f"class_%s.tex" % self.classname

        context = {
            'title': self.classname,
            'attributes': self.build_elements(self.attributes),
            'methods': self.build_elements(self.methods)
        }

        with open(self.template_path, 'r') as f:
            template_content = f.read()

        template = Template(template_content)

        with open(EXPORT_PATH + filename, 'w') as f:
            f.write(template.render(context))


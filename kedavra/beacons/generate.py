from jinja2 import Environment, FileSystemLoader
import os
import base64

def render_template(template_path, **args):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(f'{current_dir}/template'))  # Spécifiez le répertoire racine des modèles
    template = env.get_template(template_path)
    rendered_template = template.render(**args)
    main_template = env.get_template('main.py')
    b64 = base64.b64encode(rendered_template.encode('utf-8')).decode('utf-8')
    final_template = main_template.render(CONTENT=b64)
    return final_template

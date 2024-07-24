from pathlib import Path
import re

def walk_python (levels_dir):


    py_dirs = list(sorted(set(p.parent for p in levels_dir.rglob('*.py') if not p.name == '__init__.py')))
    
    return [ (p, len(list(p.glob('*.py')))) for p in py_dirs]

def walk_images(levels_dir):

    resource_extensions = ('.png', '.gif', '.jpeg', '.jpg')

    image_dirs = [p for p in levels_dir.rglob('*') if p.suffix in resource_extensions]

    return image_dirs


def get_lmla(dir_=None):
    """Get level, module, lesson, assignment from a directory"""
    if dir_ is None:
        p = Path('.')
    else:
        p = Path(dir_)

    p = str(p.absolute())


    if re.search('/Level\d+/Module\d+/.*\.py', p):
        # Form of:  levels/Level1/Module4/01_dictionaries
        # Extract the level and module names with regex,
        # then the next is the lesson, and after that is the assignment.
        # If there are only 3 parts, then the lesson is the assignment.

        # Regex to extract Lesson and Module
        lm = re.search(r'Level\d+/Module\d+', p).group()
        l, m = lm.split('/')

        # Extract the lesson and assignment
        parts = p.split('/')

        if len(parts) > parts.index(m) + 2:
            ls = parts[parts.index(m) + 1]
            a = parts[parts.index(m) + 2]
        else:
            ls = a = parts[parts.index(m) + 1]

        return l, m, ls, a



    else:

        return None, None, None, None



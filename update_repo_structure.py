import os
import shutil
import glob
import click
import os

import logging

logger = logging.getLogger(__name__)


# List of directories and files to ignore
ignore_list = ['__init__.py', '_init.py', 'init.py', '.pyproject', '.project',
               '.gitignore', '.git', '.vscode', 'LICENSE', 'update_repo_structure.py',
               '.mypy_cache', '.pydevproject', '_out']

def create_new_structure(original_path, new_path):
    stack = [(original_path, new_path)]

    while stack:
        current_original, current_new = stack.pop()

        # Use glob for a simpler way to get files and directories
        entries = glob.glob(os.path.join(current_original, '*')) + glob.glob(os.path.join(current_original, '.*'))
        
        for item_path in entries:
            entry_name = os.path.basename(item_path)
            if entry_name.startswith('.'):
                logger.debug(f'Renaming dot file: {entry_name}')
                entry_name = entry_name[1:]
            
            if os.path.isdir(item_path) and entry_name not in ignore_list:
                # Handle directories
                if "Level" in entry_name or "Module" in entry_name or "module" in entry_name:
                    if "-" in entry_name:
                        dir_to_add, sub_dir_to_add = entry_name.split('-', 1)
                    else:
                        dir_to_add, sub_dir_to_add = entry_name.split('_', 1)

                    new_directory_path = os.path.join(current_new, dir_to_add, sub_dir_to_add)
                    try:
                        os.makedirs(new_directory_path)
                        stack.append((item_path, new_directory_path))
                    except FileExistsError:
                        continue
                else:
                    new_directory_path = os.path.join(current_new, entry_name)
                    try:
                        os.makedirs(new_directory_path)
                        stack.append((item_path, new_directory_path))
                    except FileExistsError:
                        continue

            else:
                # Handle files                
                if entry_name not in ignore_list:
                    if entry_name.startswith('_'):
                        entry_name = entry_name[1:]
                    
                    if entry_name.endswith(('.py', '.pyde')):
                        # Create the new directory with the Python file's name and the '_' removed
                        if entry_name.startswith('_'):
                            new_directory_path = os.path.join(current_new, entry_name[1:-3] if entry_name.endswith('.py') else entry_name[1:-5])
                        else:
                            new_directory_path = os.path.join(current_new, entry_name[:-3] if entry_name.endswith('.py') else entry_name[:-5])
                        new_directory_path = os.path.join(current_new, os.path.splitext(entry_name)[0])
                        try:
                            os.makedirs(new_directory_path)
                            stack.append((item_path, new_directory_path))
                        except FileExistsError:
                            pass
                        # Move the file to the new directory
                        shutil.copy2(item_path, new_directory_path)
                    else:
                        # CREATE THE NEW DIRECTORY NAMED RESOURCES AND ADD IT TO THE STACK
                        try:
                            new_directory_path = os.path.join(current_new, 'resources')
                            os.makedirs(new_directory_path)
                            stack.append((item_path, new_directory_path))
                        except FileExistsError:
                            pass
                        if stack:
                            _, latest_directory = stack[-1]
                            shutil.copy2(item_path, latest_directory)


def remove_underscore_from_files(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.startswith('_'):
                new_file_name = file[1:]
                old_file_path = os.path.join(root, file)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)



@click.command()
@click.option('--original_path', '-o', default=os.getcwd(), help='Path to the original directory')
@click.option('--new_path', '-n', default='_out', help='Path to the new directory')
@click.option('--verbose', '-v', is_flag=True, help='Enable verbose logging')

def main(original_path: str , new_path: str, verbose: bool):

    if verbose:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)

    logger.info(f'Source path: {original_path}')
    logger.info(f'Destination path: {new_path}')
    create_new_structure(original_path, new_path)
    remove_underscore_from_files(new_path)

if __name__ == '__main__':
    main()


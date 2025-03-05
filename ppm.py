import sys
import os
import json
import subprocess
import importlib.metadata
import time
from colorama import Fore, Style, init

init(autoreset=True)

VERSION = "0.1"

def print_debug(message):
    print(f"{Fore.CYAN}[DEBUG] {message}{Style.RESET_ALL}")

def print_success(message):
    print(f"{Fore.GREEN}[SUCCESS] {message}{Style.RESET_ALL}")

def print_error(message):
    print(f"{Fore.RED}[ERROR] {message}{Style.RESET_ALL}")

def print_warning(message):
    print(f"{Fore.YELLOW}[WARNING] {message}{Style.RESET_ALL}")

def create(name_project):
    try:
        print_debug(f"Creating project '{name_project}'...")
        os.mkdir(name_project)
        os.chdir(name_project)
        dependencies = {
            "example-lib": "1.0.0"
        }
        project = {
            "Name": name_project,
            "Version": 0.1,
            "BaseFile": "src/main.py"
        }
        with open('dependencies.json', 'w') as f:
            json.dump(dependencies, f, indent=4)
        with open('project.json', 'w') as f:
            json.dump(project, f, indent=4)
        print_success(f'Project "{name_project}" created successfully.')
        os.mkdir('src')
        os.chdir('src')
        with open('main.py', 'w') as f:
            f.write('print("Hello, PPM")\n')
    except FileExistsError:
        print_error(f'Directory "{name_project}" already exists.')
    except Exception as e:
        print_error(e)

def install_dependencies():
    try:
        print_debug("Checking dependencies...")
        with open('dependencies.json', 'r') as f:
            dependencies = json.load(f)
        
        for package, version in dependencies.items():
            try:
                installed_version = importlib.metadata.version(package)
                if installed_version != version:
                    print_warning(f'Updating {package} to version {version}...')
                    subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{package}=={version}', '--break-system-packages'])
                else:
                    print_success(f'{package} is already at the required version {version}.')
            except importlib.metadata.PackageNotFoundError:
                print_warning(f'Installing {package} version {version}...')
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', f'{package}=={version}', '--break-system-packages'])
    except FileNotFoundError:
        print_error('No dependencies.json file found.')

def run():
    try:
        print_debug("Running project...")
        install_dependencies()
        time.sleep(0.5)
        print_success("Starting execution...")
        time.sleep(0.5)
        os.system('clear')
        with open('project.json', 'r') as f:
            project = json.load(f)
        
        base_file = project.get("BaseFile", "src/main.py")
        print_debug(f'Executing {base_file}...')
        subprocess.check_call([sys.executable, base_file])
    except Exception as e:
        print_error(e)

def print_help():
    print(f"{Fore.YELLOW}PPM - the simple and fast python3 project manager{Style.RESET_ALL}")
    print(f"{Fore.BLUE}Usage:{Style.RESET_ALL}")
    print(f"  ppm create <project_name>  - Create a new project")
    print(f"  ppm run                    - Run the project")
    print(f"  ppm --help                 - Show this help message")
    print(f"  ppm --version              - Show the version")

def print_version():
    print(f"PPM Version: {VERSION}")

if __name__ == '__main__':
    try:
        if len(sys.argv) < 2:
            print_help()
        elif sys.argv[1] == 'new' and len(sys.argv) == 3:
            create(sys.argv[2])
        elif sys.argv[1] == 'run':
            run()
        elif sys.argv[1] == '--help':
            print_help()
        elif sys.argv[1] == '--version':
            print_version()
        else:
            print_error("Unknown command or incorrect arguments!")
            print_help()
    except Exception as e:
        print_error(e)

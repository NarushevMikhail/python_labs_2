from cli import CLI
from app import Application
from storage import Storage

def main():
    storage = Storage('users.json')
    app = Application(storage)
    cli = CLI(app)
    cli.start()

if __name__ == '__main__':
    main()
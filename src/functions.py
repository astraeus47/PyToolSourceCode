from settings import *
from settings import _gettext
from time import sleep


# Custom alert function using print().
def alert(type, text):
    try:
        # SUCCESS.
        if type == 'success':
            success_text = _gettext("[SUCCESS]:")
            print(_gettext(f"{fg_success}{success_text} {fg_text}{text}"))

        # INFO.
        elif type == 'info':
            info_text = _gettext("[INFO]:")
            print(_gettext(f"{fg_info}{info_text} {fg_text}{text}"))

        # ERROR.
        elif type == 'error':
            error_text = _gettext("[ERROR]:")
            print(_gettext(f"{fg_error}{error_text} {fg_text}{text}"))

        else:
            type = 'error'
            print(_gettext(f"{fg_error}{error_text} {fg_text}{text}"))
    
    except Exception as error:
        alert(None, error)


# Login function.
def login():
    while True:
        os.system(f'cls && title Login')
        
        # Input username.
        text = _gettext("Enter your username:")
        user = input(f'{fg_one}{text} {fg_text}')

        # Input password.
        text = _gettext("Enter your password:")
        passwd = input(f'{fg_one}{text} {fg_text}')

        # Performs user verification.
        if user == STORED_USERNAME and hashlib.sha256(passwd.encode()).hexdigest() == STORED_PASSWORD_HASH:
            alert('success', _gettext("Access authorized!"))
            sleep(3)
            break

        else:
            alert('error', _gettext("Access not authorized!"))
            sleep(3)


# Whenever you add a new command or category, you should use this code structure to list and return them.
def list_commands(): 
    commands_found = {
        # Whenever you add a new category, also add it as it is below.
        # _gettext("New Category"): [f"{cmd}: {desc}" for cmd, desc in default.items()],
        
        _gettext("Default Commands"): [f"{cmd}: {desc}" for cmd, desc in default.items()],
        _gettext("Tool Commands"): [f"{cmd}: {desc}" for cmd, desc in tools.items()]
    }
    return commands_found


# If used, displays information about the transmitted command.
def cmd_info(arg):
    for cmds in list_commands().values():
        for cmd in cmds:
            if cmd.startswith(f'{arg}: '):
                print(cmd)
                return
    alert('error', _gettext("Command not found!"))


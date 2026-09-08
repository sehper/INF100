import sys
from subprocess import run

package_name = 'uib-inf100-graphics'

# Sjekk at Python-versjonen er 3.10 eller nyere
if ((sys.version_info[0] != 3) or (sys.version_info[1] < 10)):
    raise Exception(f'{package_name} requires Python 3.10 or later. '
            + 'Your current version is: '
            + f'{sys.version_info[0]}.{sys.version_info[1]}')

# Spør brukeren om å installere pakken
ans = input(f'\n\nType yes to install {package_name}: ')
if ((ans.lower() == 'yes') or (ans.lower() == 'y')):
    print()

    # Oppdater pip
    cmd_pip_update = f'{sys.executable} -m pip install --upgrade pip'
    print(f'Attempting to update pip with command: {cmd_pip_update}')
    run(cmd_pip_update.split())
    print()

    # Installer pakken
    cmd_install = f'{sys.executable} -m pip install {package_name}'
    print(f'Attempting to install {package_name} with command: {cmd_install}')
    run(cmd_install.split())
else:
    print(f'Did not attempt to install {package_name} now')
print('\n')
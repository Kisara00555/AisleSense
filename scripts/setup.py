"""First-time setup for the Windows presentation environment; requires internet."""
from pathlib import Path
import os
import shutil
import subprocess
import sys
import venv

ROOT = Path(__file__).resolve().parent.parent

def run(args):
    subprocess.run([str(x) for x in args], cwd=ROOT, check=True)

def main():
    if sys.version_info[:2] != (3, 13):
        raise SystemExit('Use Python 3.13 for the verified lock file: py -3.13 scripts/setup.py')
    npm = shutil.which('npm.cmd' if os.name == 'nt' else 'npm')
    node = shutil.which('node')
    if not npm or not node:
        raise SystemExit('Install Node.js 24, reopen the terminal, then run setup again.')
    if subprocess.check_output([node, '--version'], text=True).strip().split('.')[0] != 'v24':
        raise SystemExit('Use Node.js 24 for the verified frontend setup.')
    env = ROOT / '.venv'
    interpreter = env / ('Scripts/python.exe' if os.name == 'nt' else 'bin/python')
    if not interpreter.exists():
        venv.EnvBuilder(with_pip=True).create(env)
    run([interpreter, '-m', 'pip', 'install', '-r', 'requirements-lock.txt'])
    run([npm, 'ci'])
    run([npm, 'run', 'build'])
    run([interpreter, 'scripts/download_model.py'])
    print('Setup complete. Run Start Business Dashboard.cmd or .venv/Scripts/python.exe launch.py --system')

if __name__ == '__main__':
    main()

"""Build the manual with MkDocs in strict mode."""
from pathlib import Path
import os, subprocess, sys
ROOT = Path(__file__).resolve().parents[1]
env = dict(os.environ, NO_MKDOCS_2_WARNING='1')
subprocess.run([sys.executable, '-m', 'mkdocs', 'build', '--strict'], cwd=ROOT, env=env, check=True)

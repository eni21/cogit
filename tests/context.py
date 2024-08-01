import sys
import os
import json

srcPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
sys.path.insert(0, srcPath)

# print(f'srcPath={srcPath}')
# print(f'sys.path={json.dumps(sys.path, indent=2)}')

import src

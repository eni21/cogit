# этот файл нужен для поддержки тестов
#
# папки src и tests имеют одинаковую структуру
# это приводит к тому что образуются модули с одинаковыми названиями
# что бы обойти эту проблему добавляем $projectRoot в os.path
# и ссылки на модули делаем из рута

import sys
import os
import json

rootPath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, rootPath)

# print(f'rootPath={rootPath}')
# print(f'sys.path={json.dumps(sys.path, indent=2)}')


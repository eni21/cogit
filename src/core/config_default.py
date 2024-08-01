config_default = {
            'cwd': '.',
            'branch': 'develop',
            'pattern': '{major}.{minor}.{patch}',
            'convention': {
                'major': '^[a-zA-Z0-9 _-]+(\([a-zA-Z0-9 _-]+\))?!:',
                'minor': '^feat ?(\([a-zA-Z0-9 _-]+\))?:',
                'patch': '^fix ?(\([a-zA-Z0-9 _-]+\))?:'
                #'patch': '.*'
            },
            'bumps': [
                # {'filename': '', 'pattern': ''}
            ],
            'types': [
                'build',
                'chore',
                'ci',
                'docs',
                'feat',
                'fix',
                'perf',
                'refactor',
                'revert',
                'style',
                'test'
            ],
        }

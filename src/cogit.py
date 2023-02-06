from packages import click
import json

from actions.config_action import ConfigAction
from actions.change_log_action import ChangeLogAction
from actions.current_version_action import CurrentVersionAction
from actions.next_version_action import NextVersionAction
from actions.bump_action import BumpAction
from version import version as cogit_version

def run_action(action):
    result = action.run()
    if result == None:
        pass
    elif isinstance(result, str):
        click.echo(result)
    else:
        click.echo(json.dumps(result, indent=2, sort_keys=True))

config_option = click.option('--config', default=None,  help='Config file') #type=click.Path(exists=True),

@click.group()
def cli():
    pass

@cli.command()
def version():
    click.echo(f'Co-Git Version {cogit_version}')

@cli.command()
@config_option
def config(config):
    run_action(ConfigAction(config))

@cli.command()
@config_option
def change_log(config):
    run_action(ChangeLogAction(config))

@cli.command()
@config_option
def current_version(config):
    run_action(CurrentVersionAction(config))

@cli.command()
@config_option
def next_version(config):
    run_action(NextVersionAction(config))

@cli.command()
@config_option
@click.argument('version')
def bump(config, version):
    run_action(BumpAction(config, version))

@cli.command()
@config_option
def commit(config):
    pass

    
    # # Type
    # commitType = Menu('Select type', config['types']).show()
    # # Scope
    # commitScope = Menu('Select scope', config['scopes']).show()
    # if commitScope == 'custom':
    #     commitScope = Tb('Input custom scope').show()
    # # Summary
    # commitSummary = Tb('Enter summary').show()
    # # Body
    # commitBody = ''
    # hasBody = Menu('Has body?', {'no': '', 'yes': ''}).show()
    # if hasBody == 'yes':
    #     commitBody = Tb1('Describe commit or leave empty').show()
    # # Breaking changes
    # commitBc = Tb('Describe breaking change or leave empty').show()
    # # Issues
    # commitIssues = Tb('Enter closed issues separated by comma (e.g. "123,234,345") or leave empty').show()
    # # Format
    # commitMessage = formatMessage(commitType, commitScope, commitBc, commitSummary)
    # commitBody = formatBody(commitBody, commitBc, commitIssues) 
    # # Build command
    # commitCmd = ['git', 'commit', '-m', commitMessage]
    # if commitBody != '':
    #     commitCmd.extend(['-m', commitBody])
    # print(commitCmd)
    # process = subprocess.run(['git', 'commit', '-m', commitMessage, '-m', commitBody])


if __name__ == '__main__':
    cli()

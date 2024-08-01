from packages import click
import json
import sys
import context

from src.actions.config_action import ConfigAction
from src.actions.change_log_action import ChangeLogAction
from src.actions.current_version_action import CurrentVersionAction
from src.actions.next_version_action import NextVersionAction
from src.actions.bump_action import BumpAction
from src.actions.debug_convention import DebugConvention
from src.actions.debug_git_messages import DebugGitMessages
from src.actions.debug_git_messages_raw import DebugGitMessagesRaw
from src.actions.debug_git_versions import DebugGitVersions
from src.actions.lint_action import LintAction
from src.actions.lint_enable_action import LintEnableAction
from src.actions.lint_disable_action import LintDisableAction
from src.version import version as cogit_version

def run_action(action):
    result = action.run()
    if result == None:
        pass
    elif isinstance(result, str):
        click.echo(result)
    else:
        click.echo(json.dumps(result, indent=2, sort_keys=True))

config_option = click.option('--config', default=None,  help='Config file') #type=click.Path(exists=True),
limit_option = click.option('--limit', default=0, help='Limit versions output')

@click.group()
def cli():
    pass

# debug

@cli.command()
@config_option
@limit_option
def debug_git_messages(config, limit):
    run_action(DebugGitMessages(config, limit))

@cli.command()
@config_option
@limit_option
def debug_git_messages_raw(config, limit):
    run_action(DebugGitMessagesRaw(config, limit))

@cli.command()
@config_option
@limit_option
def debug_git_versions(config, limit):
    run_action(DebugGitVersions(config, limit))

@cli.command()
@config_option
@limit_option
def debug_convention(config, limit):
    run_action(DebugConvention(config, limit))

# main

@cli.command()
def version():
    click.echo(f'CoGit Version {cogit_version}')

@cli.command()
@config_option
def config(config):
    run_action(ConfigAction(config))

@cli.command()
@config_option
@limit_option
def change_log(config, limit):
    run_action(ChangeLogAction(config, limit))

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

# lint

@cli.command()
@config_option
def lint(config):
    run_action(LintAction(config))

@cli.command()
@config_option
def lint_enable(config):
    run_action(LintEnableAction(config))

@cli.command()
@config_option
def lint_disabe(config):
    run_action(LintDisableAction(config))

# commit

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

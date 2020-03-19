from __future__ import print_function
from cloudmesh.shell.command import command
from cloudmesh.shell.command import PluginCommand
from cloudmesh.common.console import Console
from cloudmesh.common.util import path_expand
from pprint import pprint
from cloudmesh.common.debug import VERBOSE

class LauncherCommand(PluginCommand):

    # noinspection PyUnusedLocal
    @command
    def do_launcher(self, args, arguments):
        """
        ::

          Usage:
                launcher --file=FILE
                launcher list

          This command does some useful things.

          Arguments:
              FILE   a file name

          Options:
              -f      specify the file

        """

        VERBOSE(arguments)


        if arguments.FILE:
            print("option a")

        elif arguments.list:
            print("option b")

        return ""

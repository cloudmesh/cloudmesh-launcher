from cloudmesh.common.util import banner
from cloudmesh.common.console import Console
from cloudmesh.launcher.Config import Config
import sys
from pprint import pprint
import textwrap
import os as _os

# noinspection PyUnusedLocal
class Launcher(Config):
    spec = textwrap.dedent("""
     info:
       name: sample
       version: '0.1'
       filename: None
       kind: launcher
       service: local
     launcher:
       darwin:
         prerequisite:
         - pwd
         install:
         - pwd
         configure:
         - pwd
         run:
         - pwd
       ubuntu:
         prerequisite:
         - pwd
         install:
         - pwd
         configure:
         - pwd
         run:
         - pwd
     """)

    def __init__(self, filename=None, spec=None, **kwargs):
        super().__init__(filename=None, spec=None, **kwargs)


    def _run_step(self, step=None, os=None):
        lines = self[f"launcher.{os}.{step}"]
        if os.lower() in ["darwin", "linux"]:
            for line in lines:
                _os.system(line)
        else:
            raise ValueError(f"OS {os} not supported")


    def run(self, step=None, os=None):
        """
        define a launch and give it the name

        :param name: the unique launch name
        :return:  The dict representing the launch
        """
        if step is None and os:
            banner(f"All steps for `{os}`", c="#")
            steps = self[f"launcher.{os}"].keys()
            print ("S", steps)
            for step in steps:
                self.run(step=step, os=os)

        elif step and os:
            banner(f"Step `{step}` for `{os}`", c="-")

            self._run_step(step=step, os=os)


        if step is None and os is None:
            raise ValueError("Neither os or step defined")


    def check(self, name=None, step=None):
        """
        checks if the step is successful

        :param name:
        :return: The dict representing the launch including updated status
        """
        raise NotImplementedError


    def stop(self, name=None):
        """
        stops the launch with the given name

        :param name:
        :return: The dict representing the launch including updated status
        """
        raise NotImplementedError

    def log(self, name=None):
        """
        returns the log of the launch

        :param name:
        :return:
        """
        raise NotImplementedError
        return ""

    def clean(self, name=None):
        """
        returns the log of the launch

        :param name:
        :return:
        """
        raise NotImplementedError
        return ""

if __name__ == "__main__":

    launcher = Launcher()
    print(launcher)
    pprint(launcher.__dict__)
    pprint(launcher.data)
    pprint(launcher["info"])
    pprint(launcher["info.version"])
    launcher["info.version"] = "0.2"
    pprint(launcher["info.version"])

    # launcher.run()
    launcher.run(os="darwin")

    print(launcher.data)
    print(launcher["launcher.darwin.prerequisite"])

    launcher.run(os="darwin", step="prerequisite")


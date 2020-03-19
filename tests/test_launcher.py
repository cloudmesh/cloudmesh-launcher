###############################################################
# pytest -v --capture=no tests/test_launcher.py
# pytest -v  tests/test_launcher.py
# pytest -v --capture=no  tests/test_launcher..py::Test_launcher::<METHODNAME>
###############################################################
import pytest
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.Benchmark import Benchmark
from cloudmesh.launcher.Launcher import Launcher
from pprint import pprint

Benchmark.debug()

cloud = "local"



@pytest.mark.incremental
class TestLauncher:

    def test_str(self):
        HEADING()

        launcher = Launcher()

        Benchmark.Start()
        spec = str(launcher)
        VERBOSE(spec)

        assert spec.startswith("info:")
        Benchmark.Stop()

    def test_dict(self):
        HEADING()

        launcher = Launcher()

        Benchmark.Start()
        d = type(launcher.__dict__)
        VERBOSE(d)
        assert d == dict
        Benchmark.Stop()

    def test_info(self):
        HEADING()

        launcher = Launcher()

        Benchmark.Start()
        info = launcher["info"]
        VERBOSE(info)
        compare = {'filename': 'None', 'name': 'sample', 'version': '0.1', 'kind': 'launcher', 'service': 'local'}
        assert info == compare
        Benchmark.Stop()


    def test_version(self):
        HEADING()

        launcher = Launcher()

        Benchmark.Start()
        version = launcher["info.version"]
        VERBOSE(version)
        assert version == "0.1"
        Benchmark.Stop()

    def test_version_set(self):
        HEADING()

        launcher = Launcher()

        Benchmark.Start()
        launcher["info.version"] = "0.2"
        version = launcher["info.version"]
        VERBOSE(version)
        assert version == "0.2"
        Benchmark.Stop()

    def test_file(self):
        HEADING()

        a = Launcher()
        b = Launcher()
        Benchmark.Start()
        print (a.data)
        a.write("test.yaml")
        b.read("test.yaml")

        assert str(a) == str(b)

        Benchmark.Stop()

    def test_benchmark(self):
        HEADING()
        #Benchmark.print(csv=True, tag=cloud)

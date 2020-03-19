###############################################################
# pytest -v --capture=no tests/test_config.py
# pytest -v  tests/test_config.py
# pytest -v --capture=no  tests/test_config..py::Test_config::<METHODNAME>
###############################################################
import pytest
from cloudmesh.common.Shell import Shell
from cloudmesh.common.debug import VERBOSE
from cloudmesh.common.util import HEADING
from cloudmesh.common.Benchmark import Benchmark
#from cloudmesh.launcher.Launcher import Launcher
from cloudmesh.launcher.Config import Config
from pprint import pprint

Benchmark.debug()

cloud = "local"



@pytest.mark.incremental
class TestConfig:

    def test_str(self):
        HEADING()

        config = Config()

        Benchmark.Start()
        spec = str(config)
        VERBOSE(spec)

        assert spec.startswith("info:")
        Benchmark.Stop()

    def test_dict(self):
        HEADING()

        config = Config()

        Benchmark.Start()
        d = type(config.__dict__)
        VERBOSE(d)
        assert d == dict
        Benchmark.Stop()

    def test_info(self):
        HEADING()

        config = Config()

        Benchmark.Start()
        info = config["info"]
        VERBOSE(info)
        compare = {'filename': 'None', 'name': 'sample', 'version': '0.1', 'kind': 'launcher', 'service': 'local'}
        assert info == compare
        Benchmark.Stop()


    def test_version(self):
        HEADING()

        config = Config()

        Benchmark.Start()
        version = config["info.version"]
        VERBOSE(version)
        assert version == "0.1"
        Benchmark.Stop()

    def test_version_set(self):
        HEADING()

        config = Config()

        Benchmark.Start()
        config["info.version"] = "0.2"
        version = config["info.version"]
        VERBOSE(version)
        assert version == "0.2"
        Benchmark.Stop()

    def test_file(self):
        HEADING()

        a = Config()
        b = Config()
        Benchmark.Start()
        print (a.data)
        a.write("test.yaml")
        b.read("test.yaml")

        assert str(a) == str(b)

        Benchmark.Stop()

    def test_benchmark(self):
        HEADING()
        #Benchmark.print(csv=True, tag=cloud)

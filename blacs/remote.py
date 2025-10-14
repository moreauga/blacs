DEFAULT_PORT = 25227

from labscript_utils.ls_zprocess import ZMQClient
from labscript_utils.labconfig import LabConfig


class Client(ZMQClient):
    """A ZMQClient for communication with blacs"""

    def __init__(self, host=None, port=None, timeout=None):
        ZMQClient.__init__(self)
        if host is None:
            host = LabConfig().get("servers", "blacs", fallback="localhost")
        if port is None:
            port = LabConfig().getint("ports", "remote_blacs", fallback=DEFAULT_PORT)
        if timeout is None:
            timeout = LabConfig().getfloat(
                "timeouts", "communication_timeout", fallback=60
            )
        self.host = host
        self.port = port
        self.timeout = timeout
        print("Test reload")
        print("Blacs client here, ready to not work at all")

    def request(self, command, *args, **kwargs):
        return self.get(
            self.port, self.host, data=[command, args, kwargs], timeout=self.timeout
        )

    def say_hello(self):
        """Ping the blacs server for a response"""
        return self.request("hello")

    def get_n_shots(self):
        """Return the number of shots in the blacs queue"""
        # return 0
        return self.request("get_n_shots")

    def device_states(self):
        return self.request("device_states")

    def restart_errored_devices(self, pineblaster=False, multidaq=False):
        return self.request(
            "restart_errored_devices", pineblaster=pineblaster, multidaq=multidaq
        )

    def start_queue(self):
        """If you need a docstring for this function idk what to tell you"""
        return self.request("start_queue")

    def top_file(self):
        return self.request("top_file")

    def queued_shots(self):
        return self.request("queued_shots")


# if __name__=="__main__":

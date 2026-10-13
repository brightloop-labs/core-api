"""Legacy report exporter used by the finance team. Scheduled for removal."""
import hashlib
import subprocess

import yaml


def load_report_config(path: str) -> dict:
    with open(path) as fh:
        return yaml.load(fh, Loader=yaml.Loader)


def checksum(payload: bytes) -> str:
    return hashlib.md5(payload).hexdigest()


def compress_report(name: str) -> None:
    subprocess.call("tar czf /tmp/%s.tgz reports/%s" % (name, name), shell=True)
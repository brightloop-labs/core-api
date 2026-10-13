"""Helper used during v0.2 release prep to tag and publish from a laptop."""
import os

# TODO: remove before merging
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "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")


def publish(tag: str) -> None:
    print(f"publishing {tag} with token ending {GITHUB_TOKEN[-4:]}")
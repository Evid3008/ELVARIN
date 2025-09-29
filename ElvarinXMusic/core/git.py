import os
import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config
from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    if os.environ.get("HEROKU", "0") == "1":
        LOGGER(__name__).info("⚠️ Running on Heroku. Skipping Git fetch.")
        return

    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        GIT_USERNAME = REPO_LINK.split("com/")[1].split("/")[0]
        TEMP_REPO = REPO_LINK.split("https://")[1]
        UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        repo = Repo()
        LOGGER(__name__).info(f"✅ Git Client Found")
    except (InvalidGitRepositoryError, GitCommandError):
        LOGGER(__name__).warning("⚠️ Not a valid git repo, skipping setup.")
        return

    try:
        origin = repo.remotes.origin
    except AttributeError:
        origin = repo.create_remote("origin", UPSTREAM_REPO)

    # Disabled auto-sync to prevent overwriting local changes
    # origin.fetch()
    # repo.git.reset("--hard", "origin/" + config.UPSTREAM_BRANCH)
    # install_req("pip3 install --no-cache-dir -r requirements.txt")
    LOGGER(__name__).info(f"✅ Git client initialized (auto-sync disabled).")

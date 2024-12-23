"""Simple, fast and fun task runner, not unlike gulp / grunt (but zero dep)"""

import os
from pathlib import Path
import shlex
import subprocess
import sys
import textwrap


def do_check(_args: list[str]) -> None:
    """typecheck, lint etc goes here"""
    c("python mypy scf_prj")


def do_format(_args: list[str]) -> None:
    """Reformat all code"""
    c(["ruff", "format", "."])


def do_lint(_args: list[str]) -> None:
    """Check with ruff"""
    c(["ruff", "check"])


def do_test(_args: list[str]) -> None:
    os.chdir("test")
    c("pytest")


def default() -> None:
    show_help()


# library functions here (or in own module, whatever, I don't care)

emit = print

def c(
    cmd: list[str | Path] | str, check=True, shell=False, cwd: str | Path | None = None
) -> None:
    """ Run a shell command"""
    cmdtext = shlex.join(str(s) for s in cmd) if isinstance(cmd, list) else cmd
    cwd_text = f"{cwd} " if cwd else ""
    cmdtext = f"{cwd_text}> {cmdtext}"
    emit(cmdtext)
    subprocess.run(cmd, check=check, shell=shell, cwd=cwd)

# scaffolding starts. Do not edit below


def show_help() -> None:
    g = globals()
    emit(
        "Command not found, try",
        sys.argv[0],
        " | ".join([n[3:] for n in g if n.startswith("do_")]),
        "| <command> -h",
    )


def main() -> None:
    """Launcher. Do not modify."""
    if len(sys.argv) < 2:
        default()
        return
    func = sys.argv[1]
    f = globals().get("do_" + func)
    if sys.argv[-1] == "-h":
        emit(
            textwrap.dedent(f.__doc__).strip()
            if f.__doc__
            else "No documentation for this command",
        )
        return
    if not f:
        show_help()
        return
    f(sys.argv[2:])


if __name__ == "__main__":
    main()

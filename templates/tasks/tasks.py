"""Simple, fast and fun task runner, not unlike gulp / grunt (but zero dep)"""

import os
import shutil
import subprocess
import sys
import textwrap

print(sys.executable)


def do_check(args) -> None:
    """typecheck, lint etc goes here"""
    c("python mypy scf_prj")


def do_format(args) -> None:
    """Reformat all code"""
    c(["ruff", "format", "."])


def do_lint(args) -> None:
    """Check with ruff"""
    c(["ruff", "check"])


def do_test(args) -> None:
    os.chdir("test")
    c("pytest")


def default() -> None:
    show_help()


# library functions here (or in own module, whatever, I don't care)

emit = print

def c(cmd, check=True, shell=False, cwd=None) -> None:
    if isinstance(cmd, list):
        cmdtext = " ".join(cmd)
    else:
        cmdtext = cmd
    if cwd is not None:
        cmdtext = f"{cwd} > {cmdtext}"
    emit(">", cmdtext)
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

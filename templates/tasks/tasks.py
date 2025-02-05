"""Simple, fast and fun task runner, not unlike gulp / grunt (but zero dep)"""

import os
from pathlib import Path
import shlex
import subprocess
import sys
import textwrap
from argparse import ArgumentParser, Namespace
import inspect


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


def do_complex(_args: Namespace) -> ArgumentParser | None:
    if _args is None:
        parser = ArgumentParser(description="Complex fn")
        parser.add_argument("--foo", type=int, required=True, help="foo help")
        return parser
    print("Complex fn called with", _args)


def default() -> None:
    show_help()


# library functions here (or in own module, whatever, I don't care)

emit = print


def c(
    cmd: list[str | Path] | str, check=True, shell=False, cwd: str | Path | None = None
) -> None:
    """Run a shell command"""
    cmdtext = shlex.join(str(s) for s in cmd) if isinstance(cmd, list) else cmd
    cwd_text = f"{cwd} " if cwd else ""
    cmdtext = f"{cwd_text}> {cmdtext}"
    emit(cmdtext)
    subprocess.run(cmd, check=check, shell=shell, cwd=cwd)


# scaffolding starts. Do not edit below


def _is_argparse_function(f) -> bool:
    annotations = list(p.annotation for p in inspect.signature(f).parameters.values())
    if len(annotations) == 1 and annotations[0] == Namespace:
        return True
    return False


def _collect_args_from_argparse_function(f) -> ArgumentParser:
    parser = f(None)
    if not isinstance(parser, ArgumentParser):
        raise ValueError(
            "Function taking argparse.Namespace must return ArgumentParser when called with None"
        )
    parser.prog = "python tasks.py " + f.__name__[3:]
    return parser


def show_help() -> None:
    g = globals()
    funcs = [(n[3:], f) for (n, f) in g.items() if n.startswith("do_")]
    funcs.sort()
    emit(
        "Command not found. Try one of these:",
    )
    for name, func in funcs:
        nametext = name + ":"

        if _is_argparse_function(func):
            parser = _collect_args_from_argparse_function(func)
            help_text = parser.format_help()
            emit(nametext)
            emit(textwrap.indent(help_text, " " * 4))
        else:
            emit(f"{nametext:<15} {func.__doc__ or ''}")


def main() -> None:
    """Launcher. Do not modify."""
    if len(sys.argv) < 2:
        default()
        return
    func = sys.argv[1]
    f = globals().get("do_" + func)
    if f:
        if _is_argparse_function(f):
            parser = _collect_args_from_argparse_function(f)
            args = parser.parse_args(sys.argv[2:])
            f(args)
            return
        else:
            f(sys.argv[2:])
            return

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


if __name__ == "__main__":
    main()

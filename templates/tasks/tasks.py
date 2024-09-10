"""Simple, fast and fun task runner, not unlike gulp / grunt (but zero dep)"""

import os
import shutil
import subprocess
import sys
import textwrap

PACKAGE = "scf_prj"


def do_check(args) -> None:
    """typecheck, lint etc goes here"""
    c("mypy scf_prj")


def do_black(args) -> None:
    """Do 'black' reformat of all code"""
    c("py -m black scf_prj")


def do_test(args) -> None:
    os.chdir("test")
    c("pytest")


def default() -> None:
    show_help()


# library functions here (or in own module, whatever, I don't care)

emit = print


def c_spawn(cmd, cwd):
    emit(">", cmd)
    subprocess.Popen(cmd, cwd=cwd, shell=True)


def copy_files(sources, destinations):
    """Copy each source to each destinatios"""
    for src in sources:
        for dest in destinations:
            src = os.path.abspath(src)
            dest = os.path.abspath(dest)
            emit("cp %s -> %s" % (src, dest))
            if not os.path.isdir(dest):
                emit("File not found", dest)
                continue
            shutil.copy(src, dest)


def c(cmd):
    emit(">", cmd)
    subprocess.check_call(cmd, shell=True)


def c_ignore(cmd):
    emit(">", cmd)
    subprocess.call(cmd, shell=True)


def c_dir(cmd, dir):
    emit("%s > %s" % (dir, cmd))
    subprocess.check_call(cmd, cwd=dir, shell=True)


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

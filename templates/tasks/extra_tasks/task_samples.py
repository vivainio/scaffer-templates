from argparse import Namespace, ArgumentParser

# feel free to delete this file, this is just an example on
# - how to declare tasks that use argparse
# - how to add tasks from other modules in addition to tasks.py


def do_complex(_args: Namespace) -> ArgumentParser | None:
    if _args is None:
        parser = ArgumentParser(description="Function with argparse")
        parser.add_argument("--foo", type=int, required=True, help="foo help")
        return parser
    print("Complex fn called with", _args)

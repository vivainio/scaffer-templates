from __future__ import print_function

""" scf_app """

from argparse import ArgumentParser


def declare_foo_cmd(sub):
    p = sub.add_parser("foo", help="Foo subcommand")
    p.add_argument("--bar", action="store_true", help="With bar enabled")

    def do_foo_cmd(args):
        print("Invoking command", args)

    p.set_defaults(func=do_foo_cmd)


def main():
    p = ArgumentParser()
    sub = p.add_subparsers()
    declare_foo_cmd(sub)
    # ... call more declares

    parsed = p.parse_args()
    if "func" in parsed:
        parsed.func(parsed)
    else:
        p.print_usage()


if __name__ == "__main__":
    main()

from argparse import ArgumentParser, Namespace


def get_argparse() -> Namespace:
    parser: ArgumentParser = ArgumentParser(
        # TODO: Add program name
        # TODO: Choose either Computation or Collection
        # TODO: Add program usage
        # TODO: Add program description
        # TODO: Add program epilog
        prog="SSL Metrics PROJECT NAME COMPUTATION/COLLECTION Utility",
        usage="PROGRAM USAGE",
        description="PROGRAM DESCRIPTION",
        epilog="PROGRAM EPILOG",
    )
    parser.add_argument(
        "-i",
        "--input",
        help="The input JSON file that is to be used for graphing",
        type=str,
        required=True,
    )

    return parser.parse_args()


def main() -> None:
    args: Namespace = get_argparse()

    if args.input[-5::] != ".json":
        print("Invalid input file type. Input file must be JSON")
        quit(1)


if __name__ == "__main__":
    main()

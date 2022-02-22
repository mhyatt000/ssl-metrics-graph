'''creates a graph given arguments'''

from argparse import ArgumentParser, Namespace

import pandas as pd
from matplotlib.figure import Figure
from pandas import DataFrame

from args import check_args, get_columns, get_graph_args
from graph_util import SSLGraph, appendID, window


def main() -> None:
    """TODO:
    -i input files.split(',')

    datasets = []
    for item in args.input:
        col = input('what column')
        datasets.append(pd.read_json(item)[col])

    """

    # get args, check, proceed
    args: Namespace = get_graph_args()
    check_args(args)

    inputs = args.inputs
    column_args = get_columns(args)

    """TODO
    load an input
    find all columns which can be graphed from it
    cross the columns off the list
    if no more cols then quit
    """

    for input in inputs:

        quit() if not any(column_args) else None

        df = pd.read_json(input)

        columns = [col for col in column_args if col in df.columns]

        job_args = [args.data, args.best_fit, args.velocity, args.acceleration]
        job_names = ["data", "best_fit", "velocity", "acceleration"]
        jobs = [j for j, i in zip(job_names, job_args) if i]

        # quit()
        for col in columns:

            x, y = window(
                df=df,
                column=col,
                xmin=args.x_min,
                xmax=args.x_max,
                stepper=args.stepper,
            )

            for job in jobs:

                g = SSLGraph(job=job, x=x, y=y, maxdeg=args.maximum_polynomial_degree)

                g.set(
                    column=col,
                    repo=args.repo,
                    stepper=args.stepper,
                    output=args.output,
                )

                g.build()

        [column_args.remove(col) for col in columns]


if __name__ == "__main__":
    main()

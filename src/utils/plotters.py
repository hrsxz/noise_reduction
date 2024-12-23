"""This module contains the functions to plot the data.
"""
import pandas as pd
import plotly.graph_objs as go  # type: ignore
from plotly.subplots import make_subplots  # type: ignore


def plot_traces(
    data: pd.DataFrame,
    title: str = "Traces",
    x_axis_title: str = "x_axis",
    y_axis_title: str = "y_axis",
    plot_columns: list[str] = [],
    width=800,
    height=1200,
    mode="markers",
) -> None:
    """This function plots the traces of the dataframe.

    Args:
        data (pd.DataFrame): The dataframe.
        title (str, optional): The title of the plot. Defaults to "".
        x_axis_title (str, optional): The title of the x axis. Defaults to "x_axis".
        y_axis_title (str, optional): The title of the y axis. Defaults to "y_axis".
        plot_columns (list[str], optional): The list of columns to plot. Defaults to [].

    Returns:
        None
    """
    if plot_columns == []:
        plot_columns = data.columns.to_list()

    fig = make_subplots(rows=len(plot_columns),
                        cols=1,
                        shared_xaxes=True,
                        vertical_spacing=0.1)  # setting the distance between subplots

    traces = []
    for i, column in enumerate(plot_columns):
        trace = go.Scatter(
            x=data.index,
            y=data[column],
            name=column,
            mode=mode,
        )
        traces.append(trace)
        fig.add_trace(traces[i], row=i + 1, col=1)

        # Set axis titles for each subplot
        fig.update_xaxes(title_text=x_axis_title, row=i + 1, col=1)
        fig.update_yaxes(title_text=f"{column}", row=i + 1, col=1)

    fig.update_layout(
        title=title,
        width=width,
        height=height,
        # xaxis={
        #     "title": "Time Step",
        # },
        # yaxis_title='Signal Value'
        margin=dict(
            l=50,  # left margin
            r=50,  # right margin
            t=50,  # top margin
            b=50   # bottom margin
        )
    )

    fig.show()

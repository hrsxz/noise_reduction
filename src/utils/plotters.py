"""This module contains the functions to plot the data.
"""

import numpy as np
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


def show_traces(
    df: pd.DataFrame,
    title: str = "Traces"
):
    fig = go.Figure()
    for index, row in df.iterrows():
        fig.add_trace(go.Scatter(
            x=df.columns,  # columns names as x values
            y=row.values,  # 当前行的值
            mode='lines',  # 绘制线条模式
            name=str(index)  # 使用行索引作为图例名称
        ))
    fig.update_layout(
        title=title
    )
    fig.show()
    
    
def compare_org_reconstructed(input_data, reconstructed_data):
    """_summary_

    Args:
        input_data (_type_): _description_
        reconstructed_data (_type_): _description_
    """
    x = np.arange(140)  # X轴的范围

    # 创建图表
    fig = go.Figure()

    # 添加原始输入数据线条
    fig.add_trace(go.Scatter(
        x=x,
        y=input_data,
        mode='lines',
        name='Input',
        line=dict(color='blue')
    ))

    # 添加重建数据线条
    fig.add_trace(go.Scatter(
        x=x,
        y=reconstructed_data,
        mode='lines',
        name='Reconstruction',
        line=dict(color='red')
    ))

    # 添加误差填充区域
    fig.add_trace(go.Scatter(
        x=np.concatenate([x, x[::-1]]),  # x 和倒序的 x 拼接，形成封闭区域
        y=np.concatenate([input_data, reconstructed_data[::-1]]),
        fill='toself',
        fillcolor='rgba(255, 0, 0, 0.3)',  # 填充颜色
        line=dict(color='rgba(255,255,255,0)'),  # 去除边框线
        name='Error'
    ))

    # 设置图表布局
    fig.update_layout(
        title='Input, Reconstruction, and Error',
        xaxis_title='Index',
        yaxis_title='Value',
        legend=dict(x=1, y=1),
        template='plotly_white'
    )

    # 显示图表
    fig.show()


def plot_overlay_density(data_list, labels, feature_idx, title):
    """
    Use Plotly to plot the overlay density of the data.
    """
    fig = go.Figure()
    for data, label in zip(data_list, labels):
        fig.add_trace(go.Histogram(
            x=data[:, feature_idx],
            histnorm='density',
            name=label,
            opacity=0.7
        ))
    fig.update_layout(
        title=title,
        xaxis_title="Value",
        yaxis_title="Density",
        barmode='overlay',
        template="plotly_white"
    )
    fig.show()
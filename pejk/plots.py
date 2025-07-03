import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import pandas as pd
from pejk.config import COLORS


def plot_barhplot(
    df: pd.DataFrame,
    y: str,
    x: str,
    padding: int = 1,
    labels: bool = True,
    percenteges: bool = False,
) -> plt.Figure:
    """Plot horizontal barplots

    Parameters
    ----------
    df
        data frame with frequencies.
    y
        column with frequencies
    x
        column with categories
    padding, optional
        the distance to the frequency to barplot, by default 10

    Returns
    -------
       plt.Figure
    """
    fig = plt.figure(figsize=(10, 8))
    rects = plt.barh(df[x].tolist(), df[y].tolist(), color=COLORS["dark blue"])
    if labels and not percenteges:
        fig.axes[0].bar_label(rects, padding=padding, fmt=lambda x: int(round(x, 0)))
    if not labels and percenteges:
        fig.axes[0].bar_label(
            rects, padding=padding, fmt=lambda x: f"{int(round(x, 0))}%"
        )
        fig.axes[0].set_xlim(0, 100)
        fig.axes[0].xaxis.set_major_formatter(mtick.PercentFormatter())

    return fig


def plot_barplot(
    df: pd.DataFrame,
    y: str,
    x: str,
    padding: int = 1,
    labels: bool = True,
    percenteges: bool = False,
) -> plt.Figure:
    """Plot barplots

    Parameters
    ----------
    df
        data frame with frequencies
    x
        column with categories
    y
        column with frequencies
    padding, optional
        the distance to the frequency to barplot, by default 10

    Returns
    -------
        plt.Figure
    """
    fig = plt.figure(figsize=(10, 8))
    rects = plt.bar(df[x].tolist(), df[y].tolist(), color=COLORS["dark blue"])
    if labels:
        fig.axes[0].bar_label(rects, padding=padding, fmt=lambda x: int(round(x, 0)))
    if not labels and percenteges:
        fig.axes[0].bar_label(
            rects, padding=padding, fmt=lambda x: f"{int(round(x, 0))}%"
        )
        fig.axes[0].set_ylim(0, 100)
        fig.axes[0].yaxis.set_major_formatter(mtick.PercentFormatter())
    return fig

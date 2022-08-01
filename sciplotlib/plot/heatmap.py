import os

import matplotlib.ticker
import numpy as np
from matplotlib import pyplot as plt

__all__ = ["heatmap"]


def heatmap(data,
            remove_axis=True,
            x_labels="",
            y_labels="",
            color_bar=False,
            color_bar_label="",
            vmin=None,
            vmax=None,
            val_fmt="{x:.2f}",
            spines=False,
            grid=False,
            grid_color="black",
            grid_linewidth=2,
            save_path="./heatmap",
            save_name="heatmap",
            color=None,
            figsize=(6, 4),
            axis_fontsize=10):
    """
    Create a heatmap from a numpy array and two lists of labels.
    :param data: A numpy array of dimension [2, N].
    :param remove_axis: This will remove the axis and bounding box.
    :param x_labels: x labels
    :param y_labels: y labels
    :param grid_linewidth: line width of grid
    :param grid_color: color of grid
    :param grid: plot grid or not
    :param spines: plot spines or not
    :param val_fmt: number format
    :param vmax: data range that the colormap covers
    :param vmin: data range that the colormap covers
    :param color_bar_label: label for color bar
    :param color_bar: show color bar or not
    :param save_path: Save path.
    :param save_name: Save name.
    :param color: A hexadecimal array of colors.
    :param figsize: Width, height in inches.
    :param axis_fontsize: Axis fontsize used when remove_axis is False.
    :return: None
    """
    if color is None:
        color = "YlGn"

    plt.figure(figsize=figsize)
    plt.rcParams["font.family"] = "Times New Roman"
    im = plt.imshow(data, cmap=color, vmin=vmin, vmax=vmax)

    if color_bar is True:
        color_bar = plt.gca().figure.colorbar(im, ax=plt.gca())
        color_bar.ax.set_ylabel(color_bar_label, rotation=-90, va="bottom")
        color_bar.ax.spines[:].set_linewidth(grid_linewidth)

    if isinstance(val_fmt, str):
        val_fmt = matplotlib.ticker.StrMethodFormatter(val_fmt)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            plt.text(j,
                     i,
                     val_fmt(data[i, j], None),
                     ha="center",
                     va="center",
                     color="black")

    # Turn spines off
    plt.gca().spines[:].set_visible(spines)

    pad_inches = 0

    # Create grid.
    if grid is True:
        plt.gca().set_xticks(np.arange(data.shape[1] + 1) - .5, minor=True)
        plt.gca().set_yticks(np.arange(data.shape[0] + 1) - .5, minor=True)
        plt.gca().grid(which="minor",
                       color=grid_color,
                       linewidth=grid_linewidth,
                       fillstyle="full")
        plt.gca().spines[:].set_linewidth(grid_linewidth)
        plt.gca().tick_params(which="minor", bottom=False, left=False)
        pad_inches = 1.0 / 72.0 * grid_linewidth / 2.0

    plt.tight_layout()

    if remove_axis:
        plt.axis('off')
    else:
        plt.xticks(fontsize=axis_fontsize)
        plt.yticks(fontsize=axis_fontsize)
        plt.gca().set_xticks(np.arange(len(x_labels)), labels=x_labels)
        plt.gca().set_yticks(np.arange(len(y_labels)), labels=y_labels)
        plt.setp(plt.gca().get_xticklabels(),
                 rotation=45,
                 ha="right",
                 rotation_mode="anchor")

    os.makedirs(save_path, exist_ok=True)
    plt.savefig(os.path.join(save_path, f"{save_name}.pdf"),
                bbox_inches="tight",
                transparent="True",
                pad_inches=pad_inches)

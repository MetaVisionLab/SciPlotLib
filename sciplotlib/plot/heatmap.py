import os

import matplotlib.ticker
import numpy as np
from matplotlib import pyplot as plt

__all__ = ["heatmap"]


def heatmap(data,
            axis=False,
            spines=False,
            ticks=True,
            x_labels=None,
            y_labels=None,
            color_bar=False,
            color_bar_label="",
            vmin=None,
            vmax=None,
            val_fmt="{x:.2f}",
            grid=False,
            grid_color="black",
            grid_linewidth=2,
            save_path="./heatmap",
            save_name="heatmap",
            color=None,
            figsize=(6, 4),
            axis_fontsize=10,
            val_fontsize=10):
    """
    Create a heatmap from a numpy array and two lists of labels.
    :param data: A numpy array of dimension [2, N].
    :param axis: This will remove the axis and bounding box.
    :param spines: plot spines or not.
    :param ticks: Where show ticks or not.
    :param x_labels: x labels
    :param y_labels: y labels
    :param grid_linewidth: line width of grid
    :param grid_color: color of grid
    :param grid: plot grid or not
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
    :param val_fontsize: The fontsize of the padding value.
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
        color_bar.ax.tick_params(labelsize=axis_fontsize)

    if isinstance(val_fmt, str):
        val_fmt = matplotlib.ticker.StrMethodFormatter(val_fmt)
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            plt.text(j,
                     i,
                     val_fmt(data[i, j], None),
                     ha="center",
                     va="center",
                     color="black",
                     fontsize=val_fontsize)

    # Spines
    plt.gca().spines[:].set_visible(spines)

    if ticks is False:
        plt.gca().tick_params(axis="both",
                              which="major",
                              left=False,
                              bottom=False,
                              labelleft=False,
                              labelbottom=False)

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

    if axis:
        plt.xticks(fontsize=axis_fontsize)
        plt.yticks(fontsize=axis_fontsize)
        if x_labels is not None:
            plt.gca().set_xticks(np.arange(len(x_labels)), labels=x_labels)
        if y_labels is not None:
            plt.gca().set_yticks(np.arange(len(y_labels)), labels=y_labels)
        plt.setp(plt.gca().get_xticklabels(),
                 rotation=45,
                 ha="right",
                 rotation_mode="anchor")
    else:
        plt.axis('off')

    os.makedirs(save_path, exist_ok=True)
    plt.savefig(os.path.join(save_path, f"{save_name}.pdf"),
                bbox_inches="tight",
                transparent="True",
                pad_inches=pad_inches)

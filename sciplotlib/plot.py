import os

import numpy as np
from matplotlib import pyplot as plt

color_map = [
    "#377EB8",
    "#4DAF4A",
    "#984EA3",
    "#E93F3F",
    "#FF7F00",
    "#FFD92F",
    "#A65628",
    "#F781BF",
    "#C2BD2C",
    "#999999",
    "#66C2A5",
    "#8DA0CB",
    "#96A331",
    "#DDB375",
]

marker_map = [
    "o",
    "x",
    "s",
    "*",
    "^",
    "2",
    "d",
    "+",
    "v",
    "<",
    ">",
    "8",
    "1",
    "h",
]


def scatter(data,
            group=None,
            legend_names=None,
            series=None,
            save_path=".",
            save_name="scatter",
            s=5,
            color=None,
            marker=None,
            alpha=0.8,
            markerscale=1,
            loc="lower right",
            figsize=(6, 4),
            remove_axis=True,
            legend_fontsize=15,
            axis_fontsize=10):
    """
    A scatter plot of data with varying marker size and/or color.
    :param data: A numpy array of dimension [2, N].
    :param group: An N-dimensional numpy array indicating that
    data[i] belongs to the group[i]th group.
    :param legend_names: If provided, it will appear on the legend.
    :param series: Extra group, group must not None when group1 is not None.
    :param save_path: Save path.
    :param save_name: Save name.
    :param s: The marker size.
    :param color: A hexadecimal array of colors.
    :param marker: An array of markers.
    :param alpha: The alpha blending value.
    :param markerscale: markerscale for legend.
    :param loc: loc for legend.
    :param figsize: Width, height in inches.
    :param remove_axis: This will remove the axis and bounding box. The
    image cannot be centered without removing the bounding box. If you
    need a bounding box, you can insert it yourself, e.g. place
    includegraphics command into frame command for LaTex.
    :param legend_fontsize: Legend fontsize used when needed.
    :param axis_fontsize: Axis fontsize used when remove_axis is False.
    :return: None
    """
    if color is None:
        color = color_map
    if marker is None:
        marker = marker_map
    plt.figure(figsize=figsize)
    plt.rcParams["font.sans-serif"] = "Times New Roman"
    assert group is not None or group is None and series is None,\
        "group must not None when series is not None."
    if group is None and series is None:
        plt.scatter(data[0],
                    data[1],
                    s=s,
                    c=color[0],
                    marker=marker[0],
                    alpha=alpha,
                    linewidths=0.5)
    elif series is None:
        for i in np.unique(group):
            idx = group == i
            plt.scatter(data[0][idx],
                        data[1][idx],
                        s=s,
                        c=color[i],
                        marker=marker[i],
                        alpha=alpha,
                        linewidths=0.5)
    else:
        for j in np.unique(group):
            for i in np.unique(series):
                idx = (series == i) & (group == j)
                plt.scatter(data[0][idx],
                            data[1][idx],
                            s=s,
                            c=color[i],
                            marker=marker[j],
                            alpha=alpha,
                            linewidths=0.5)
    if legend_names is not None:
        plt.legend(legend_names,
                   loc=loc,
                   fontsize=legend_fontsize,
                   labelspacing=0,
                   handletextpad=0,
                   markerscale=markerscale)
    if remove_axis:
        plt.axis('off')
    else:
        plt.xticks(fontsize=axis_fontsize)
        plt.yticks(fontsize=axis_fontsize)
    os.makedirs(save_path, exist_ok=True)
    plt.savefig(os.path.join(save_path, f"{save_name}.pdf"),
                bbox_inches="tight",
                transparent="True",
                pad_inches=0)

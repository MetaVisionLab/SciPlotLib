import os

import numpy as np
from matplotlib import pyplot as plt

__all__ = ["scatter"]

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
            group_names=None,
            series=None,
            series_names=None,
            save_path="./scatter",
            save_name="scatter",
            s=10,
            color=None,
            marker=None,
            fix_marker=False,
            alpha=0.8,
            linewidths=0.5,
            labelspacing=0,
            handletextpad=0.2,
            handlelength=0.4,
            borderpad=0.2,
            markerscale=1,
            fancybox=True,
            framealpha=0.5,
            loc="lower right",
            loc_series="upper left",
            figsize=(6, 4),
            remove_axis=True,
            legend_fontsize=15,
            axis_fontsize=10):
    """
    A scatter plot of data with varying marker size and/or color.
    :param data: A numpy array of dimension [2, N].
    :param group: An N-dimensional int numpy array indicating that
    data[i] belongs to the group[i]th group.
    :param group_names: If provided, it will appear on the legend.
    :param series: Series, group must not None when series is not None.
    :param series_names: If provided, it will appear on the legend.
    :param save_path: Save path.
    :param save_name: Save name.
    :param s: The marker size.
    :param color: A hexadecimal array of colors.
    :param marker: An array of markers.
    :param fix_marker: If provided, all scatters will use marker[0].
    :param alpha: The alpha blending value.
    :param linewidths:
    :param labelspacing:
    :param handletextpad:
    :param handlelength:
    :param borderpad:
    :param markerscale: markerscale for legend.
    :param fancybox:
    :param framealpha:
    :param loc: loc for group legend.
    :param loc_series: loc for series legend.
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
    assert series is None or group is not None, \
        "group must not None when series is not None."
    assert group is None or group.dtype == "int64", \
        "group must be int64 numpy array."
    assert series is None or series.dtype == "int64", \
        "series must be int64 numpy array."
    if group is not None and group_names is not None:
        assert len(group_names) == len(np.unique(group)), \
            "The length of group_names does not match group."
    if series is not None and series_names is not None:
        assert len(series_names) == len(np.unique(series)), \
            "The length of series_names does not match series."

    plt.figure(figsize=figsize)
    plt.rcParams["font.family"] = "Times New Roman"
    handles_group = []
    handles_series = []
    if group is None and series is None:
        handle = plt.scatter(data[0],
                             data[1],
                             s=s,
                             c=color[0],
                             marker=marker[0],
                             alpha=alpha,
                             linewidths=linewidths)
        handles_group.append(handle)
    elif series is None:
        for i in np.unique(group):
            idx = group == i
            handle = plt.scatter(data[0][idx],
                                 data[1][idx],
                                 s=s,
                                 c=color[i],
                                 marker=marker[0] if fix_marker else marker[i],
                                 alpha=alpha,
                                 linewidths=linewidths)
            handles_group.append(handle)
    else:
        for j in np.unique(group):
            for i in np.unique(series):
                idx = (series == i) & (group == j)
                handle = plt.scatter(
                    data[0][idx],
                    data[1][idx],
                    s=s,
                    c=color[i],
                    marker=marker[0] if fix_marker else marker[j],
                    alpha=alpha,
                    linewidths=linewidths)
                handles_series.append(handle)
                if i == 0:
                    handles_group.append(handle)

    if group_names is not None:
        legend_group = plt.legend(handles=handles_group,
                                  labels=group_names,
                                  loc=loc,
                                  fontsize=legend_fontsize,
                                  labelspacing=labelspacing,
                                  handletextpad=handletextpad,
                                  handlelength=handlelength,
                                  borderpad=borderpad,
                                  markerscale=markerscale,
                                  fancybox=fancybox,
                                  framealpha=framealpha)
        for lh in legend_group.legendHandles:
            lh.set_alpha(alpha)
        plt.gca().add_artist(legend_group)
    if series_names is not None:
        legend_series = plt.legend(handles=handles_series,
                                   labels=series_names,
                                   loc=loc_series,
                                   fontsize=legend_fontsize,
                                   labelspacing=labelspacing,
                                   handletextpad=handletextpad,
                                   handlelength=handlelength,
                                   borderpad=borderpad,
                                   markerscale=markerscale,
                                   fancybox=fancybox,
                                   framealpha=framealpha)
        for lh in legend_series.legendHandles:
            lh.set_alpha(alpha)
        plt.gca().add_artist(legend_series)
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

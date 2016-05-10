# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:54:08 2015

@author: craigmoodie
"""
import os.path
import pylab as plt
from matplotlib.gridspec import GridSpec
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.image as mimage


def generate_report(output_file, first_plot, second_plot, third_plot,
                    fifth_plot, sixth_plot, seventh_plot):

    plots = ["output_file", "first_plot", "second_plot", "third_plot",
             "fifth_plot", "sixth_plot", "seventh_plot"]
    error_image = "some/path/"
    error = mimage.imread(error_image)
    report = PdfPages(output_file)
    fig = plt.figure()
    grid = GridSpec(4, 3)

    plot_iterator = iter(plots)
    for i in range(0, 3):
        for j in range(0, 4):
            plot = plot_iterator.next()
            if plot is None:
                plot = error
            img = mimage.imread(plot)
            ax = plt.subplot(grid[j, i])
            ax.imshow(img)
            ax.set_aspect('auto')
            for item in ([ax.title, ax.xaxis.label, ax.yaxis.label] +
                         ax.get_xticklabels() + ax.get_yticklabels()):
                item.set_fontsize(8)

            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

    fig.subplots_adjust(wspace=0.02, hspace=.2)

    report.savefig(fig, dpi=300)
    report.close()

    return os.path.abspath(output_file)

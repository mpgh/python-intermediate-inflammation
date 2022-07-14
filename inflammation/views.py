"""Module containing code for plotting inflammation data."""

from matplotlib import pyplot as plt
from . import serializers
import numpy as np


def save_serialized_patient_records(patient):
    """Save serialized data for all patient."""
    output_file = 'test_patient.json'
    serializers.PatientJSONSerializer.save([patient], output_file)
    #tbd

def display_patient_record(patient):
    """Display data for a single patient."""
    print(patient.name)
    for obs in patient.observations:
        print(obs.day, obs.value)


def visualize(data_dict, save = False):
    """Display plots of basic statistical properties of the inflammation data.

    :param data_dict: Dictionary of name -> data to plot
    """
    # TODO(lesson-design) Extend to allow saving figure to file

    num_plots = len(data_dict)
    fig = plt.figure(figsize=((3 * num_plots) + 1, 3.0))

    for i, (name, data) in enumerate(data_dict.items()):
        axes = fig.add_subplot(1, num_plots, i + 1)

        axes.set_ylabel(name)
        axes.plot(data)

    fig.tight_layout()
    if save:
        plt.savefig('output.png')
    else:
        plt.show()

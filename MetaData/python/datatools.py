'''

Various functions for getting information about the data samples defined in
datadefs.py

Author: Evan K. Friis, UW Madison

'''

from datadefs import datadefs

def find_data_for_run(run, primds):
    '''
    Get the appropriate dataset alias for a given run.
    This depends on the valid run ranges specified for each dataset.
    '''
    matching_datasets = []
    for dataset, dataset_info in datadefs.iteritems():
        if primds in dataset_info['datasetpath']:
            if run == 1 or (run >= dataset_info['firstRun'] and
                            run <= dataset_info['lastRun']):
                matching_datasets.append(dataset)

    if len(matching_datasets) != 1:
        raise ValueError("0 or multiple matching datasets found! %s"
                         % matching_datasets)
    return matching_datasets[0]

def map_data_to_dataset(data):
    '''
    Get the DBS name given the data nice name
    '''
    return datadefs[data]['datasetpath']

#!/usr/bin/env python
'''

Dump the measured fake rates to stdout

Author: Evan K. Friis, UW

'''

from RecoLuminosity.LumiDB import argparse
import glob
import json
import logging
import sys
import os

args = sys.argv[:]
sys.argv = [sys.argv[0]]

import rootpy.io as io
from rootpy.plotting import views
from fit_fake_rates import make_path_mangler
import FinalStateAnalysis.PatTools.data_views as data_views
from FinalStateAnalysis.StatTools.efficiencies import efficiency

log = logging.getLogger("dump_fake_rates")
logging.basicConfig(level=logging.DEBUG)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('meta', help='File with meta information')
    parser.add_argument('cfg', help='Configuration python file')
    parser.add_argument('files', metavar='file', nargs='+',
                        help = 'Histogram files')
    args = parser.parse_args(args[1:])

    meta_info = None
    with open(args.meta) as meta_file:
        meta_info = json.load(meta_file)

    log.info("Importing configuration")
    cfg = __import__(args.cfg.replace('.py', ''))

    log.info("Building views")
    data_views = data_views.data_views( args.files, cfg.data_sample)

    # We just need to figure out the directory structure from any old file
    layout_filename = data_views.values()[0]['subsamples'].values()[0]['filename']
    log.info("Getting file layout from %s", layout_filename)

    keys_to_plot = []

    with io.open(layout_filename, 'r') as layout_file:
        for path, subdirs, histos in layout_file.walk(class_pattern='TH1F'):
            # Skip folders w/o histograms
            if not histos:
                continue
            for histo in histos:
                key = [
                    x for x in path.split('/')
                    if x != 'all' and x != 'pass' ] + [ histo ]
                keys_to_plot.append(tuple(key))

    for key in keys_to_plot:
        path = os.path.join(*key)
        sys.stdout.write("Fake rates for %s\n" % path)
        for sample, sample_info in data_views.iteritems():
            num_view = views.PathModifierView(
                sample_info['unweighted_view'], make_path_mangler('pass'))
            all_view = views.PathModifierView(
                sample_info['unweighted_view'], make_path_mangler('all'))
            num_entries = num_view.Get(path).Integral()
            all_entries = all_view.Get(path).Integral()

            eff, eff_down, eff_up = 0, 0, 0
            if all_entries:
                eff, eff_down, eff_up = efficiency(num_entries, all_entries)
                eff, eff_down, eff_up = (eff*100, 100*eff_down, 100*eff_up)

            sys.stdout.write("%s: %i/%i = %0.2f%% +%0.2f -%0.2f\n" % (
                sample, num_entries, all_entries,
                eff, eff_up, eff_down))


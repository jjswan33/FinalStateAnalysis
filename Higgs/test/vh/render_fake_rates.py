#!/usr/bin/env python
'''

Render the measured and fitted fake rates from a RooWorkspace

Author: Evan K. Friis, UW

'''


import atexit
from RecoLuminosity.LumiDB import argparse
import logging
import math
import os
import re
import sys
# Need to generate dictionaries
import FinalStateAnalysis.Utilities.styling as styling
import FinalStateAnalysis.Utilities.RooFitTools as roofit
# Steal the args so ROOT doesn't mess them up!
parser = argparse.ArgumentParser()
args = sys.argv[:]
sys.argv = []

import rootpy.io as io
import ROOT

log = logging.getLogger("render_fake_rates")
logging.basicConfig(level=logging.DEBUG)

def load_fit_result(fit_result, ws):
    ''' Load the fit result values into the appropriate variables '''
    for var in roofit.iter_collection(ws.allVars()):
        name = var.GetName()
        if fit_result.floatParsFinal().find(name):
            value = fit_result.floatParsFinal().find(name).getVal()
            if math.isnan(value):
                log.error("Var %s is NAN - returning false!", name)
                return False
            var.setVal(value)
            log.info("Setting var %s to %f", name, value)
    return True

if __name__ == "__main__":

    parser.add_argument('input', help='Input file w/ fit results RooWorkspace')
    parser.add_argument('output', help='Output directory to store plots in')

    args = parser.parse_args(args[1:])

    log.info("Opening input file %s", args.input)

    file = io.open(args.input, 'r')
    # Always close the file before exiting, otherwise RooPlot will segfault
    atexit.register(file.Close)

    log.info("Getting workspace")
    ws = file.Get("fit_results")

    x = ws.var('x')
    cut = ws.cat('cut')

    # Put everything in python form
    data = {}
    fake_rate_datas = ws.allData()
    # Plot the results of each one
    for datum in fake_rate_datas:
        data[datum.GetName()] = datum
        print datum

    functions = {}
    log.info("Loading functions")
    # We need to unmangle the function names
    name_extractor = re.compile('func_(?P<name>.*)')
    for function in roofit.iter_collection(ws.allFunctions()):
        function_name = function.GetName()
        log.info("Found function: %s", function_name)
        match = name_extractor.match(function_name)
        if not match:
            log.warning("Can't find name for function, skipping!")
            continue
        functions[match.group('name')] = function
        log.info("Added function with name %s", match.group('name'))

    canvas = ROOT.TCanvas("basdf", "aasdf", 800, 600)

    keeps = []
    frame = x.frame()
    # Keep track of output files we write
    output_files = []
    for data_name, data_info in data.iteritems():
        log.info("Making %s plot", data_name)
        frame = x.frame()
        frame.GetYaxis().SetTitle("Fake rate")
        frame.GetXaxis().SetTitle("p_{T}")
        result = ws.genobj('result_' + data_name)
        fit_ok = load_fit_result(result, ws)
        if fit_ok:
            function.plotOn(frame, ROOT.RooFit.LineColor(ROOT.EColor.kBlack),
                            ROOT.RooFit.VisualizeError(result, 1.0),
                            ROOT.RooFit.FillColor(styling.colors['ewk_yellow'].code),
                            ROOT.RooFit.PrintEvalErrors(-1),
                           )
            function.plotOn(frame, ROOT.RooFit.LineColor(ROOT.EColor.kRed),
                            ROOT.RooFit.LineStyle(2),
                            ROOT.RooFit.PrintEvalErrors(-1),
                           )
        data_info.plotOn(frame, ROOT.RooFit.Efficiency(cut))
        frame.Draw()
        canvas.SetLogy(True)
        frame.SetMinimum(1e-3)
        frame.SetMaximum(1)
        output_files.append(os.path.abspath(
            os.path.join(args.output, data_name + '.pdf')))

        canvas.SaveAs(os.path.join(args.output, data_name + '.pdf'))

    # Touch a "dummy" txt file file so Make knows what's up.
    # Write the list of files we just wrote.
    dummy_file = open(os.path.join(args.output, 'plot_list.txt'), 'w')
    for output_file in output_files:
        dummy_file.write(output_file + '\n')


#!/usr/bin/env python

import ROOT
from rootpy.utils import asrootpy
from rootpy.plotting import Canvas, Legend, HistStack
from FinalStateAnalysis.Utilities.AnalysisPlotter import styling,samplestyles
import rootpy.io as io
import FinalStateAnalysis.StatTools.poisson as poisson

# This stuff is just so we can get matching styles as analysis.py
import FinalStateAnalysis.PatTools.data as data_tool
int_lumi = 5000
skips = ['DoubleEl', 'EM']
samples, plotter = data_tool.build_data(
    'VH',  '2012-04-14-v1-WHAnalyze', 'scratch_results',
    int_lumi, skips, count='emt/skimCounter')

# Get stupid templates to build the styles automatically
signal = asrootpy(plotter.get_histogram(
    'VH120',
    'emt/skimCounter',
).th1)

wz = asrootpy(plotter.get_histogram(
    'WZ',
    'emt/skimCounter',
).th1)

zz = asrootpy(plotter.get_histogram(
    'ZZ',
    'emt/skimCounter',
).th1)

fakes_myhist = asrootpy(plotter.get_histogram(
    'Zjets',
    'emt/skimCounter',
))
styling.apply_style(fakes_myhist, **samplestyles.SAMPLE_STYLES['ztt'])

fakes = asrootpy(fakes_myhist.th1)

data = asrootpy(plotter.get_histogram(
    'data_DoubleMu',
    'emt/skimCounter',
).th1)


canvas = Canvas(800, 800)

legend = ROOT.TLegend(0.6, 0.65, 0.9, 0.90, "", "brNDC")
legend.SetFillStyle(0)
legend.SetBorderSize(0)

data.SetMarkerSize(2)
data.SetTitle("data")
data.SetLineWidth(2)
legend.AddEntry(data,  "data", "lp")
signal.SetLineStyle(1)
signal.SetLineWidth(3)
signal.SetTitle("m_{H}=120 (#times 5)")
signal.SetLineColor(ROOT.EColor.kRed)
signal.SetFillStyle(0)
wz.SetTitle('WZ')
zz.SetTitle('ZZ')
fakes.SetTitle("fake bkg.")
legend.AddEntry(signal, signal.GetTitle(), "l")
legend.AddEntry(wz, 'WZ', 'lf')
legend.AddEntry(zz, 'ZZ', 'lf')
legend.AddEntry(fakes,  'fake bkg.', "lf")

whtt_file = io.open('../vhtt_shapes.root')

def get_total(histo):
    return whtt_file.Get('mmt_mumu_final_MuTauMass/%s' % histo) +  \
            whtt_file.Get('emt_emu_final_SubleadingMass/%s' % histo)

hWZ   = get_total('WZ')
hZZ   = get_total('ZZ')
hZJets   = get_total('fakes')
hData = get_total('data_obs')
hSignal = get_total('VH120') + get_total('VH120WW')
hHWW   = hSignal

canvas.cd()

hHWW = hHWW*5.0

hZZ.decorate(zz)
hWZ.decorate(wz)
hZJets.decorate(fakes)
hData.decorate(data)
hHWW.decorate(signal)
hHWW.SetLineWidth(2)

for hist in [hZZ, hZJets, hWZ]:
    hist.format = 'hist'

for hist in [hZZ, hZJets, hData]:
    pass
    #hist.Rebin(5)

hData_poisson = poisson.convert(hData, x_err=False, set_zero_bins=-100)
hData_poisson.SetMarkerSize(2)

stack = HistStack()
stack.Add(hZJets)
stack.Add(hWZ)
stack.Add(hZZ)

stack.Draw()
print stack
stack.GetXaxis().SetTitle("Visible Mass [GeV]")
bin_width = stack.GetXaxis().GetBinWidth(1)
stack.GetYaxis().SetTitle("Events/%0.0f GeV" % bin_width)
stack.GetYaxis().SetTitleOffset(0.8)
stack.SetMinimum(1e-1)
stack.SetMaximum(10)
hHWW.Draw('same,hist')
hData_poisson.Draw('p0')

cms_label = styling.cms_preliminary(5000, is_preliminary=False,
                                    lumi_on_top=True)
#canvas.SetLogy(True)
legend.Draw()

canvas.Update()
canvas.SaveAs('whtt_result.pdf')

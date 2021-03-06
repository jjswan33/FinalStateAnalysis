#!/usr/bin/env python

import os
import ROOT
from FinalStateAnalysis.TMegaSelector.megaselect import TMegaPySelector

proof = ROOT.TProof.Open('workers=4')
proof.SetParameter( "PROOF_UseTreeCache",  1 )
proof.Exec('gSystem->Load("$CMSSW_BASE/lib/$SCRAM_ARCH/libFinalStateAnalysisTMegaSelector.so")')

chain = ROOT.TChain("TestTree")
# test_file.root can be generated by the CPP unit test
chain.Add('test_file.root')
print "Got tree with %i entries" % chain.GetEntries()

dataset = ROOT.TDSet("doot", "TestTree", "/", "TTree")
dataset.Add('file:test_file.root')

cwd = os.getcwd()
if cwd not in os.environ.get('PYTHONPATH', ''):
    os.environ['PYTHONPATH'] = cwd + ':' + os.environ.get('PYTHONPATH', '')

print "Analyze dataset using TDSet"
dataset.Process("TMegaPySelector", "TestSelector")

results = proof.GetOutputList()
for x in results:
    print x

print results.FindObject("adsf").GetMean()

print "Done"

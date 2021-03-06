'''

Algorithms to identify jets coming from PU.

See: https://twiki.cern.ch/twiki/bin/view/CMS/PileupJetID

NB that you must change the "jets" input tag for puJetId and puJetMVA
to point to the correct collection!

External sequence name: puJetIdSequence

The embedded pat::Jets are produced w/ label: patJetsPUID

'''

import FWCore.ParameterSet.Config as cms

from CMGTools.External.pujetidsequence_cff import \
        puJetIdSqeuence, puJetId, puJetMva # sic

# Module to embed the IDs
patJetsPUID = cms.EDProducer(
    "PATJetPUIDEmbedder",
    src = cms.InputTag('fixme'),
    discriminants = cms.VInputTag(
        cms.InputTag("puJetMva", "fullDiscriminant"),
        cms.InputTag("puJetMva", "philv1Discriminant"),
        cms.InputTag("puJetMva", "simpleDiscriminant"),
    ),
    ids = cms.VInputTag(
        cms.InputTag("puJetMva", "fullId"),
        cms.InputTag("puJetMva", "philv1Id"),
        cms.InputTag("puJetMva", "simpleId"),
    )
)

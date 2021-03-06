import math

# Conversions to pico barns
_millibarns = 1.0e+9
_microbarns = 1.0e+6
_nanobarns  = 1.0e+3
_picobarns =  1.0
_femtobarns = 1.0e-3

def quad(*xs):
    # Add stuff in quadrature
    return math.sqrt(sum(x*x for x in xs))

# NB the data samples are built automatically at the bottom

data_name_map = {
    # Fixme there is some double counting here!
    #'Zjets' : ['Zjets_M50', 'Zbb_M50', 'Zcc_M40'],
    'Zjets' : ['Zjets_M50',],

    'QCDMu' : ['QCD_20toInf_MuPt15'],

    #'QCDE' : ['QCD_20to30_EM', 'QCD_30to80_EM', 'QCD_80to170_EM'],

    'Wjets' : ['WplusJets_madgraph'],

    'WW' : ['WWJetsTo2L2Nu'],
    'WZ' : ['WZJetsTo3LNu'],
    'WZ_pythia' : ['WZJetsTo3LNu_pythia'],
    'ZZ' : ['ZZJetsTo4L_pythia'],

    'ttjets': ['TTplusJets_madgraph'],

    'VGamma': ['VGjets'],

    'VH100' : ['VH_100'],
    'VH110' : ['VH_110'],
    'VH115' : ['VH_115'],
    'VH120' : ['VH_120'],
    'VH125' : ['VH_125'],
    'VH130' : ['VH_130'],
    'VH135' : ['VH_135'],
    'VH140' : ['VH_140'],
    'VH145' : ['VH_145'],
    'VH150' : ['VH_150'],
    'VH160' : ['VH_160'],

    'VH110WW' : ['WH_110_HWW3l'],
    'VH115WW' : ['WH_115_HWW3l'],
    'VH120WW' : ['WH_120_HWW3l'],
    'VH125WW' : ['WH_125_HWW3l'],
    'VH130WW' : ['WH_130_HWW3l'],
    'VH135WW' : ['WH_135_HWW3l'],
    'VH140WW' : ['WH_140_HWW3l'],
    'VH145WW' : ['WH_145_HWW3l'],
    'VH150WW' : ['WH_150_HWW3l'],
    'VH155WW' : ['WH_155_HWW3l'],
    'VH160WW' : ['WH_160_HWW3l'],

    'TTW' : ['TTWToLplus', 'TTWToLminus'],
    'TTZ' : ['TTZToLplus', 'TTZToLminus'],
    'WWW' : ['WWWTo2Lplus', 'WWWTo2Lminus'],

    'ggH_ZZ_4l_120' : ['ggH_ZZ_4l_120'],
}

# Some constants
br_w_leptons =  0.1075+0.1057+0.1125
br_www_all_leptons = br_w_leptons*br_w_leptons*br_w_leptons

datadefs = {
    ############################################################################
    #### EWK background datasets            ####################################
    ############################################################################

    'Zjets_M50' : {
        'datasetpath' : '/DYJetsToLL_TuneZ2_M-50_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : 3048*_picobarns, #NNLO
        'pu' : 'S6',
        'analyses' : ['HTT', 'SSDL', 'VH', 'Tau', 'Mu'],
    },
    'WplusJets_madgraph' : {
        'datasetpath' : "/WJetsToLNu_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 31314*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT', 'SSDL', 'VH', 'Tau', 'Mu'],
    },
    'TTplusJets_madgraph' : {
        'datasetpath' : "/TTJets_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 157.5*_picobarns, # NLO cross-section from https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSections
        'pu' : 'S6',
        'analyses' : ['HTT', 'SSDL', 'VH', 'Tau', 'Mu'],
    },
    'T_tW_Powheg' : {
        'datasetpath' : "/T_TuneZ2_tW-channel-DS_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 10.6*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'T_t_Powheg' : {
        'datasetpath' : "/T_TuneZ2_t-channel_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 64.6*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'T_s_Powheg' : {
        'datasetpath' : "/T_TuneZ2_s-channel_7TeV-powheg-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 4.21*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'Wplus3Jets_madgraph' : {
        'datasetpath' : "/W3Jets_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 304.2*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },


    ############################################################################
    #### VGamma background datasets         ####################################
    ############################################################################
    'VGjets' : {
        'datasetpath' : '/GVJets_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : 56.64*_picobarns,
        'pu' : 'S6',
        'analyses' : ['Mu', 'VH'],
    },

    ############################################################################
    #### Diboson datasets                   ####################################
    ############################################################################

    'ZZJetsTo4L' : {
        'datasetpath' : "/ZZJetsTo4L_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        #'x_sec' : 0.03906*_picobarns,
        # 3.8 +- 1.5 0.2 0.2 from EWK-11-10
        'x_sec' : 3.8*_picobarns*0.1096*0.1096,
        'x_sec_unc' : quad(1.5, 0.2, 0.2)*0.1096*0.1096,
        'analyses' : ['VH', 'SSDL'],
    },

    'ZZJetsTo4L_pythia' : {
        'datasetpath' : "/ZZTo4L_TuneZ2_7TeV_pythia6_tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : 0.106*_picobarns, # from MCFM via Ian
        'x_sec_unc' : quad(1.5, 0.2, 0.2)*0.1096*0.1096,
        'analyses' : ['VH', 'SSDL', '4L', 'HTT'],
    },
    'WZJetsTo3LNu' : {
        'datasetpath' : "/WZJetsTo3LNu_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : 26.735*_picobarns*3*0.03365*(0.1075+0.1057+0.1125) ,
        'x_sec_unc' : quad(2.4, 1.1, 1.0)*0.3257*0.1096,
        'analyses' : ['VH', 'SSDL'],
    },
    'WZJetsTo2L2Q' : {
        'datasetpath' : "/WZJetsTo2L2Q_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : 3.85*_picobarns ,
        'analyses' : ['HTT'],
    },
    'WZJetsTo3LNu_pythia' : {
        'datasetpath' : "/WZTo3LNu_TuneZ2_7TeV_pythia6_tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        # This xsec comes from PREP and is only LO.  Different from the PREP
        # value for the madgraph sample, as Pythia does not include gamma*
        'x_sec' : 0.33*_picobarns, # FIXME !!!!!!!!
        'x_sec_unc' : quad(2.4, 1.1, 1.0)*0.3257*0.1096,
        'analyses' : ['VH', 'SSDL', 'HTT'],
    },
    'WWJetsTo2L2Nu' : {
        'datasetpath' : '/WWJetsTo2L2Nu_TuneZ2_7TeV-madgraph-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'pu' : 'S6',
        #'x_sec' : 3.783*_picobarns, # FROM PREP
        # 55.3 +- 3.3 6.9 3.3 from EWK-11-10
        'x_sec' : 55.3*_picobarns*0.3257*0.3257, # 32.57% BR to leptons
        'x_sec_unc' : quad(3.3, 6.9, 3.3)*0.3257*0.3257,
        'analyses' : ['VH', 'SSDL'],
    },

    ############################################################################
    #### QCD datasets                       ####################################
    ############################################################################

    'QCD_20toInf_MuPt15' : {
        'datasetpath' : '/QCD_Pt-20_MuEnrichedPt-15_TuneZ2_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'pu' : 'S6',
        'x_sec' : 2.966E8*_picobarns*2.855E-4,
        'analyses' : ['HTT', 'VH', 'Tau', 'Mu'],
    },

    ############################################################################
    #### Signal datasets                    ####################################
    ############################################################################

    'VH_100' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : (1.186 + 0.6313 + 0.1638)*_picobarns*8.36e-2,
        'skim' : 1.0,
        'analyses' : ['VH', 'HTT'],
    },
    'VH_110' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-110_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : (0.8754 + 0.4721 + 0.1257)*_picobarns*8.02e-2,
        'skim' : 1.0,
        'analyses' : ['VH', 'HTT'],
    },
    'VH_115' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-115_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : (0.7546 + 0.4107 + 0.1106)*_picobarns*7.65e-2,
        'skim' : 1.0,
        'analyses' : ['VH', 'HTT'],
    },
    'VH_120' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-120_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'pu' : 'S6',
        'x_sec' : (0.6561 + 0.3598 + 0.09756)*_picobarns*7.1e-2,
        'skim' : 1.0,
        'analyses' : ['VH', 'HTT'],
    },
    'VH_125' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-125_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.6729 + 0.3158 + 0.08634)*_picobarns*6.37e-2,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },
    'VH_130' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-130_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.5008 + 0.2778 + 0.07658)*_picobarns*5.48e-2,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },
    'VH_135' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-135_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.4390 + 0.2453 + 0.06810)*_picobarns*4.52e-2,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },
    'VH_140' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-140_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.3857 + 0.2172 + 0.06072)*_picobarns*3.54e-2,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },
    'VH_145' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-145_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.3406 + 0.1930 + 0.05435)*_picobarns*2.61e-2,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },
    'VH_150' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-150_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.3001 + 0.1713 + 0.04869)*_picobarns*1.78e-2,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },
    'VH_160' : {
        'datasetpath' :"/WH_ZH_TTH_HToTauTau_M-160_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.2291 + 0.1334 + 0.03942)*_picobarns*3.96E-03,
        'pu' : 'S6',
        'analyses' : ['VH', 'HTT'],
    },

    ############################################################################
    #### VH -> WW dataset                   ####################################
    ############################################################################

    'VH_120_HWW' : {
        'datasetpath' :"/WH_ZH_TTH_HToWW_M-120_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.6561 + 0.3598 + 0.09756)*_picobarns*1.43E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'VH_130_HWW' : {
        'datasetpath' :"/WH_ZH_TTH_HToWW_M-130_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.5008 + 0.2778 + 0.07658)*_picobarns*3.05E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'VH_135_HWW' : {
        'datasetpath' :"/WH_ZH_TTH_HToWW_M-135_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM	",
        'x_sec' : (0.4390 + 0.2453 + 0.06810)*_picobarns*4.03E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'VH_140_HWW' : {
        'datasetpath' :"/WH_ZH_TTH_HToWW_M-140_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.3857 + 0.2172 + 0.06072)*_picobarns*5.03E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'VH_150_HWW' : {
        'datasetpath' :"/WH_ZH_TTH_HToWW_M-150_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM	",
        'x_sec' : (0.3001 + 0.1713 + 0.04869)*_picobarns*6.98E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'VH_160_HWW' : {
        'datasetpath' :"/WH_ZH_TTH_HToWW_M-160_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM	",
        'x_sec' : (0.2291 + 0.1334 + 0.03942)*_picobarns*9.08E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'WH_110_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-110_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.8754*_picobarns*br_www_all_leptons*4.82E-02,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_115_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-115_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.7546*_picobarns*br_www_all_leptons*8.67E-02,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_120_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-120_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.6561*_picobarns*br_www_all_leptons*1.43E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_125_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-125_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.5729*_picobarns*br_www_all_leptons*2.16E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_130_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-130_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.5008*_picobarns*br_www_all_leptons*3.05E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_135_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-135_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.4390*_picobarns*br_www_all_leptons*4.03E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_140_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-140_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.3857*_picobarns*br_www_all_leptons*5.03E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_145_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-145_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.3406*_picobarns*br_www_all_leptons*6.02E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_150_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-150_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.3001*_picobarns*br_www_all_leptons*6.98E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_155_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-155_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.2646*_picobarns*br_www_all_leptons*7.95E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },
    'WH_160_HWW3l' : {
        'datasetpath' : "/WH_HToWW_3l_M-160_7TeV-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 0.2291*_picobarns*br_www_all_leptons*9.08E-01,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    ############################################################################
    #### ZH private production              ####################################
    ############################################################################

    'ZH_110_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-110-7TeV-pythia6/friis-RECO_crab_reco_TT_110-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.4721*_picobarns*8.02e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_115_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-115-7TeV-pythia6/friis-RECO_crab_reco_TT_115-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.4107*_picobarns*7.65e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_120_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-120-7TeV-pythia6/friis-RECO_crab_reco_TT_120-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.3598*_picobarns*7.1e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_125_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-125-7TeV-pythia6/friis-RECO_crab_reco_TT_125-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.3158*_picobarns*6.37e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_130_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-130-7TeV-pythia6/friis-RECO_crab_reco_TT_130-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.2778*_picobarns*5.48e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_135_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-135-7TeV-pythia6/friis-RECO_crab_reco_TT_135-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.2453*_picobarns*4.52e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_140_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-140-7TeV-pythia6/friis-RECO_crab_reco_TT_140-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.2172*_picobarns*3.54e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_145_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-145-7TeV-pythia6/friis-RECO_crab_reco_TT_145-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.1930*_picobarns*2.61e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_150_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-150-7TeV-pythia6/friis-RECO_crab_reco_TT_150-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.1713*_picobarns*1.78e-2,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_155_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-155-7TeV-pythia6/friis-RECO_crab_reco_TT_155-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_160_HTT' : {
        'datasetpath' : "/ZH_ZToLL_HToTauTau_M-160-7TeV-pythia6/friis-RECO_crab_reco_TT_160-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 0.1334*_picobarns*3.96e-3,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },


    'ZH_110_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-110-7TeV-pythia6/friis-RECO_crab_reco_WW_110-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_115_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-115-7TeV-pythia6/friis-RECO_crab_reco_WW_115-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_120_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-120-7TeV-pythia6/friis-RECO_crab_reco_WW_120-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_125_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-125-7TeV-pythia6/friis-RECO_crab_reco_WW_125-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_130_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-130-7TeV-pythia6/friis-RECO_crab_reco_WW_130-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_135_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-135-7TeV-pythia6/friis-RECO_crab_reco_WW_135-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_140_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-140-7TeV-pythia6/friis-RECO_crab_reco_WW_140-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_145_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-145-7TeV-pythia6/friis-RECO_crab_reco_WW_145-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_150_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-150-7TeV-pythia6/friis-RECO_crab_reco_WW_150-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_155_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-155-7TeV-pythia6/friis-RECO_crab_reco_WW_155-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    'ZH_160_HWW' : {
        'datasetpath' : "/ZH_ZToLL_HToWW_WWTo2LNu-160-7TeV-pythia6/friis-RECO_crab_reco_WW_160-01715716b3165466edf30580d661ec8b/USER",
        'x_sec' : 999,
        'pu' : 'S6',
        'analyses' : ['VH'],
        'dbs' : "cms_dbs_ph_analysis_01",
    },

    ############################################################################
    #### H2Tau samples                      ####################################
    ############################################################################
    
    ######################### VBF H-->tau+tau ##################################
    'VBF_H2Tau_M-100' : {
        'datasetpath' : '/VBF_HToTauTau_M-100_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-105' : {
        'datasetpath' : '/VBF_HToTauTau_M-105_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },    
    'VBF_H2Tau_M-110' : {
        'datasetpath' : '/VBF_HToTauTau_M-110_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },    
    'VBF_H2Tau_M-115' : {
        'datasetpath' : '/VBF_HToTauTau_M-115_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },    
    'VBF_H2Tau_M-120' : {
        'datasetpath' : '/VBF_HToTauTau_M-120_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-125' : {
        'datasetpath' : '/VBF_HToTauTau_M-125_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-130' : {
        'datasetpath' : '/VBF_HToTauTau_M-130_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-135' : {
        'datasetpath' : '/VBF_HToTauTau_M-135_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-140' : {
        'datasetpath' : '/VBF_HToTauTau_M-140_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-145' : {
        'datasetpath' : '/VBF_HToTauTau_M-145_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    'VBF_H2Tau_M-150' : {
        'datasetpath' : '/VBF_HToTauTau_M-150_7TeV-powheg-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    
    ######################### GGH SM H-->tau+tau ##################################

    'GGH_H2Tau_M-100' : {
        'datasetpath' : '/GluGluToHToTauTau_M-100_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },    
    'GGH_H2Tau_M-105' : {
        'datasetpath' : '/GluGluToHToTauTau_M-105_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },    
    'GGH_H2Tau_M-110' : {
        'datasetpath' : '/GluGluToHToTauTau_M-110_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },   
    'GGH_H2Tau_M-115' : {
        'datasetpath' : '/GluGluToHToTauTau_M-115_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },   
    'GGH_H2Tau_M-120' : {
        'datasetpath' : '/GluGluToHToTauTau_M-120_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },   
    'GGH_H2Tau_M-125' : {
        'datasetpath' : '/GluGluToHToTauTau_M-125_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  
    'GGH_H2Tau_M-130' : {
        'datasetpath' : '/GluGluToHToTauTau_M-130_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  
    'GGH_H2Tau_M-135' : {
        'datasetpath' : '/GluGluToHToTauTau_M-135_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  
    'GGH_H2Tau_M-140' : {
        'datasetpath' : '/GluGluToHToTauTau_M-140_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },    
    'GGH_H2Tau_M-145' : {
        'datasetpath' : '/GluGluToHToTauTau_M-145_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },   
    'GGH_H2Tau_M-150' : {
        'datasetpath' : '/GluGluToHToTauTau_M-150_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },
    
    ######################### GGH MSSM H-->tau+tau ##################################
    
    'GGHMSSM_H2Tau_M-90' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-90_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  
    'GGHMSSM_H2Tau_M-100' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },              
    'GGHMSSM_H2Tau_M-120' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-120_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },          
    'GGHMSSM_H2Tau_M-130' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-130_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-140' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-140_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-160' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-160_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-180' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-180_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-200' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-200_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-250' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-250_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-300' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-300_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-350' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-350_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },          
    'GGHMSSM_H2Tau_M-400' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-400_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },          
    'GGHMSSM_H2Tau_M-450' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-450_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },          
    'GGHMSSM_H2Tau_M-500' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-500_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-600' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-600_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },          
    'GGHMSSM_H2Tau_M-700' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-700_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-800' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-800_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-900' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-900_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    'GGHMSSM_H2Tau_M-1000' : {
        'datasetpath' : '/SUSYGluGluToHToTauTau_M-1000_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },         
    
	######################### BBH MSSM H-->tau+tau ##################################
	
    'BBH_H2Tau_M-90' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-90_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  
    'BBH_H2Tau_M-100' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-120' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-130' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-140' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-160' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-180' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-200' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-250' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-300' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-350' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-400' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-450' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-500' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-600' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-700' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-800' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-900' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  	
    'BBH_H2Tau_M-1000' : {
        'datasetpath' : '/SUSYBBHToTauTau_M-100_7TeV-pythia6-tauola/Fall11-PU_S6_START42_V14B-v1/AODSIM',
        'x_sec' : -999*_picobarns,
        'pu' : 'S6',
        'analyses' : ['HTT'],
    },  
	
    ############################################################################
    #### Obscure VH backgrounds             ####################################
    ############################################################################

    'TTWToLplus' : {
        'datasetpath' :"/TTWTo2Lplus2Nu_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.006841)*_picobarns,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'TTZToLplus' : {
        'datasetpath' :"/TTZTo2Lplus2Nu_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.002024)*_picobarns,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'WWWTo2Lplus' : {
        'datasetpath' :"/WWWTo2Lplus2Nu_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        # These have some problems with the xsec for this sample
        #'x_sec' : (0.008957)*_picobarns,
        # Just basically turn it off.
        'x_sec' : (0.017)*_picobarns*br_www_all_leptons,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'TTWToLminus' : {
        'datasetpath' :"/TTWTo2Lminus2Nu_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.002705)*_picobarns,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'TTZToLminus' : {
        'datasetpath' :"/TTZTo2Lminus2Nu_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : (0.001946)*_picobarns,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    'WWWTo2Lminus' : {
        'datasetpath' :"/WWWTo2Lminus2Nu_7TeV-madgraph/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        #'x_sec' : (0.004109)*_picobarns,
        # These have some problems with the xsec for this sample
        # Just basically turn it off.
        'x_sec' : (0.017)*_picobarns*br_www_all_leptons,
        'pu' : 'S6',
        'analyses' : ['VH'],
    },

    ############################################################################
    #### H->ZZ->4L signal samples           ####################################
    ############################################################################

    'ggH_ZZ_4l_120' : {
        'datasetpath' : "/GluGluToHToZZTo4L_M-180_7TeV-powheg-pythia6/Fall11-PU_S6_START42_V14B-v1/AODSIM",
        'x_sec' : 6.739*_picobarns*6.02e-2*3*0.03365*3*0.03365,
        'pu' : 'S6',
        'analyses' : ['4L'],
    },
}

# Add all the datasets
def build_data_set(pd, analyses):
  subsample_dict = {
    'data_%s_Run2011B_PromptReco_v1' % pd : {
      'datasetpath' : "/%s/Run2011B-PromptReco-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_160404-180252_7TeV_PromptReco_Collisions11_JSON.txt",
      'firstRun' : 175832,
      'lastRun' : 180252,
      'analyses' : analyses,
    },
    'data_%s_Run2011A_PromptReco_v6_1409' % pd : {
      'datasetpath' : "/%s/Run2011A-PromptReco-v6/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_160404-178677_7TeV_PromptReco_Collisions11_JSON.txt",
      'firstRun' : 172620,
      'lastRun' : 175831,
      'analyses' : analyses,
    },
    'data_%s_Run2011A_05Aug2011_v1' % pd : {
      'datasetpath' : "/%s/Run2011A-05Aug2011-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_170249-172619_7TeV_ReReco5Aug_Collisions11_JSON_v3.txt",
      'firstRun' : 170249,
      'lastRun' : 172619,
      'analyses' : analyses,
    },
    'data_%s_Run2011A_PromptReco_v4' % pd : {
      'datasetpath' : "/%s/Run2011A-PromptReco-v4/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_160404-178677_7TeV_PromptReco_Collisions11_JSON.txt",
      'firstRun' : 163870,
      'lastRun' : 170248,
      'analyses' : analyses,
    },
    'data_%s_Run2011A_May10ReReco_v1' % pd : {
      'datasetpath' : "/%s/Run2011A-May10ReReco-v1/AOD" % pd,
      'lumi_mask' : "FinalStateAnalysis/RecoTools/data/masks/Cert_160404-163869_7TeV_May10ReReco_Collisions11_JSON_v3.txt",
      'firstRun' : 160404,
      'lastRun' : 163869,
      'analyses' : analyses,
    },
  }
  sample_dict = {
    'data_%s' % pd : subsample_dict.keys()
  }
  return subsample_dict, sample_dict

# Build all the PDs we use
data_DoubleMu, list_DoubleMu = build_data_set('DoubleMu', ['VH', 'Mu'])
datadefs.update(data_DoubleMu)
data_name_map.update(list_DoubleMu)

data_MuEG, list_MuEG = build_data_set('MuEG', ['VH', 'HTT', 'Mu'])
datadefs.update(data_MuEG)
data_name_map.update(list_MuEG)

data_DoubleE, list_DoubleE = build_data_set('DoubleElectron', ['VH',])
datadefs.update(data_DoubleE)
data_name_map.update(list_DoubleE)

data_SingleMu, list_SingleMu = build_data_set('SingleMu', ['Tau', 'Mu'])
datadefs.update(data_SingleMu)
data_name_map.update(list_SingleMu)

data_SingleElectron, list_SingleElectron = build_data_set('SingleElectron', ['Tau', 'E', 'Wjets'])
datadefs.update(data_SingleElectron)
data_name_map.update(list_SingleElectron)

data_TauPlusX, list_TauPlusX = build_data_set('TauPlusX', ['HTT', 'SSDL'])
datadefs.update(data_TauPlusX)
data_name_map.update(list_TauPlusX)

#data_MuHad, list_MuHad = build_data_set('MuHad', ['SSDL'])
#datadefs.update(data_MuHad)
#data_name_map.update(list_MuHad)

if __name__ == "__main__":
    # Print a latex table of the samples
    samples = []
    data_samples = []
    for sample, sample_info in datadefs.iteritems():
        if 'data' not in sample:
            #samples.append(sample_info['datasetpath'].split('/')[1])
            samples.append(sample_info['datasetpath'])

    for sample in sorted(samples):
        print sample.replace('_', '\_') + ' \\\\'

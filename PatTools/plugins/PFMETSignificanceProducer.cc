/*
 * Store a PFMET significance matrix in the event.
 *
 * Based on code by Christian Veelken
 *
 * Author: Evan K Friis, UW Madison
 */

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "DataFormats/Math/interface/Error.h"
#include "FinalStateAnalysis/PatTools//interface/PFMEtSignInterfaceBase.h"

class PFMETSignificanceProducer : public edm::EDProducer {
  public:
    PFMETSignificanceProducer(const edm::ParameterSet& pset);
    virtual ~PFMETSignificanceProducer(){}
    void produce(edm::Event& evt, const edm::EventSetup& es);
  private:
    typedef math::Error<2>::type Matrix;
    typedef std::vector<edm::InputTag> vInputTag;
    vInputTag src_;
    PFMEtSignInterfaceBase pfMEtSignInterface_;
};

PFMETSignificanceProducer::PFMETSignificanceProducer(const edm::ParameterSet& pset)
  : pfMEtSignInterface_(pset) {
  src_ = pset.getParameter<vInputTag>("src");
  produces<Matrix>();
}

void PFMETSignificanceProducer::produce(edm::Event& evt, const edm::EventSetup& es) {

  std::list<const reco::Candidate*> particles;
  for ( vInputTag::const_iterator src_i = src_.begin();
	src_i != src_.end(); ++src_i ) {
    edm::Handle<reco::CandidateView> particles_i;
    evt.getByLabel(*src_i, particles_i);
    for ( reco::CandidateView::const_iterator particle = particles_i->begin();
	  particle != particles_i->end(); ++particle ) {
      particles.push_back(&(*particle));
    }
  }

  TMatrixD result_tm = pfMEtSignInterface_(particles);

  std::auto_ptr<Matrix> output(new Matrix());
  (*output)(0,0) = result_tm(0, 0);
  (*output)(1,0) = result_tm(1, 0);
  (*output)(0,1) = result_tm(0, 1);
  (*output)(1,1) = result_tm(1, 1);

  evt.put(output);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PFMETSignificanceProducer);

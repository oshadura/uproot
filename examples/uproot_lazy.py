import uproot
import numpy as np

events = uproot.open("http://scikit-hep.org/uproot/examples/Event.root")['T']

lazyarray = events.lazyarray("fTracks.fCharge", entrysteps=100)

print("Lazy or iteration steps as a fixed number of entries:")
for arrays in events.iterate(entrysteps=100):
    print(len(arrays[b"fTracks.fCharge"]))

print("\nLazy or iteration steps as a fixed memory footprint:")
for arrays in events.iterate(entrysteps="100 kB"):
    print(len(arrays[b"fTracks.fCharge"]))

###
lazy = uproot.lazyarrays(["http://scikit-hep.org/uproot/examples/Event.root", "http://scikit-hep.org/uproot/examples/Event.root"], "T")
print(lazy)
###
cache = uproot.ArrayCache("3 GB")
events = uproot.lazyarrays("root://eospublic.cern.ch//eos/root-eos/cms_opendata_2012_nanoaod/Run2012B_DoubleMuParked.root", "Events", entrysteps="1 GB", cache=cache)
pz = events.Muon_pt * np.sinh(events.Muon_eta)

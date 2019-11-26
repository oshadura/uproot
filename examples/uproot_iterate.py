import uproot
import numpy as np

for par_ in uproot.iterate("http://scikit-hep.org/uproot/examples/Event.root", 'T', ['fTracks.fPx', 'fTracks.fPy', 'fTracks.fPz', 'fTracks.fRandom', 'fTracks.fMass2', 'fTracks.fBx', 'fTracks.fBy', 'fTracks.fMeanCharge']):
    par = {key.decode("utf-8"): value for (key, value) in par_.items()}
    for i, x in enumerate(zip( par['fTracks.fPx'], par['fTracks.fPy'], par['fTracks.fPz'], par['fTracks.fRandom'], par['fTracks.fMass2'], par['fTracks.fBx'], par['fTracks.fBy'], par['fTracks.fMeanCharge'])):
        print(i)
        objs = np.array(list(zip(x[0], x[1], x[2],x[3], x[4], x[5], x[6], x[7])))
        print(objs)
import uproot
import concurrent.futures

executor = concurrent.futures.ThreadPoolExecutor(8)

data_file_ = uproot.open("http://scikit-hep.org/uproot/examples/Event.root")['T']
n_events = 100
offset = 1
branches_to_read_ = [
    'fTracks.fPx',
    'fTracks.fPy',
    'fTracks.fPz'
    ]

# Set the total number of events in the data file to be updated if offset and n_events are provided
number_of_events_ = data_file_.numentries if n_events == -1 else n_events

# Default value for starting to read the root file into an array
entrystart = None

entrystop = None if n_events == -1 else n_events
if offset != -1:
    entrystart = offset
    if entrystop is None:
        # Stop reading entries at the end of all events
        entrystop = number_of_events_
    else:
        entrystop += entrystart
    # No. of events changes if both offset and n_events are specified
    number_of_events_ = entrystop - entrystart

# array will be indexed [entrystart, ... entrystop-1]
data_ = data_file_.arrays(
    branches_to_read_,
    entrystart=entrystart,
    executor=executor,
    entrystop=entrystop
)
data_ = {i.decode('utf-8') : j for i, j in data_.items()}
print(data_)
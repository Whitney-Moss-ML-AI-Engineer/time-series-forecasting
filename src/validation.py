"""Walk-forward temporal validation."""
import numpy as np
def walk_forward(series,train_size,horizon,step=1):
    series=np.asarray(series)
    for end in range(train_size,len(series)-horizon+1,step):
        yield series[:end],series[end:end+horizon]

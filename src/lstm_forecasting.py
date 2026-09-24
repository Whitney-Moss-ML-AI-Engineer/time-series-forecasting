"""Minimal PyTorch LSTM forecaster."""
from torch import nn
class LSTMForecaster(nn.Module):
    def __init__(self,features=1,hidden=64,layers=2):
        super().__init__()
        self.lstm=nn.LSTM(features,hidden,layers,batch_first=True)
        self.head=nn.Linear(hidden,1)
    def forward(self,x):
        z,_=self.lstm(x)
        return self.head(z[:,-1,:])

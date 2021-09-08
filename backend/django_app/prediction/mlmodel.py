import torch
from torch import nn

class Model(nn.Module):
    
    def __init__(self, input_dim=4):
        super(Model, self).__init__()

        self.layer1 = nn.Linear(input_dim, 50)
        self.layer2 = nn.Linear(50, 20)
        self.layer3 = nn.Linear(20, 3)

    def forward(self, x):
        x = nn.functional.relu(self.layer1(x))
        x = nn.functional.relu(self.layer2(x))
        x = nn.functional.softmax(self.layer3(x))

        return x
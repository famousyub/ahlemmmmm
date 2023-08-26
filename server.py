# server.py
import syft as sy
import torch

hook = sy.TorchHook(torch)

# Create a virtual worker for the server
server = sy.VirtualWorker(hook, id="server")

# Create a model
model = torch.nn.Linear(2, 1)
model.send(server)

# Initial model parameters
global_model_params = model.parameters()

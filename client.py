# client.py
import syft as sy
import torch

hook = sy.TorchHook(torch)

# Create virtual workers for clients
client1 = sy.VirtualWorker(hook, id="client1")
client2 = sy.VirtualWorker(hook, id="client2")

# Load or generate client data
client1_data = torch.tensor([[1.0, 2.0], [2.0, 3.0]])
client2_data = torch.tensor([[4.0, 5.0], [5.0, 6.0]])

# Send data to respective clients
client1_data_ptr = client1_data.send(client1)
client2_data_ptr = client2_data.send(client2)

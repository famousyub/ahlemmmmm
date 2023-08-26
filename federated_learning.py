# federated_learning.py
import syft as sy
import torch

hook = sy.TorchHook(torch)

# Load pre-trained global model parameters on the server
server = sy.VirtualWorker(hook, id="server")
global_model = torch.nn.Linear(2, 1).send(server)

# Encrypted training at client 1
client1 = sy.VirtualWorker(hook, id="client1")
client1_data = torch.tensor([[1.0, 2.0], [2.0, 3.0]])
encrypted_data1 = client1_data.encrypt()

# Encrypted training at client 2
client2 = sy.VirtualWorker(hook, id="client2")
client2_data = torch.tensor([[4.0, 5.0], [5.0, 6.0]])
encrypted_data2 = client2_data.encrypt()

# Federated averaging with homomorphic encryption
global_model = global_model.get()
global_model_params = list(global_model.parameters())

# Decrypt and update model at client 1
decrypted_params1 = [param.get().decrypt() for param in global_model_params]
client1_model = torch.nn.Linear(2, 1, weight=decrypted_params1[0], bias=decrypted_params1[1])
client1_opt = torch.optim.SGD(client1_model.parameters(), lr=0.1)
client1_opt.step()

# Decrypt and update model at client 2
decrypted_params2 = [param.get().decrypt() for param in global_model_params]
client2_model = torch.nn.Linear(2, 1, weight=decrypted_params2[0], bias=decrypted_params2[1])
client2_opt = torch.optim.SGD(client2_model.parameters(), lr=0.1)
client2_opt.step()

# Average updated parameters and encrypt
average_params = [(param1 + param2).encrypt() for param1, param2 in zip(client1_model.parameters(), client2_model.parameters())]

# Update global model with averaged parameters
for global_param, average_param in zip(global_model.parameters(), average_params):
    global_param.set_(average_param.get())

# Send the updated global model back to the server
global_model = global_model.send(server)

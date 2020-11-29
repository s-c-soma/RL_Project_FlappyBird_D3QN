import torch

if torch.cuda.is_available():
  dev = "cuda:0"
  print('cuda')
else:
  dev = "cpu"
  print('cpu')
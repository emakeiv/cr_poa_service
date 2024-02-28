import torch
import torch.nn as nn


class POA_RNN(nn.Module):
    def __init__(self, 
                 device,
                 no_layers=2, 
                 hidden_dim=256, 
                 embedding_dim=300,
                 output_dim=1, 
                 drop_prob=0.5,
                 debug=False):
        super(POA_RNN, self).__init__()
        
        self.output_dim = output_dim
        self.hidden_dim = hidden_dim
        self.embedding_dim = embedding_dim
        self.no_layers = no_layers
        self.debug = debug
        self.device = device

        self.lstm = nn.LSTM(input_size=self.embedding_dim, 
                            hidden_size=hidden_dim, 
                            num_layers=no_layers, 
                            batch_first=True,
                            dropout=drop_prob if no_layers > 1 else 0)

        self.dropout = nn.Dropout(drop_prob)
        self.fc = nn.Linear(hidden_dim, output_dim)
        
    def forward(self, x, hidden):
        if self.debug:
            print(f"Input shape: {x.shape}")  
        
        batch_size = x.size(0)
        x = x.unsqueeze(1) 
        if self.debug:
            print(f"shape after embedding: {x.shape}")
            print(f"hidden state shape: {hidden[0].shape}, {hidden[1].shape}")
        
        lstm_out, hidden = self.lstm(x, hidden)
        lstm_out = lstm_out.contiguous().view(-1, self.hidden_dim)
        
        out = self.dropout(lstm_out)
        out = self.fc(out)

        sig_out = torch.sigmoid(out)
        sig_out = sig_out.view(batch_size, -1)
        sig_out = sig_out[:, -1]  
        
        return sig_out, hidden
        
    def init_hidden(self, batch_size):
        # Create two new tensors with sizes n_layers x batch_size x hidden_dim,
        # initialized to zero, for hidden state and cell state of LSTM

        weight = next(self.parameters()).data
        h0 = weight.new(self.no_layers, batch_size, self.hidden_dim).zero_().to(self.device)
        c0 = weight.new(self.no_layers, batch_size, self.hidden_dim).zero_().to(self.device)
        
        if self.debug:
            print(f"h0 shape: {h0.shape}")
            print(f"c0 shape: {c0.shape}")

        return (h0, c0)
        return hidden
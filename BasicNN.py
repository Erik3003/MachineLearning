import random
 
class neuron:
    def __init__(self, weight_count):
        self.table = [0.0] * (weight_count + 1)
 
    def get_table(self):
        return self.table
 
    def set_table(self, table):
        if len(self.table) != len(table):
            print("ERROR, incorrect data")
            return
        self.table = table
 
    def set_random(self):
        for i in range(len(self.table)):
            self.table[i] = random.uniform(0, 10)
 
    def run(self, data):
        d = [-1.0] + data
        result = 0
        for i in range(len(self.table)):
            result += d[i] * self.table[i]
        if result < 0.0:
            result = 0.0
        else:
            result = 1.0
        return result
 
class layer:
    def __init__(self, neuron_count, p_neuron_count):
        self.neurons = []
        for i in range(neuron_count):
            n = neuron(p_neuron_count)
            self.neurons.append(n)
 
    def set_random(self):
        for i in range(len(self.neurons)):
            self.neurons[i].set_random()
 
    def set_layer(self, neurons):
        if len(self.neurons) != len(neurons):
            print("ERROR, incorrect data")
            return
        for i in range(len(self.neurons)):
            self.neurons[i].set_table(neurons[i])
 
    def print_layer(self):
        for n in self.neurons:
            print(n.get_table())
 
    def run(self, data):
        processed_data = []
        for n in self.neurons:
            processed_data.append(n.run(data))
        return processed_data
 
 
class neural_network:
    def __init__(self, *neurons_per_layer):
        self.layers = []
        self.input_count = p_neutron_count = neurons_per_layer[0]
        for neuron_count in neurons_per_layer[1:]:
            l = layer(neuron_count, p_neutron_count)
            p_neutron_count = neuron_count
            self.layers.append(l)
 
    def set_random(self):
        for l in self.layers:
            l.set_random()
 
    def print_network(self):
        for l in self.layers:
            l.print_layer()
 
    def set_network(self, layers):
        if len(self.layers) != len(layers):
            print("ERROR, incorrect data")
            return
        for i in range(len(self.layers)):
            self.layers[i].set_layer(layers[i])
 
    def run(self, *inputs):
        if len(inputs) != self.input_count:
            print("Incorrect input count. This network needs ", self.input_count, " input(s).")
            return
        data = list(inputs)
        for l in self.layers:
            data = l.run(data)
        return data                
 
if __name__ == "__main__":
    nn = neural_network(2, 1)
    nn_data = [[[1.5,1.0,1.0]]]
    nn.set_network(nn_data)
    print("Network/Neuron(s):")
    nn.print_network()
    network_input = (1.0, 1.0)
    print("Input values: ", network_input)
    print("Output: ", nn.run(*network_input))
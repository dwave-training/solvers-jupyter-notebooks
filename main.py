# !pip install ocean sdk
from dimod import BinaryQuadraticModel

bqm = BinaryQuadraticModel('BINARY')

bqm.add_variable('x', 1.0)
bqm.add_variable('y', 1.0)
bqm.add_interaction('x', 'y', -1.0)

print(bqm.shape)
print(bqm)
print(bqm.change_vartype('SPIN'))


from dimod import ExactSolver
response = ExactSolver().sample(bqm)
print(response)


from neal import SimulatedAnnealingSampler
response = SimulatedAnnealingSampler().sample(bqm)
print(response)


from dwave.system import DWaveSampler
from dwave.system import EmbeddingComposite
response = EmbeddingComposite(DWaveSampler()).sample(bqm)
print(response)


from dwave.system import LeapHybridSampler
response = LeapHybridSampler().sample(bqm)
print(response)



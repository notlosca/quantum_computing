
from qiskit import *
from qiskit import IBMQ
from qiskit.visualization import plot_histogram, plot_bloch_vector
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'svg' # Makes the images look nice")

qr = QuantumRegister(4)
cr = ClassicalRegister(4)

qcircuit = QuantumCircuit(qr, cr)

get_ipython().run_line_magic('matplotlib', 'inline')

#our circuit to implement the sum of 1, 0 and a carry in equal to 1


qcircuit.x(qr[0]) #set to 1 the 1st addend
qcircuit.x(qr[2]) #set to 1 the carry in
qcircuit.ccx(qr[0], qr[1], qr[3]) #control, control, target (Toffoli gate)
qcircuit.cx(qr[0], qr[1]) #control, target (CNOT gate)
qcircuit.ccx(qr[1], qr[2], qr[3])
qcircuit.cx(qr[1], qr[2])
qcircuit.cx(qr[0], qr[1])
qcircuit.measure(qr, cr)
qcircuit.draw(output = 'mpl')


#in local
simulator = Aer.get_backend('qasm_simulator')
result = execute(qcircuit, backend = simulator).result()
print(result.get_counts(qcircuit))
plot_histogram(result.get_counts(qcircuit))




#load the account in order to launch our circuit on a real quantum computer
IBMQ.load_account() #load the account in order to execute the code on the quantum computer




#get the provider and use a job monitor 
provider = IBMQ.get_provider('ibm-q')
qcomp = provider.get_backend('ibmq_16_melbourne') #had to change from imbq_london for more accuracy
job = execute(qcircuit, backend = qcomp, shots = 8192)
from qiskit.tools.monitor import job_monitor
job_monitor(job)


#see the results 
qresult = job.result()
print(qresult.get_counts(qcircuit))
plot_histogram(qresult.get_counts(qcircuit))






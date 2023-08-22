import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from scipy.special import comb


blockLength = 1000; # Number of symbols per block
nBlocks = 10000; # Number of blocks
L = 2; # Number of antennas
EbdB = np.arange(1.0,18.1,1.5); # Energy per bit in dB
Eb = 10**(EbdB/10); # Energy per bit Eb
No = 1; # Total noise power No
SNR = 2*Eb/No; # Signal-to-noise power ratio
SNRdB = 10*np.log10(Eb/No); # SNR values in dB
BER = np.zeros(len(EbdB)); # Bit error rate (BER) values
BERt = np.zeros(len(EbdB)); # Analytical values of BER from formula



    
BER = BER/blockLength/nBlocks/2; # Evaluating BER from simulation 
BERt = comb(2*L-1, L)/2**L/SNR**L; # Evaluating BER from formula
# Plotting the bit error rate from Simulation and formula
plt.yscale('log')
plt.plot(SNRdB, BER,'g-');
plt.plot(SNRdB, BERt,'ro');
plt.grid(1,which='both')
plt.suptitle('BER for MRC')
plt.legend(["Simulation", "Theory"], loc ="lower left");
plt.xlabel('SNR (dB)')
plt.ylabel('BER') 

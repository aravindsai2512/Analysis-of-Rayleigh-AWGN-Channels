import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr
from scipy.stats import norm

blockLength = 1000;
nBlocks = 1000;
No = 1;
EbdB = np.arange(1.0,10.1,1.0);
Eb = 10**(EbdB/10);
SNR = 2*Eb/No;
SNRdB = 10*np.log10(SNR);
BER = np.zeros(len(EbdB));
BERt = np.zeros(len(EbdB));




BER = BER/blockLength/2/nBlocks;
BERt = 1-norm.cdf(np.sqrt(SNR));

plt.yscale('log');
plt.plot(SNRdB,BER,'g-')
plt.plot(SNRdB,BERt,'rs')
plt.grid(1,which='both')
plt.suptitle('BER for AWGN')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.legend(["BER","BER Theory"],loc ="lower left")
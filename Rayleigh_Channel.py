import numpy as np
import matplotlib.pyplot as plt
import numpy.random as nr


blockLength = 1000;
nBlocks = 10000;
No = 1;
EbdB = np.arange(1.0,42.1,3.0);
Eb = 10**(EbdB/10);
SNR = 2*Eb/No;
SNRdB = 10*np.log10(SNR);
BER = np.zeros(len(EbdB));
BERt = np.zeros(len(EbdB));




BER = BER/blockLength/2/nBlocks;
BERt = 1/2*(1-np.sqrt(SNR/(2+SNR)));

plt.yscale('log');
plt.plot(SNRdB,BER,'g-')
plt.plot(SNRdB,BERt,'rs')
plt.grid(1,which='both')
plt.suptitle('BER for Rayleigh Fading Channel')
plt.xlabel('SNR (dB)')
plt.ylabel('BER')
plt.legend(["BER","BER Theory"],loc ="lower left")
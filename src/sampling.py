import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq, fftshift

f0 = 10e3

x0 = lambda t: np.cos(2*np.pi*f0*t)
x1 = lambda t: np.sin(2*np.pi*f0*t)
x2 = lambda t: np.cos(2*np.pi*f0*t + np.deg2rad(45))
x8 = lambda t: 2*np.exp(-100*t)*np.sin(2000*t)

def sample_signal(x_func, Fs, duration=2e-3):
    Ts = 1/Fs
    n = np.arange(0, duration, Ts)
    y = x_func(n)
    return n, y

def compare_fftmag_to_derived(x_func, Fs, duration=0.2):
    x8_signal = sample_signal(x_func, Fs, duration)[1]
    N = len(x8_signal)

    X8_fft = fftshift(fft(x8_signal))
    omega_fft = (2*np.pi)*fftshift(fftfreq(N, 1/Fs))
    
    term1 = 1 / (100 - 1j*(2000 - omega_fft))
    term2 = 1 / (100 + 1j*(2000 + omega_fft))
    X8_analytic = (1 / 1j) * (term1 - term2)

    X8a = np.abs(X8_analytic)
    X8f = np.abs(X8_fft)

    X8a /= np.max(X8a)
    X8f /= np.max(X8f)

    plt.plot(omega_fft, X8a, label="Analytic |X8(ω)|", color='blue', linewidth=3)
    plt.plot(omega_fft, X8f, label="FFT Approximation", color='green', linewidth=2)
    plt.xlim(-8000, 8000)
    plt.xlabel("ω (rad/s)")
    plt.ylabel("Magnitude")
    plt.title("Comparison: Analytic vs FFT-Based Approximation of X8(ω) - Normalized")
    plt.grid(True)
    plt.legend()
    plt.savefig("plot/x8_comparison.png")

    

def plot_fft(y, Fs, title, filename_mag, filename_phase):
    N = len(y)
    Y = fftshift(fft(y))
    freq = fftshift(fftfreq(N, 1/Fs))

    plt.plot(freq, np.abs(Y))
    plt.title(title + " - Magnitude")
    plt.xlabel("Frequency (Hz)")
    plt.grid(True)
    plt.savefig("plot/" + filename_mag)
    plt.close()

    plt.plot(freq, np.angle(Y))
    plt.title(title + " - Phase")
    plt.xlabel("Frequency (Hz)")
    plt.grid(True)
    plt.savefig("plot/" + filename_phase)
    plt.close()

n, y0 = sample_signal(x0, Fs=20e3)

plt.stem(n, y0)
plt.title("y0[n] = x0(nTs) at Fs = 20 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y0.png')
plt.close()

n, y1 = sample_signal(x1, Fs=20e3)

plt.stem(n, y1)
plt.title("y1[n] = x1(nTs) at Fs = 20 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y1.png')
plt.close()

n, y2 = sample_signal(x2, Fs=20e3)

plt.stem(n, y2)
plt.title("y2[n] = x2(nTs) at Fs = 20 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y2.png')
plt.close()

n, y3 = sample_signal(x0, Fs=40e3)

plt.stem(n, y3)
plt.title("y3[n] = x0[nTs] at Fs = 40 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y3.png')
plt.close()

n, y4 = sample_signal(x1, Fs=40e3)

plt.stem(n, y4)
plt.title("y4[n] = x1[nTs] at Fs = 40 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y4.png')
plt.close()

n, y5 = sample_signal(x2, Fs=40e3)

plt.stem(n, y5)
plt.title("y5[n] = x2[nTs] at Fs = 40 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y5.png')
plt.close()

n, y6 = sample_signal(x1, Fs=1e6)

plt.stem(n, y6)
plt.title("y6[n] = x1[nTs] at Fs = 1 MHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y6.png')
plt.close()

n, y7 = sample_signal(x1, Fs=8e3)

plt.stem(n, y7)
plt.title("y7[n] = x1[nTs] at Fs = 8 kHz")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.grid(True)
plt.savefig('plot/y7.png')
plt.close()

plot_fft(y0, 20e3, "Y(0)", "y0_mag.png", "y0_phase.png")
plot_fft(y5, 40e3, "Y(5)", "y5_mag.png", "y5_phase.png")
plot_fft(y6, 1e6, "Y(6)", "y6_mag.png", "y6_phase.png")
plot_fft(y7, 20e3, "Y(7)", "y7_mag.png", "y7_phase.png")

compare_fftmag_to_derived(x8, Fs=1e6)


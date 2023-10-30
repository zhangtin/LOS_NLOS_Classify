# LOS/NLOS Classification Algorithm

**Please Note:** This code is intended for academic use only. Commercial usage is not allowed.

## Description

This repository contains an executable MATLAB function for Indoor Line-of-Sight (LOS) and Non-Line-of-Sight (NLOS) classification. The function is ready to work and can be used to classify signals based on LOS/NLOS conditions.

This function will return a boolean
- 1: Line-of-Sight (LOS)
- 0: Non Line-of-Sight (NLOS)

## Usage

### Syntax

```matlab
y = check_LOS(signal, fc, num_antenna, distance, scan_range, scan_interval)
```
###  Parameters
- signal (complex waveform): The input complex waveform for classification.
- fc (Hz): Signal central frequency (default: 5320e6 Hz).
- num_antenna: Number of antennas on the Uniform Linear Array (ULA) (default: 4).
- distance (meters): Inter-element distance on ULA (default: 0.025 meters).
- scan_range: Array representing the broadside angle under test (default: -90:1:90).
- scan_interval: Sweep angle per step for speeding up the process (default: 10 degrees).

### Important Note
This function requires an N*M complex signal waveform, where:

- N is the number of samples.
- M is the number of antennas on the ULA.
It can be applied to various modulation methods, including:
  - QPSK
  - 4-QAM
  - 8-QAM
  - 16-QAM
  - 32-QAM
  - 64-QAM
- Any 2-dimensional modulation scheme should be acceptable for this algorithm.

### License
This code is provided under the terms of the **No Commercial Use** license. You are allowed to use it for academic purposes but not for commercial applications.

### Disclaimer
This code is provided as-is and without any warranties. Please use it responsibly and in accordance with the provided license terms.

For any questions or inquiries, feel free to contact zhangtin@oregonstate.edu.

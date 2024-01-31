%% Los_Check example code
clc,clear,close all
% parameter setup initialization
fc = 5520e6; %signal carrier frequency
c = physconst("LightSpeed");
lambda = physconst('LightSpeed')/fc; % wavelength calculation
q = 2*pi/lambda;
d = lambda/2; % inter-element distance setup
N = 4;  %Antenna number
% Beamforming setup
azi = -90:1:90;
ucor = sind(azi);
ucor_matrix = exp(-1j * q * d * (0:N-1).' * ucor); %Beamforming weigthing
% Optional Parameter
Scan_interval = 10; % for speeding up
% Load waveform
sig = load(fullfile("QPSK_new/LOS/1.mat")).data; %load signal
%% Signal separation
tic
I = sig * ucor_matrix;
%% Check if is LOS
Result = LOS_Classify(I,Scan_interval);
toc
%% Display result
if Result == 1
    fprintf("Signal from LOS\n")
else
    fprintf("Signal from NLOS\n")
end
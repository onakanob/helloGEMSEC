%{
For normalized vector p, representing the normalized histogram in dataset 
I, S = -sum(p .* log2(p))
%}

I = uint8(zeros(256,256));
for i = 1:256
    I(:,i) = i-1;
end
figure
subplot(5,2,1), imshow(I)

I2 = uint8(256.*rand(64,64));
subplot(5,2,3), imshow(I2);

subplot(5,2,2), imhist(I), title(entropy(I));
subplot(5,2,4), imhist(I2), title(entropy(I2));

I3 = normrnd(0,1,64,64);
I3 = I3 - min(I3(:));
I3 = uint8(256 .* (I3./max(I3(:))));
subplot(5,2,5), imshow(I3);
subplot(5,2,6), imhist(I3), title(entropy(I3));

I4 = uint8(256.*(rand(64, 64)>0.5));
subplot(5,2,7), imshow(I4);
subplot(5,2,8), imhist(I4), title(entropy(I4));

I5 = uint8(64.*(ceil(4.*rand(64, 64))-1));
subplot(5,2,9), imshow(I5);
subplot(5,2,10), imhist(I5), title(entropy(I5));

%% Signal content stuff
I_signal = uint8(zeros(256,256));
for i = 1:256
    I_signal(:,i) = i-1;
end
I_signal = [I_signal uint8(100*ones(256,256))];

I_reduced = uint8(zeros(256,256));
for i = 1:256
    I_reduced(:,i) = mod((i-1),128);
end

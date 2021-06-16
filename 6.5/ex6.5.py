text = "X-DSPAM-Confidence:    0.8475";
length = len(text)
fstnum = text.find('0')
range = text[fstnum-1 : length]
newnum = float(range)
print(newnum)

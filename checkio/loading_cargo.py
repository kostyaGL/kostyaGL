def checkio(data): #dynamic programming
   sumdata, outputs = sum(data), {0}
   for n in data:
       outputs |= {m + n for m in outputs if m + n <= sumdata // 2}
   return sumdata - 2 * max(outputs)
print checkio([10, 10])
print checkio([10])
print checkio([5, 8, 13, 27, 14])
print checkio([5,5,6,5])
print checkio([12, 30, 30, 32, 42, 49])
print checkio([1, 1, 1, 3])

# list = [-1.8, 1.5, -2.2, 4.3, 12.7, 2.2, -28.0, 6.1, 7.0, -4.85, 0.77, 4.0, -2.6, 6.7, 2.5, -3.1, -4.905, 6.0, 6.3, -5.9, -2.2, 0.98, 2.4, -4.85, -3.0, 0.074]
# total = 0
# for x in list:
#     total += x
# print(total)

# print(reference_frequencies)
            # print(LetterFrequency(self.encrypt(text, -key)).get_frequencies())
            # print("------------------")
            # print(frequency_diff)

            # print("\n")

reference_frequencies = [1, 2, 3]
encrypted_frequencies = [3, 1, 2]  # Shifted 1 position to the right

# For key = 0
frequency_diff = [abs(a - b) for a, b in zip(reference_frequencies, encrypted_frequencies)]
print(frequency_diff)
print(sum(frequency_diff))  # Outputs: 4

# For key = 1
shifted_encrypted_frequencies = encrypted_frequencies[1:] + encrypted_frequencies[:1]
frequency_diff = [abs(a - b) for a, b in zip(reference_frequencies, shifted_encrypted_frequencies)]
print(sum(frequency_diff))  # Outputs: 0
import matplotlib.pyplot as plt
import numpy as np
rsa_key_size = [512, 1024, 2048, 3072, 4096, 7680, 15360]
rsa_sign = [16740.7, 4460.5, 621.5, 192.0, 84.2, 9.7, 1.7 ]
rsa_verify = [178852.4, 69184.2 , 20279.9, 9339.9, 5375.0, 1567.4, 393.2 ]
rsa_enc = [150613.4 , 63598.2, 19525.2,  9140.5, 5286.3, 1550.7, 391.3]
rsa_dec = [12311.0, 4019.0, 582.7, 192.3, 83.8, 9.6, 1.7]

aes_block_size = [16, 64, 256, 1024, 8192, 16384]
aes_128 = [520196.12, 599876.52, 619567.79, 623290.37, 626898.96, 624203.09]
aes_192 = [446592.87,503197.67, 518466.35, 519970.82, 520798.21, 522337.26]
aes_256 = [390101.17, 433196.31, 443161.26, 445795.67, 447811.98, 446496.77]
byte_16 = [520196.12, 446592.87, 390101.17]
byte_64 = [599876.52, 503197.67, 433196.31]
byte_256 = [ 619567.79, 518466.35, 443161.26]
byte_1024 = [623290.37, 519970.82, 445795.67]
byte_8192 = [626898.96, 520798.21, 447811.98]
byte_16384 = [624203.09, 522337.26, 446496.77]


plt.figure(figsize=(10, 6))
bar_width = 0.25
index_rsa = np.arange(len(rsa_key_size))
plt.bar(index_rsa - bar_width*1.5, rsa_sign, width=bar_width, label='RSA Sign/s')
plt.bar(index_rsa - bar_width*0.5, rsa_verify, width=bar_width, label='RSA Verify/s')
plt.bar(index_rsa + bar_width*0.5, rsa_enc, width=bar_width, label='RSA Encrypt/s')
plt.bar(index_rsa + bar_width*1.5, rsa_dec, width=bar_width, label='RSA Decrypt/s')
plt.xlabel('RSA Key Size')
plt.ylabel('Throughput')
plt.title('RSA Key Size vs Throughput')
plt.xticks(index_rsa, rsa_key_size)
plt.legend()
plt.show()


plt.figure(figsize=(10, 6))
bar_width = 0.25 
index_aes = np.arange(len(aes_block_size))
plt.bar(index_aes, aes_128, width=bar_width, label='AES-128')
plt.bar([i + bar_width for i in index_aes], aes_192, width=bar_width, label='AES-192')
plt.bar([i + 2 * bar_width for i in index_aes], aes_256, width=bar_width, label='AES-256')
plt.xlabel('Block Size')
plt.ylabel('Throughput')
plt.title('AES Block Size vs Throughput')
plt.xticks(index_aes, aes_block_size)
plt.legend()
plt.show()
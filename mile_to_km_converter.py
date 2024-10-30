import tkinter

def miles_to_km_converter():
    """ Converts miles to km, when user clicks 'Calculate' button and display the result. """

    def miles_to_km():
        """ Convert user input (miles) to km, when user clicks 'Calculate' button, and
        display the result in 'result_label' by rounding it to two decimal places. """
        miles = user_input.get()
        miles = int(miles) if miles.isnumeric() else 0
        km = round(miles * 1.609344, 2)
        result_label.config(text=f"{km}")

    # Set the window for the application
    window = tkinter.Tk()
    window.title("Mile to Km Converter")
    window.config(padx=20, pady=20)

    # Entry for user input (miles)
    user_input = tkinter.Entry(width=7)
    user_input.grid(column=1, row=0)

    # Miles Label
    miles_label = tkinter.Label(text="Miles", font=("Arial", 12, "italic"))
    miles_label.grid(column=2, row=0)

    # Miles Label
    equals_label = tkinter.Label(text="is equal to", font=("Arial", 12, "italic"))
    equals_label.grid(column=0, row=1)

    # Result Label
    result_label = tkinter.Label(text="0", font=("Arial", 12, "italic"))
    result_label.grid(column=1, row=1)

    # Km Label
    km_label = tkinter.Label(text="Km", font=("Arial", 12, "italic"))
    km_label.grid(column=2, row=2)

    # Calculate Button
    button = tkinter.Button(text="Calculate", command=miles_to_km)
    button.grid(column=1, row=2)

    window.mainloop()


if __name__ == "__main__":
    miles_to_km_converter()

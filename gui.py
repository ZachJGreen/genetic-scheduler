import tkinter as tk
from tkinter import ttk, messagebox
import threading

from main import main
from visualize import plot_results


def run_gui():
    root = tk.Tk()
    root.title("Genetic Scheduler")
    root.resizable(False, False)

    frame = ttk.Frame(root, padding=24)
    frame.grid(row=0, column=0)

    ttk.Label(frame, text="Genetic Scheduler", font=("", 13, "bold")).grid(
        row=0, column=0, columnspan=2, pady=(0, 16)
    )

    ttk.Label(frame, text="Generations:").grid(row=1, column=0, sticky="w", pady=5)
    gen_var = tk.StringVar(value="100")
    ttk.Entry(frame, textvariable=gen_var, width=10).grid(row=1, column=1, padx=10)

    ttk.Label(frame, text="Population size:").grid(row=2, column=0, sticky="w", pady=5)
    pop_var = tk.StringVar(value="500")
    ttk.Entry(frame, textvariable=pop_var, width=10).grid(row=2, column=1, padx=10)

    ttk.Label(frame, text="Mutation rate (0–1):").grid(row=3, column=0, sticky="w", pady=5)
    mut_var = tk.StringVar(value="0.01")
    ttk.Entry(frame, textvariable=mut_var, width=10).grid(row=3, column=1, padx=10)

    status_var = tk.StringVar(value="")
    ttk.Label(frame, textvariable=status_var, foreground="gray").grid(
        row=5, column=0, columnspan=2, pady=(6, 0)
    )

    def on_run():
        try:
            generations = int(gen_var.get())
            pop_size = int(pop_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Generations and population size must be integers.")
            return
        try:
            mutation_rate = float(mut_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Mutation rate must be a number.")
            return
        if generations < 1:
            messagebox.showerror("Invalid input", "Generations must be at least 1.")
            return
        if pop_size < 4:
            messagebox.showerror("Invalid input", "Population size must be at least 4.")
            return
        if not 0.0 <= mutation_rate <= 1.0:
            messagebox.showerror("Invalid input", "Mutation rate must be between 0 and 1.")
            return

        run_btn.config(state="disabled")
        status_var.set("Running...")

        def task():
            history, best = main(generations=generations, population_size=pop_size, mutation_rate=mutation_rate)
            root.after(0, lambda: on_done(history, best))

        threading.Thread(target=task, daemon=True).start()

    def on_done(history, best):
        run_btn.config(state="normal")
        status_var.set(f"Done — best score: {best.score:.2f}")
        plot_results(history, best, parent=root)

    run_btn = ttk.Button(frame, text="Run", command=on_run)
    run_btn.grid(row=4, column=0, columnspan=2, pady=14)

    root.mainloop()


if __name__ == "__main__":
    run_gui()

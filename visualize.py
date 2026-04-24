import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches
from matplotlib import cm
import numpy as np

from core_data import FACILITATORS, TIMES, ROOMS


def _make_tab(notebook, title, figsize):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=title)
    fig = Figure(figsize=figsize, dpi=100)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
    return fig, canvas


def _fitness_tab(notebook, title, generations, scores, color, linestyle="-"):
    fig, canvas = _make_tab(notebook, title, figsize=(9, 5))
    ax = fig.add_subplot(111)
    ax.plot(generations, scores, color=color, linewidth=2, linestyle=linestyle)
    ax.set_title(title)
    ax.set_xlabel("Generation")
    ax.set_ylabel("Fitness Score")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    canvas.draw()


def _schedule_tab(notebook, best_schedule):
    fig, canvas = _make_tab(notebook, "Schedule", figsize=(11, 6))
    ax = fig.add_subplot(111)

    assignments = best_schedule.assignments
    room_list = list(ROOMS.keys())
    facilitator_to_idx = {f: i for i, f in enumerate(FACILITATORS)}
    tab10 = cm.get_cmap("tab10")
    colors = [tab10(i) for i in range(len(FACILITATORS))]

    grid_fac = np.full((len(TIMES), len(room_list)), np.nan)
    grid_text = [["" for _ in room_list] for _ in TIMES]

    for activity, assignment in assignments.items():
        t_idx = TIMES.index(assignment["time"])
        r_idx = room_list.index(assignment["room"])
        grid_fac[t_idx, r_idx] = facilitator_to_idx[assignment["facilitator"]]
        grid_text[t_idx][r_idx] = f"{activity}\n{assignment['facilitator']}"

    cmap = cm.get_cmap("tab10").copy()
    cmap.set_bad(color="#eeeeee")
    masked = np.ma.masked_invalid(grid_fac)

    ax.imshow(masked, cmap=cmap, vmin=0, vmax=len(FACILITATORS) - 1, aspect="auto")

    for t_idx in range(len(TIMES)):
        for r_idx in range(len(room_list)):
            text = grid_text[t_idx][r_idx]
            if text:
                ax.text(r_idx, t_idx, text, ha="center", va="center",
                        fontsize=7.5, color="white", fontweight="bold")

    ax.set_xticks(range(len(room_list)))
    ax.set_xticklabels(room_list, rotation=30, ha="right", fontsize=8)
    ax.set_yticks(range(len(TIMES)))
    ax.set_yticklabels(TIMES, fontsize=9)
    ax.set_xticks(np.arange(-0.5, len(room_list), 1), minor=True)
    ax.set_yticks(np.arange(-0.5, len(TIMES), 1), minor=True)
    ax.grid(which="minor", color="white", linestyle="-", linewidth=1.5)
    ax.tick_params(which="minor", bottom=False, left=False)
    ax.set_title(f"Best Schedule  (score: {best_schedule.score:.2f})")

    patches = [mpatches.Patch(color=colors[i], label=f) for i, f in enumerate(FACILITATORS)]
    ax.legend(handles=patches, bbox_to_anchor=(1.02, 1), loc="upper left",
              fontsize=7.5, title="Facilitator")

    fig.tight_layout()
    canvas.draw()


def plot_results(history, best_schedule, parent=None):
    standalone = parent is None
    win = tk.Tk() if standalone else tk.Toplevel(parent)
    win.title("Genetic Scheduler — Results")
    win.geometry("960x580")

    notebook = ttk.Notebook(win)
    notebook.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    generations = [h["generation"] for h in history]
    _fitness_tab(notebook, "Best Fitness",    generations, [h["best"]  for h in history], "#2ca02c")
    _fitness_tab(notebook, "Average Fitness", generations, [h["avg"]   for h in history], "#1f77b4", linestyle="--")
    _fitness_tab(notebook, "Worst Fitness",   generations, [h["worst"] for h in history], "#d62728", linestyle=":")
    _schedule_tab(notebook, best_schedule)

    if standalone:
        win.mainloop()

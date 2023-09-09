import tkinter as tk
from database import get_assignments, get_assignment_by_title

class GradingManager(tk.Frame):
    def __init__(self, parent, show_grading_assignment):
        super().__init__(parent)
        self.show_grading_assignment = show_grading_assignment
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Grading Manager")
        self.label.pack(pady=10)

        self.grade_button = tk.Button(self, text="Grade Assignment", command=self.show_grading_assignment)
        self.grade_button.pack()

        self.assignment_listbox = tk.Listbox(self)
        self.assignment_listbox.pack()

        self.load_assignments()
        self.assignment_listbox.bind("<Double-Button-1>", self.grade_selected_assignment)

    def load_assignments(self):
        assignments = get_assignments()
        self.assignment_listbox.delete(0, tk.END)
        for assignment in assignments:
            if "graded" not in assignment or not assignment["graded"]:
                self.assignment_listbox.insert(tk.END, assignment["title"])

    def grade_selected_assignment(self, event):
        selected_index = self.assignment_listbox.curselection()
        if selected_index:
            assignment_index = selected_index[0]
            assignment_title = self.assignment_listbox.get(assignment_index)
            assignment = get_assignment_by_title(assignment_title)  # Implement this function
            if assignment:
                self.show_grading_assignment(assignment)

class GradingAssignment(tk.Toplevel):
    def __init__(self, parent, assignment):
        super().__init__(parent)
        self.assignment = assignment
        self.create_widgets()

    def create_widgets(self):
        self.title("Grading Assignment")
        # Create a form for grading the assignment (e.g., grade, feedback, etc.)

# You can expand this module with additional grading-related functionality as needed.

import tkinter as tk
from database import get_assignments, get_assignment_by_title

class FeedbackManager(tk.Frame):
    def __init__(self, parent, show_feedback_assignment):
        super().__init__(parent)
        self.show_feedback_assignment = show_feedback_assignment
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Feedback Manager")
        self.label.pack(pady=10)

        self.feedback_button = tk.Button(self, text="Provide Feedback", command=self.show_feedback_assignment)
        self.feedback_button.pack()

        self.assignment_listbox = tk.Listbox(self)
        self.assignment_listbox.pack()

        self.load_assignments()
        self.assignment_listbox.bind("<Double-Button-1>", self.view_feedback_assignment)

    def load_assignments(self):
        assignments = get_assignments()
        self.assignment_listbox.delete(0, tk.END)
        for assignment in assignments:
            if "graded" in assignment and assignment["graded"] and "feedback" not in assignment:
                self.assignment_listbox.insert(tk.END, assignment["title"])

    def view_feedback_assignment(self, event):
        selected_index = self.assignment_listbox.curselection()
        if selected_index:
            assignment_index = selected_index[0]
            assignment_title = self.assignment_listbox.get(assignment_index)
            assignment = get_assignment_by_title(assignment_title)  # Implement this function
            if assignment:
                self.show_feedback_assignment(assignment)

class FeedbackAssignment(tk.Toplevel):
    def __init__(self, parent, assignment):
        super().__init__(parent)
        self.assignment = assignment
        self.create_widgets()

    def create_widgets(self):
        self.title("Feedback Assignment")
        # Create a form for providing feedback (e.g., feedback text, comments, etc.)

# You can expand this module with additional feedback-related functionality as needed.

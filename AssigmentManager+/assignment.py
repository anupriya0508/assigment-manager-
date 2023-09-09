import tkinter as tk
from tkinter import messagebox
from database import insert_assignment, get_assignments, get_assignment_by_id


class AssignmentManager(tk.Frame):
    def __init__(self, parent, show_assignment_submission, show_assignment_details):
        super().__init__(parent)
        self.show_assignment_submission = show_assignment_submission
        self.show_assignment_details = show_assignment_details
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self, text="Assignment Manager")
        self.label.pack(pady=10)

        self.submit_button = tk.Button(self, text="Submit Assignment", command=self.show_assignment_submission)
        self.submit_button.pack()

        self.assignment_listbox = tk.Listbox(self)
        self.assignment_listbox.pack()

        self.load_assignments()
        self.assignment_listbox.bind("<Double-Button-1>", self.view_assignment_details)

    def load_assignments(self):
        assignments = get_assignments()
        self.assignment_listbox.delete(0, tk.END)
        for assignment in assignments:
            self.assignment_listbox.insert(tk.END, assignment["title"])

    def view_assignment_details(self, event):
        selected_index = self.assignment_listbox.curselection()
        if selected_index:
            assignment_index = selected_index[0]
            assignment_title = self.assignment_listbox.get(assignment_index)
            assignment = get_assignment_by_title(assignment_title)  # Implement this function
            if assignment:
                self.show_assignment_details(assignment)


class AssignmentSubmission(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.create_widgets()

    def create_widgets(self):
        self.title("Assignment Submission")

        self.assignment_label = tk.Label(self, text="Assignment Title:")
        self.assignment_label.pack(pady=5)
        self.assignment_entry = tk.Entry(self)
        self.assignment_entry.pack()

        self.text_label = tk.Label(self, text="Assignment Text:")
        self.text_label.pack(pady=5)
        self.text_entry = tk.Text(self, height=10, width=40)
        self.text_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.submit_assignment)
        self.submit_button.pack()

    def submit_assignment(self):
        title = self.assignment_entry.get()
        text = self.text_entry.get("1.0", "end-1c")

        if not title or not text:
            messagebox.showerror("Error", "Title and text cannot be empty.")
            return

        assignment_data = {
            "title": title,
            "text": text,
        }

        # Insert the assignment into the database using pymongo
        assignment_id = insert_assignment(assignment_data)

        if assignment_id:
            messagebox.showinfo("Success", "Assignment submitted successfully.")
            self.destroy()
            self.parent.update_assignment_list()


class AssignmentDetails(tk.Toplevel):
    def __init__(self, parent, assignment):
        super().__init__(parent)
        self.assignment = assignment
        self.create_widgets()

    def create_widgets(self):
        self.title("Assignment Details")

        title_label = tk.Label(self, text="Title:")
        title_label.pack()
        title_text = tk.Label(self, text=self.assignment["title"])
        title_text.pack()

        text_label = tk.Label(self, text="Text:")
        text_label.pack()
        text_text = tk.Label(self, text=self.assignment["text"])
        text_text.pack()

# You can expand this module with additional assignment-related functionality as needed.

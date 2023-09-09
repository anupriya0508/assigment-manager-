import tkinter as tk
from gui import Application
from user import UserManager
from assignment import AssignmentManager, AssignmentSubmission, AssignmentDetails
from grading import GradingManager, GradingAssignment
from feedback import FeedbackManager, FeedbackAssignment

def show_assignment_manager():
    assignment_manager.pack()
    grading_manager.pack_forget()
    feedback_manager.pack_forget()

def show_assignment_submission():
    assignment_manager.pack_forget()
    grading_manager.pack_forget()
    feedback_manager.pack_forget()
    assignment_submission = AssignmentSubmission(root)
    assignment_submission.mainloop()

def show_assignment_details(assignment):
    assignment_details = AssignmentDetails(root, assignment)
    assignment_details.mainloop()

def show_grading_assignment(assignment):
    grading_assignment = GradingAssignment(root, assignment)
    grading_assignment.mainloop()

def show_feedback_assignment(assignment):
    feedback_assignment = FeedbackAssignment(root, assignment)
    feedback_assignment.mainloop()

if __name__ == "__main__":
    root = tk.Tk()

    # Create instances of manager classes
    user_manager = UserManager(root, show_assignment_manager)
    assignment_manager = AssignmentManager(root, show_assignment_submission, show_assignment_details)
    grading_manager = GradingManager(root, show_grading_assignment)
    feedback_manager = FeedbackManager(root, show_feedback_assignment)

    # Create the Application instance with manager instances
    app = Application(root, user_manager, assignment_manager, grading_manager, feedback_manager)
    app.run()

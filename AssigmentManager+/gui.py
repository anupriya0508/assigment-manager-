from assignment import AssignmentManager
from grading import GradingManager
from feedback import FeedbackManager
from user import UserManager

class Application:
    def __init__(self, root, user_manager, assignment_manager, grading_manager, feedback_manager):
        self.root = root
        self.root.title("Assignment Manager+")
        self.user_manager = user_manager
        self.assignment_manager = assignment_manager
        self.grading_manager = grading_manager
        self.feedback_manager = feedback_manager
        self.show_login()

    def show_login(self):
        self.user_manager.pack()
        self.assignment_manager.pack_forget()
        self.grading_manager.pack_forget()
        self.feedback_manager.pack_forget()

    def show_assignment_manager(self):
        self.user_manager.pack_forget()
        self.assignment_manager.pack()
        self.grading_manager.pack_forget()
        self.feedback_manager.pack_forget()

    def show_grading_manager(self):
        self.user_manager.pack_forget()
        self.assignment_manager.pack_forget()
        self.grading_manager.pack()
        self.feedback_manager.pack_forget()

    def show_feedback_manager(self):
        self.user_manager.pack_forget()
        self.assignment_manager.pack_forget()
        self.grading_manager.pack_forget()
        self.feedback_manager.pack()

    def run(self):
        self.root.mainloop()

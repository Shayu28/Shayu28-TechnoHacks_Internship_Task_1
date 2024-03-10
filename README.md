# TechnoHacks_Internship_Task_1

ALGORITHM:

Initialize the TodoListApp:
Set up the main window with title, geometry, and theme.
Create input fields for task and deadline, and configure placeholders.
Bind events for input fields to clear and restore placeholders.
Create buttons for adding, marking tasks as done, deleting, and viewing statistics.
Load tasks from a JSON file.

Event Handling:
clear_placeholder: Clears the placeholder text when an input field is clicked.
restore_placeholder: Restores the placeholder text if the input field is empty.
add_task: Adds a task to the list if both task and deadline are entered correctly.
mark_done: Marks a selected task as done (changes text color to green).
delete_task: Deletes a selected task from the list.

Task List Management:
view_stats: Calculates and displays total and completed task counts.
load_tasks: Loads tasks from a JSON file into the list.
save_tasks: Saves tasks from the list to a JSON file.

Main Loop:
Create an instance of TodoListApp and start the main event loop.

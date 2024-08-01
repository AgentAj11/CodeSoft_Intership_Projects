import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# File to store contacts
CONTACTS_FILE = 'contacts.json'

def read_contacts():
    """Read contacts from the JSON file."""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

def write_contacts(contacts):
    """Write contacts to the JSON file."""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    """Add a new contact."""
    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone or not email or not address:
        messagebox.showerror("Input Error", "Please enter all contact details")
        return

    contacts = read_contacts()
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    write_contacts(contacts)
    refresh_contacts()
    clear_entries()

def view_contacts():
    """Display all contacts."""
    contacts = read_contacts()
    for widget in frame_list_buttons.winfo_children():
        widget.destroy()  # Clear existing buttons

    for index, contact in enumerate(contacts):
        contact_button = tk.Button(frame_list_buttons, text=f"{contact['name']} - {contact['phone']}",
                                  command=lambda idx=index: show_contact_info(idx))
        contact_button.pack(pady=2, fill=tk.X)

def show_contact_info(index):
    """Show detailed information about the selected contact."""
    contacts = read_contacts()
    contact = contacts[index]
    info = f"Name: {contact['name']}\nPhone: {contact['phone']}\nEmail: {contact['email']}\nAddress: {contact['address']}"
    messagebox.showinfo("Contact Information", info)

def search_contact():
    """Search for a contact by name or phone number."""
    search_term = entry_search.get()
    if not search_term:
        messagebox.showerror("Input Error", "Please enter a name or phone number to search")
        return

    contacts = read_contacts()
    for widget in frame_list_buttons.winfo_children():
        widget.destroy()  # Clear existing buttons

    for index, contact in enumerate(contacts):
        if search_term.lower() in contact['name'].lower() or search_term in contact['phone']:
            contact_button = tk.Button(frame_list_buttons, text=f"{contact['name']} - {contact['phone']}",
                                      command=lambda idx=index: show_contact_info(idx))
            contact_button.pack(pady=2, fill=tk.X)

def update_contact():
    """Update selected contact."""
    selected_contact = listbox_contacts.curselection()
    if not selected_contact:
        messagebox.showerror("Selection Error", "Please select a contact to update")
        return

    index = selected_contact[0]
    contacts = read_contacts()

    name = entry_name.get()
    phone = entry_phone.get()
    email = entry_email.get()
    address = entry_address.get()

    if not name or not phone or not email or not address:
        messagebox.showerror("Input Error", "Please enter all contact details")
        return

    contacts[index] = {"name": name, "phone": phone, "email": email, "address": address}
    write_contacts(contacts)
    refresh_contacts()
    clear_entries()

def delete_contact():
    """Delete selected contact."""
    selected_contact = listbox_contacts.curselection()
    if not selected_contact:
        messagebox.showerror("Selection Error", "Please select a contact to delete")
        return

    index = selected_contact[0]
    contacts = read_contacts()
    contacts.pop(index)
    write_contacts(contacts)
    refresh_contacts()

def refresh_contacts():
    """Refresh the contact list display."""
    view_contacts()

def clear_entries():
    """Clear input entries."""
    entry_name.delete(0, tk.END)
    entry_phone.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_address.delete(0, tk.END)

# Initialize main window
root = tk.Tk()
root.title("Contact Management System")

# Frame for contact details
frame_details = tk.Frame(root)
frame_details.pack(pady=10)

label_name = tk.Label(frame_details, text="Name:")
label_name.pack(side=tk.LEFT, padx=5, pady=5)
entry_name = tk.Entry(frame_details)
entry_name.pack(side=tk.LEFT, padx=5, pady=5)

label_phone = tk.Label(frame_details, text="Phone:")
label_phone.pack(side=tk.LEFT, padx=5, pady=5)
entry_phone = tk.Entry(frame_details)
entry_phone.pack(side=tk.LEFT, padx=5, pady=5)

label_email = tk.Label(frame_details, text="Email:")
label_email.pack(side=tk.LEFT, padx=5, pady=5)
entry_email = tk.Entry(frame_details)
entry_email.pack(side=tk.LEFT, padx=5, pady=5)

label_address = tk.Label(frame_details, text="Address:")
label_address.pack(side=tk.LEFT, padx=5, pady=5)
entry_address = tk.Entry(frame_details)
entry_address.pack(side=tk.LEFT, padx=5, pady=5)

btn_add = tk.Button(frame_details, text="Add Contact", command=add_contact)
btn_add.pack(pady=10)

# Frame for contact list and operations
frame_list = tk.Frame(root)
frame_list.pack(pady=10)

# Frame for contact buttons
frame_list_buttons = tk.Frame(frame_list)
frame_list_buttons.pack(pady=10)

btn_view = tk.Button(frame_list, text="View Contacts", command=view_contacts)
btn_view.pack(side=tk.LEFT, padx=5)

label_search = tk.Label(frame_list, text="Search:")
label_search.pack(side=tk.LEFT, padx=5)
entry_search = tk.Entry(frame_list)
entry_search.pack(side=tk.LEFT, padx=5)

btn_search = tk.Button(frame_list, text="Search", command=search_contact)
btn_search.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(frame_list, text="Update Contact", command=update_contact)
btn_update.pack(side=tk.LEFT, padx=5, pady=10)

btn_delete = tk.Button(frame_list, text="Delete Contact", command=delete_contact)
btn_delete.pack(side=tk.LEFT, padx=5, pady=10)

btn_clear = tk.Button(frame_list, text="Clear Fields", command=clear_entries)
btn_clear.pack(side=tk.LEFT, padx=5, pady=10)

# Start the GUI event loop
root.mainloop()

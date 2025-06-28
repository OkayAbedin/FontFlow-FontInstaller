#!/usr/bin/env python3
"""
Simple Windows Font Installer
A modern GUI application to install TTF and OTF fonts from ZIP files.
"""

import os
import sys
import shutil
import zipfile
import tempfile
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import ctypes
from ctypes import wintypes
import threading
from typing import List, Set

# Windows API constants
HWND_BROADCAST = 0xFFFF
WM_FONTCHANGE = 0x001D
SMTO_ABORTIFHUNG = 0x0002

class FontInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_gui()
        self.font_extensions = {'.ttf', '.otf', '.ttc', '.otc'}
        
    def setup_window(self):
        """Configure the main window with modern styling."""
        self.root.title("Font Installer")
        self.root.geometry("600x500")
        self.root.minsize(500, 400)
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (600 // 2)
        y = (self.root.winfo_screenheight() // 2) - (500 // 2)
        self.root.geometry(f"600x500+{x}+{y}")
        
        # Configure modern style
        style = ttk.Style()
        style.theme_use('winnative')
        
    def setup_gui(self):
        """Create the modern GUI interface."""
        # Main container with padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(2, weight=1)
        
        # Title
        title_label = ttk.Label(
            main_frame, 
            text="Font Installer", 
            font=('Segoe UI', 18, 'bold')
        )
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Description
        desc_text = "Select ZIP files containing TTF or OTF fonts to install them automatically.\n"
        
        # Check admin privileges and add appropriate message
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if is_admin:
                desc_text += "Running as Administrator - fonts will be installed system-wide."
            else:
                desc_text += "Running without Administrator privileges - fonts will be installed for current user only."
        except:
            desc_text += "Admin status unknown - fonts will install where permissions allow."
            
        desc_label = ttk.Label(
            main_frame,
            text=desc_text,
            font=('Segoe UI', 10),
            foreground='gray',
            justify=tk.CENTER
        )
        desc_label.grid(row=1, column=0, columnspan=3, pady=(0, 20))
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="Select Font Archives", padding="10")
        file_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 20))
        file_frame.columnconfigure(0, weight=1)
        file_frame.rowconfigure(1, weight=1)
        
        # File selection button
        self.select_btn = ttk.Button(
            file_frame,
            text="Select ZIP Files",
            command=self.select_files,
            style='Accent.TButton'
        )
        self.select_btn.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Selected files listbox
        listbox_frame = ttk.Frame(file_frame)
        listbox_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        listbox_frame.columnconfigure(0, weight=1)
        listbox_frame.rowconfigure(0, weight=1)
        
        self.files_listbox = tk.Listbox(
            listbox_frame,
            height=8,
            font=('Segoe UI', 9),
            selectmode=tk.EXTENDED
        )
        self.files_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Scrollbar for listbox
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.files_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.files_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Clear button
        self.clear_btn = ttk.Button(
            file_frame,
            text="Clear List",
            command=self.clear_files,
            state=tk.DISABLED
        )
        self.clear_btn.grid(row=2, column=0, sticky=(tk.W), pady=(10, 0))
        
        # Progress frame
        progress_frame = ttk.LabelFrame(main_frame, text="Installation Progress", padding="10")
        progress_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 20))
        progress_frame.columnconfigure(0, weight=1)
        
        # Progress bar
        self.progress = ttk.Progressbar(
            progress_frame,
            mode='indeterminate',
            length=400
        )
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(
            progress_frame,
            text="Ready to install fonts",
            font=('Segoe UI', 9)
        )
        self.status_label.grid(row=1, column=0, sticky=(tk.W))
        
        # Install button
        self.install_btn = ttk.Button(
            main_frame,
            text="Install Fonts",
            command=self.install_fonts,
            state=tk.DISABLED,
            style='Accent.TButton'
        )
        self.install_btn.grid(row=4, column=0, columnspan=3, pady=(0, 10))
        
        # Exit button
        exit_btn = ttk.Button(
            main_frame,
            text="Exit",
            command=self.root.quit
        )
        exit_btn.grid(row=5, column=0, columnspan=3)
        
        # Configure accent button style
        style = ttk.Style()
        style.configure('Accent.TButton', font=('Segoe UI', 10, 'bold'))
        
        self.selected_files = []
        
    def select_files(self):
        """Open file dialog to select ZIP files."""
        files = filedialog.askopenfilenames(
            title="Select ZIP files containing fonts",
            filetypes=[
                ("ZIP files", "*.zip"),
                ("All files", "*.*")
            ]
        )
        
        if files:
            self.selected_files.extend(files)
            self.update_files_display()
            self.update_button_states()
            
    def clear_files(self):
        """Clear the selected files list."""
        self.selected_files.clear()
        self.update_files_display()
        self.update_button_states()
        
    def update_files_display(self):
        """Update the listbox with selected files."""
        self.files_listbox.delete(0, tk.END)
        for file_path in self.selected_files:
            filename = os.path.basename(file_path)
            self.files_listbox.insert(tk.END, filename)
            
    def update_button_states(self):
        """Update button states based on selected files."""
        has_files = len(self.selected_files) > 0
        self.install_btn.config(state=tk.NORMAL if has_files else tk.DISABLED)
        self.clear_btn.config(state=tk.NORMAL if has_files else tk.DISABLED)
        
    def extract_fonts_from_zip(self, zip_path: str, temp_dir: str) -> List[str]:
        """Extract font files from a ZIP archive."""
        font_files = []
        
        try:
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                for file_info in zip_ref.infolist():
                    if not file_info.is_dir():
                        file_ext = Path(file_info.filename).suffix.lower()
                        if file_ext in self.font_extensions:
                            # Extract to temp directory
                            extracted_path = zip_ref.extract(file_info, temp_dir)
                            font_files.append(extracted_path)
                            
        except zipfile.BadZipFile:
            messagebox.showerror("Error", f"Invalid ZIP file: {os.path.basename(zip_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Error extracting {os.path.basename(zip_path)}: {str(e)}")
            
        return font_files
        
    def install_font_file(self, font_path: str) -> tuple[bool, str]:
        """Install a single font file using Windows API with fallback to user installation."""
        font_filename = os.path.basename(font_path)
        
        # Try system-wide installation first (requires admin)
        try:
            system_fonts_dir = os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'Fonts')
            system_dest_path = os.path.join(system_fonts_dir, font_filename)
            
            # Copy font file to Windows Fonts directory
            shutil.copy2(font_path, system_dest_path)
            
            # Register the font with Windows
            gdi32 = ctypes.windll.gdi32
            user32 = ctypes.windll.user32
            
            # Add font resource
            result = gdi32.AddFontResourceW(system_dest_path)
            
            if result > 0:
                # Notify all windows that fonts have changed
                user32.SendMessageTimeoutW(
                    HWND_BROADCAST,
                    WM_FONTCHANGE,
                    0,
                    0,
                    SMTO_ABORTIFHUNG,
                    1000,
                    None
                )
                return True, "system-wide"
            else:
                # If AddFontResource failed, remove the copied file
                try:
                    os.remove(system_dest_path)
                except:
                    pass
                    
        except PermissionError:
            # Fall back to user-level installation
            pass
        except Exception as e:
            print(f"System installation failed for {font_filename}: {str(e)}")
        
        # Try user-level installation (no admin required)
        try:
            # Get user fonts directory
            user_fonts_dir = os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Microsoft', 'Windows', 'Fonts')
            
            # Create user fonts directory if it doesn't exist
            os.makedirs(user_fonts_dir, exist_ok=True)
            
            user_dest_path = os.path.join(user_fonts_dir, font_filename)
            
            # Copy font file to user fonts directory
            shutil.copy2(font_path, user_dest_path)
            
            # Register the font with Windows (user-level)
            gdi32 = ctypes.windll.gdi32
            user32 = ctypes.windll.user32
            
            # Add font resource
            result = gdi32.AddFontResourceW(user_dest_path)
            
            if result > 0:
                # Notify all windows that fonts have changed
                user32.SendMessageTimeoutW(
                    HWND_BROADCAST,
                    WM_FONTCHANGE,
                    0,
                    0,
                    SMTO_ABORTIFHUNG,
                    1000,
                    None
                )
                return True, "user-level"
            else:
                # If AddFontResource failed, remove the copied file
                try:
                    os.remove(user_dest_path)
                except:
                    pass
                return False, "registration failed"
                
        except Exception as e:
            print(f"User installation failed for {font_filename}: {str(e)}")
            return False, f"error: {str(e)}"
            
    def install_fonts_thread(self):
        """Install fonts in a separate thread to prevent GUI freezing."""
        installed_count = 0
        total_fonts = 0
        system_installs = 0
        user_installs = 0
        failed_installs = []
        
        # Update status
        self.root.after(0, lambda: self.status_label.config(text="Extracting fonts from archives..."))
        self.root.after(0, self.progress.start)
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                all_font_files = []
                
                # Extract all fonts from ZIP files
                for zip_path in self.selected_files:
                    self.root.after(0, lambda z=zip_path: self.status_label.config(
                        text=f"Extracting: {os.path.basename(z)}"
                    ))
                    
                    font_files = self.extract_fonts_from_zip(zip_path, temp_dir)
                    all_font_files.extend(font_files)
                    
                total_fonts = len(all_font_files)
                
                if total_fonts == 0:
                    self.root.after(0, lambda: messagebox.showwarning(
                        "No Fonts Found",
                        "No TTF or OTF font files were found in the selected ZIP archives."
                    ))
                    return
                    
                # Install each font
                self.root.after(0, lambda: self.status_label.config(text="Installing fonts..."))
                
                for i, font_path in enumerate(all_font_files):
                    font_name = os.path.basename(font_path)
                    self.root.after(0, lambda fn=font_name, prog=i+1, tot=total_fonts: self.status_label.config(
                        text=f"Installing ({prog}/{tot}): {fn}"
                    ))
                    
                    success, install_type = self.install_font_file(font_path)
                    if success:
                        installed_count += 1
                        if install_type == "system-wide":
                            system_installs += 1
                        elif install_type == "user-level":
                            user_installs += 1
                    else:
                        failed_installs.append((font_name, install_type))
                        
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Installation Error",
                f"An error occurred during installation: {str(e)}"
            ))
        finally:
            # Update UI in main thread
            self.root.after(0, self.progress.stop)
            self.root.after(0, lambda: self.status_label.config(
                text=f"Installation complete: {installed_count}/{total_fonts} fonts installed"
            ))
            
            # Prepare detailed completion message
            if installed_count > 0:
                message_parts = [f"Successfully installed {installed_count} out of {total_fonts} fonts:"]
                
                if system_installs > 0:
                    message_parts.append(f"• {system_installs} fonts installed system-wide (available to all users)")
                
                if user_installs > 0:
                    message_parts.append(f"• {user_installs} fonts installed for current user only")
                    
                if failed_installs:
                    message_parts.append(f"\n{len(failed_installs)} fonts failed to install:")
                    for font_name, reason in failed_installs[:5]:  # Show first 5 failures
                        message_parts.append(f"  - {font_name}: {reason}")
                    if len(failed_installs) > 5:
                        message_parts.append(f"  ... and {len(failed_installs) - 5} more")
                
                message_parts.append("\nThe fonts are now available in your applications.")
                
                self.root.after(0, lambda: messagebox.showinfo(
                    "Installation Complete",
                    "\n".join(message_parts)
                ))
            else:
                failure_details = "\n".join([f"• {name}: {reason}" for name, reason in failed_installs[:10]])
                if len(failed_installs) > 10:
                    failure_details += f"\n... and {len(failed_installs) - 10} more failures"
                    
                self.root.after(0, lambda: messagebox.showerror(
                    "Installation Failed",
                    f"No fonts were successfully installed.\n\nFailure details:\n{failure_details}\n\n"
                    "Try running as Administrator for system-wide installation."
                ))
                
            # Re-enable buttons
            self.root.after(0, lambda: self.install_btn.config(state=tk.NORMAL))
            self.root.after(0, lambda: self.select_btn.config(state=tk.NORMAL))
            
    def install_fonts(self):
        """Start font installation process."""
        if not self.selected_files:
            messagebox.showwarning("No Files Selected", "Please select ZIP files containing fonts first.")
            return
            
        # Disable buttons during installation
        self.install_btn.config(state=tk.DISABLED)
        self.select_btn.config(state=tk.DISABLED)
        
        # Start installation in separate thread
        thread = threading.Thread(target=self.install_fonts_thread, daemon=True)
        thread.start()
        
    def run(self):
        """Run the application."""
        self.root.mainloop()

def main():
    """Main entry point."""
    # Check if running on Windows
    if sys.platform != 'win32':
        print("This application is designed for Windows only.")
        sys.exit(1)
        
    # Check for admin privileges (recommended but not required)
    try:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin()
        if not is_admin:
            print("Note: Running without administrator privileges. Some fonts may not install properly.")
    except:
        pass
        
    # Create and run the application
    app = FontInstaller()
    app.run()

if __name__ == "__main__":
    main()

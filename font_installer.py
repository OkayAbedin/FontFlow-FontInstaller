#!/usr/bin/env python3
"""
FontFlow - A modern GUI application to install TTF and OTF fonts from ZIP files.
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
import winreg
try:
    from PIL import Image, ImageTk
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

# Windows API constants
HWND_BROADCAST = 0xFFFF
WM_FONTCHANGE = 0x001D
SMTO_ABORTIFHUNG = 0x0002

class FontInstaller:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_modern_style()  # Setup styles before GUI
        self.setup_gui()
        self.font_extensions = {'.ttf', '.otf', '.ttc', '.otc'}
        
    def setup_window(self):
        """Configure the main window with modern styling."""
        self.root.title("FontFlow")
        
        # Set App User Model ID for Windows taskbar icon
        try:
            # This ensures Windows shows the correct icon in the taskbar
            myappid = 'okayabedin.fontflow.installer.1.0'
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
        except Exception:
            pass
        
        # Set window icon
        try:
            # Prefer .ico file for Windows compatibility
            if os.path.exists("icon.ico"):
                self.root.iconbitmap("icon.ico")
            elif os.path.exists("icon.png"):
                # Fallback to PNG using iconphoto
                icon_image = tk.PhotoImage(file="icon.png")
                self.root.iconphoto(True, icon_image)
        except Exception:
            pass  # Continue without icon if there's any issue
            
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (840 // 2)
        y = (self.root.winfo_screenheight() // 2) - (680 // 2)
        self.root.geometry(f"840x680+{x}+{y}")
        self.root.minsize(400, 600)
        
        # Modern dark color scheme
        self.colors = {
            'bg': '#1a1a1a',           # Dark background
            'surface': '#2d2d2d',       # Dark surface
            'primary': '#007acc',      # Modern blue
            'primary_hover': '#005a9e', # Darker blue
            'secondary': '#858585',    # Light gray
            'success': '#28a745',      # Green
            'danger': '#dc3545',       # Red
            'warning': '#ffc107',      # Orange
            'text': '#ffffff',         # Light text
            'text_muted': '#b3b3b3',   # Muted light text
            'border': '#404040'        # Dark border
        }
        
        # Set window background
        self.root.configure(bg=self.colors['bg'])
        
        # Center the window
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (840 // 2)
        y = (self.root.winfo_screenheight() // 2) - (680 // 2)
        self.root.geometry(f"840x680+{x}+{y}")
        
        # Configure modern style
        self.setup_modern_style()
        
    def setup_gui(self):
        """Create the modern GUI interface."""
        # Main container with reduced padding for more compact layout
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)  # File selection should expand
        
        # Header section
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        header_frame.columnconfigure(0, weight=1)
        
        # Title with modern typography and icon
        title_frame = ttk.Frame(header_frame)
        title_frame.grid(row=0, column=0, pady=(0, 5))
        
        # Load and display icon
        icon_loaded = False
        try:
            if PIL_AVAILABLE:
                # Try to load .ico file first
                if os.path.exists("icon.ico"):
                    img = Image.open("icon.ico")
                    img = img.resize((32, 32), Image.Resampling.LANCZOS)
                    icon_img = ImageTk.PhotoImage(img)
                    icon_label = ttk.Label(title_frame, image=icon_img)
                    icon_label.image = icon_img  # Keep a reference
                    icon_label.grid(row=0, column=0, padx=(0, 10))
                    icon_loaded = True
                elif os.path.exists("icon.png"):
                    img = Image.open("icon.png")
                    img = img.resize((32, 32), Image.Resampling.LANCZOS)
                    icon_img = ImageTk.PhotoImage(img)
                    icon_label = ttk.Label(title_frame, image=icon_img)
                    icon_label.image = icon_img  # Keep a reference
                    icon_label.grid(row=0, column=0, padx=(0, 10))
                    icon_loaded = True
            elif os.path.exists("icon.png"):
                # Fallback to tk.PhotoImage for PNG if PIL not available
                icon_img = tk.PhotoImage(file="icon.png")
                # Resize icon to fit nicely in the title (32x32 pixels)
                subsample_x = max(1, icon_img.width() // 32)
                subsample_y = max(1, icon_img.height() // 32)
                icon_img = icon_img.subsample(subsample_x, subsample_y)
                icon_label = ttk.Label(title_frame, image=icon_img)
                icon_label.image = icon_img  # Keep a reference
                icon_label.grid(row=0, column=0, padx=(0, 10))
                icon_loaded = True
        except Exception as e:
            pass  # Will use emoji fallback
        
        if not icon_loaded:
            # Fallback to emoji if icon can't be loaded
            icon_label = ttk.Label(title_frame, text="🎨", style='Title.TLabel')
            icon_label.grid(row=0, column=0, padx=(0, 5))
        
        title_label = ttk.Label(
            title_frame, 
            text="FontFlow", 
            style='Title.TLabel'
        )
        title_label.grid(row=0, column=1)
        
        # Modern description with permission info
        desc_text = "Install TTF and OTF fonts from ZIP archives with one click\n"

        # Ensure the application is running with administrator privileges
        try:
            is_admin = ctypes.windll.shell32.IsUserAnAdmin()
            if not is_admin:
                print("This application requires administrator privileges to run.")
                ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, "".join(sys.argv), None, 1)
                sys.exit(0)
        except Exception as e:
            print(f"Error checking administrator privileges: {e}")
            sys.exit(1)

        desc_text += "🔐 Administrator mode is required for system-wide installation"
        
        desc_label = ttk.Label(
            header_frame,
            text=desc_text,
            style='Subtitle.TLabel',
            justify=tk.CENTER
        )
        desc_label.grid(row=1, column=0)
        
        # File selection card
        file_card = ttk.LabelFrame(main_frame, text="📁  Select Font Archives", padding=15)
        file_card.grid(row=1, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        file_card.columnconfigure(0, weight=1)
        file_card.rowconfigure(1, weight=1)
        
        # Select button with modern styling
        select_button_frame = ttk.Frame(file_card)
        select_button_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        select_button_frame.columnconfigure(0, weight=1)
        
        self.select_btn = ttk.Button(
            select_button_frame,
            text="Select ZIP Files",
            command=self.select_files,
            style='Primary.TButton'
        )
        self.select_btn.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        # Modern file list
        listbox_frame = ttk.Frame(file_card)
        listbox_frame.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        listbox_frame.columnconfigure(0, weight=1)
        listbox_frame.rowconfigure(0, weight=1)
        
        # Create a modern-looking listbox with comfortable height
        self.files_listbox = tk.Listbox(
            listbox_frame,
            height=5,
            font=('Segoe UI', 12),
            selectmode=tk.EXTENDED,
            bg=self.colors['surface'],
            fg=self.colors['text'],
            selectbackground=self.colors['primary'],
            selectforeground='white',
            relief='solid',
            borderwidth=1,
            highlightthickness=0
        )
        self.files_listbox.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        # Modern scrollbar
        scrollbar = ttk.Scrollbar(listbox_frame, orient=tk.VERTICAL, command=self.files_listbox.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.files_listbox.configure(yscrollcommand=scrollbar.set)
        
        # Clear button (icon only)
        self.clear_btn = ttk.Button(
            file_card,
            text="✕",
            command=self.clear_files,
            state=tk.DISABLED,
            style='Icon.TButton',
            width=3
        )
        self.clear_btn.grid(row=2, column=0, sticky=(tk.W))
        
        # Progress card
        progress_card = ttk.LabelFrame(main_frame, text="Installation Progress", padding=15)
        progress_card.grid(row=2, column=0, sticky=(tk.W, tk.E), pady=(0, 15))
        progress_card.columnconfigure(0, weight=1)
        
        # Modern progress bar
        self.progress = ttk.Progressbar(
            progress_card,
            mode='indeterminate',
            length=500,
            style='Modern.Horizontal.TProgressbar'
        )
        self.progress.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Status label with icon
        self.status_label = ttk.Label(
            progress_card,
            text="Select ZIP files to begin",
            style='Status.TLabel'
        )
        self.status_label.grid(row=1, column=0, sticky=(tk.W))
        
        # Install button (centered, compact spacing)
        self.install_btn = ttk.Button(
            main_frame,
            text="Install Fonts",
            command=self.install_fonts,
            state=tk.DISABLED,
            style='Success.TButton'
        )
        self.install_btn.grid(row=3, column=0, sticky=(tk.W, tk.E), pady=(10, 0))
        
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
        """Update button states and status message based on selected files."""
        has_files = len(self.selected_files) > 0
        self.install_btn.config(state=tk.NORMAL if has_files else tk.DISABLED)
        self.clear_btn.config(state=tk.NORMAL if has_files else tk.DISABLED)
        
        # Update status message based on selection
        if has_files:
            file_count = len(self.selected_files)
            file_text = "file" if file_count == 1 else "files"
            self.status_label.config(text=f"Ready to install fonts from {file_count} {file_text}")
        else:
            self.status_label.config(text="Select ZIP files to begin")
        
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
        """Install a single font file using Windows API with proper registry registration."""
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
                # Register in system registry for persistence across reboots
                try:
                    with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, 
                                      r"SOFTWARE\Microsoft\Windows NT\CurrentVersion\Fonts", 
                                      0, winreg.KEY_SET_VALUE) as key:
                        # Create registry entry with font name and file
                        font_reg_name = self.get_font_name_from_file(font_path)
                        winreg.SetValueEx(key, font_reg_name, 0, winreg.REG_SZ, font_filename)
                except Exception as reg_error:
                    print(f"Registry registration failed for {font_filename}: {str(reg_error)}")
                    # Continue anyway - font is still loaded temporarily
                
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
            print(f"System installation failed for {font_filename}: Administrator privileges are required.")
            return
        except Exception as e:
            print(f"System installation failed for {font_filename}: {str(e)}")
        
        return False, "unknown error"
        
    def get_font_name_from_file(self, font_path: str) -> str:
        """Extract the actual font name from the font file for better registry registration."""
        try:
            # Try to read font name from the file itself
            # This is a simplified approach - for more complex font name extraction,
            # you would need a font parsing library like fonttools
            font_filename = os.path.basename(font_path)
            font_name_base = os.path.splitext(font_filename)[0]
            
            # Clean up common font filename patterns
            font_name_base = font_name_base.replace('_', ' ').replace('-', ' ')
            
            # Determine font type and create proper registry name
            ext = os.path.splitext(font_filename)[1].lower()
            if ext == '.ttf':
                return f"{font_name_base} (TrueType)"
            elif ext == '.otf':
                return f"{font_name_base} (OpenType)"
            elif ext in ['.ttc', '.otc']:
                return f"{font_name_base} (TrueType Collection)" if ext == '.ttc' else f"{font_name_base} (OpenType Collection)"
            else:
                return f"{font_name_base} (TrueType)"  # Default fallback
                
        except Exception:
            # Fallback to simple naming
            font_name_base = os.path.splitext(os.path.basename(font_path))[0]
            return f"{font_name_base} (TrueType)"
            
    def install_fonts_thread(self):
        """Install fonts in a separate thread to prevent GUI freezing."""
        installed_count = 0
        total_fonts = 0
        system_installs = 0
        user_installs = 0
        failed_installs = []
        
        # Update status with modern icons
        self.root.after(0, lambda: self.status_label.config(text="📦  Extracting fonts from archives..."))
        self.root.after(0, self.progress.start)
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                all_font_files = []
                
                # Extract all fonts from ZIP files
                for zip_path in self.selected_files:
                    self.root.after(0, lambda z=zip_path: self.status_label.config(
                        text=f"📂  Extracting: {os.path.basename(z)}"
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
                self.root.after(0, lambda: self.status_label.config(text="⚡  Installing fonts..."))
                
                for i, font_path in enumerate(all_font_files):
                    font_name = os.path.basename(font_path)
                    self.root.after(0, lambda fn=font_name, prog=i+1, tot=total_fonts: self.status_label.config(
                        text=f"🔧  Installing ({prog}/{tot}): {fn}"
                    ))
                    
                    success, install_type = self.install_font_file(font_path)
                    if success:
                        installed_count += 1
                        if install_type == "system-wide":
                            system_installs += 1
                        elif "user-level" in install_type:  # Handles all user-level variants
                            user_installs += 1
                    else:
                        failed_installs.append((font_name, install_type))
                        
        except Exception as e:
            self.root.after(0, lambda: messagebox.showerror(
                "Installation Error",
                f"An error occurred during installation: {str(e)}"
            ))
        finally:
            # Update UI in main thread with modern status
            self.root.after(0, self.progress.stop)
            
            if installed_count > 0:
                self.root.after(0, lambda: self.status_label.config(
                    text=f"✅  Complete: {installed_count}/{total_fonts} fonts installed successfully"
                ))
            else:
                self.root.after(0, lambda: self.status_label.config(
                    text=f"❌  Failed: No fonts were installed"
                ))
            
            # Prepare detailed completion message with modern formatting
            if installed_count > 0:
                message_parts = [f"Successfully installed {installed_count} out of {total_fonts} fonts"]
                
                if system_installs > 0:
                    message_parts.append(f"\n{system_installs} fonts installed system-wide")
                
                if user_installs > 0:
                    message_parts.append(f"\n{user_installs} fonts installed for current user")
                    
                if failed_installs:
                    message_parts.append(f"\n{len(failed_installs)} fonts failed to install")
                    
                message_parts.append("\nThe fonts are now available in your applications")
                
                self.root.after(0, lambda: messagebox.showinfo(
                    "Installation Complete",
                    "\n".join(message_parts)
                ))
            else:
                self.root.after(0, lambda: messagebox.showerror(
                    "Installation Failed",
                    "No fonts were installed.\n\nPlease try running as Administrator."
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

    def setup_modern_style(self):
        """Configure modern dark theme ttk styles."""
        style = ttk.Style()
        
        # Use a modern theme as base
        try:
            style.theme_use('clam')   # Clam theme works better for dark themes
        except:
            style.theme_use('default')  # Ultimate fallback
        
        # Configure dark theme colors
        style.configure('.',
                       background=self.colors['bg'],
                       foreground=self.colors['text'],
                       bordercolor=self.colors['border'],
                       darkcolor=self.colors['surface'],
                       lightcolor=self.colors['surface'],
                       troughcolor=self.colors['surface'],
                       focuscolor='none',
                       selectbackground=self.colors['primary'],
                       selectforeground='white')
        
        # Configure modern button styles with rounded appearance
        style.configure('Modern.TButton',
                       font=('Segoe UI', 12),
                       padding=(20, 12),
                       background=self.colors['surface'],
                       foreground=self.colors['text'],
                       borderwidth=0,
                       relief='flat',
                       focuscolor='none')
        
        style.map('Modern.TButton',
                 background=[('active', self.colors['secondary']),
                           ('pressed', self.colors['border'])],
                 foreground=[('active', self.colors['text']),
                           ('pressed', self.colors['text'])],
                 relief=[('pressed', 'sunken'),
                        ('active', 'flat')])
        
        style.configure('Primary.TButton',
                       font=('Segoe UI', 13, 'bold'),
                       padding=(25, 15),
                       background=self.colors['primary'],
                       foreground='white',
                       borderwidth=0,
                       relief='flat',
                       focuscolor='none')
        
        style.map('Primary.TButton',
                 background=[('active', self.colors['primary_hover']),
                           ('pressed', self.colors['primary_hover']),
                           ('disabled', self.colors['border'])],
                 foreground=[('disabled', self.colors['text_muted'])],
                 relief=[('pressed', 'sunken'),
                        ('active', 'flat')])
        
        style.configure('Secondary.TButton',
                       font=('Segoe UI', 12),
                       padding=(18, 12),
                       background=self.colors['secondary'],
                       foreground=self.colors['text'],
                       borderwidth=0,
                       relief='flat',
                       focuscolor='none')
        
        style.map('Secondary.TButton',
                 background=[('active', self.colors['border']),
                           ('pressed', self.colors['border']),
                           ('disabled', self.colors['surface'])],
                 foreground=[('active', self.colors['text']),
                           ('pressed', self.colors['text']),
                           ('disabled', self.colors['text_muted'])],
                 relief=[('pressed', 'sunken'),
                        ('active', 'flat')])
        
        # Configure icon button style (small, minimal)
        style.configure('Icon.TButton',
                       font=('Segoe UI', 11),
                       padding=(8, 8),
                       background=self.colors['surface'],
                       foreground=self.colors['text_muted'],
                       borderwidth=0,
                       relief='flat',
                       focuscolor='none')
        
        style.map('Icon.TButton',
                 background=[('active', self.colors['danger']),
                           ('pressed', self.colors['danger']),
                           ('disabled', self.colors['surface'])],
                 foreground=[('active', 'white'),
                           ('pressed', 'white'),
                           ('disabled', self.colors['border'])],
                 relief=[('pressed', 'sunken'),
                        ('active', 'flat')])
        
        # Configure success button style (green)
        style.configure('Success.TButton',
                       font=('Segoe UI', 13, 'bold'),
                       padding=(25, 15),
                       background=self.colors['success'],
                       foreground='white',
                       borderwidth=0,
                       relief='flat',
                       focuscolor='none')
        
        style.map('Success.TButton',
                 background=[('active', '#1e7e34'),  # Darker green on hover
                           ('pressed', '#1e7e34'),
                           ('disabled', self.colors['border'])],
                 foreground=[('disabled', self.colors['text_muted'])],
                 relief=[('pressed', 'sunken'),
                        ('active', 'flat')])
        
        # Configure label styles
        style.configure('Title.TLabel',
                       font=('Segoe UI', 26, 'bold'),
                       background=self.colors['bg'],
                       foreground=self.colors['text'])
        
        style.configure('Subtitle.TLabel',
                       font=('Segoe UI', 13),
                       background=self.colors['bg'],
                       foreground=self.colors['text_muted'])
        
        style.configure('Status.TLabel',
                       font=('Segoe UI', 13, 'bold'),
                       foreground=self.colors['text'])
        
        # Configure frame styles
        style.configure('TFrame',
                       background=self.colors['bg'],
                       borderwidth=0)
        
        style.configure('TLabelFrame',
                       background=self.colors['bg'],
                       foreground=self.colors['text'],
                       borderwidth=1,
                       relief='solid')
        
        style.configure('TLabelFrame.Label',
                       background=self.colors['bg'],
                       foreground=self.colors['text'],
                       font=('Segoe UI', 11, 'bold'))
        
        style.configure('Card.TLabelFrame',
                       padding=20,
                       background=self.colors['surface'],
                       borderwidth=1,
                       relief='solid')
        
        style.configure('Card.TLabelFrame.Label',
                       font=('Segoe UI', 11, 'bold'),
                       background=self.colors['surface'],
                       foreground=self.colors['text'])
        
        # Configure progress bar
        style.configure('Modern.Horizontal.TProgressbar',
                       borderwidth=0,
                       background=self.colors['primary'],
                       troughcolor=self.colors['surface'])
        
        # Configure scrollbar with comprehensive dark theme styling
        style.configure('Vertical.TScrollbar',
                       background=self.colors['surface'],
                       troughcolor=self.colors['bg'],
                       borderwidth=0,
                       arrowcolor=self.colors['text'],
                       darkcolor=self.colors['border'],
                       lightcolor=self.colors['surface'],
                       gripcolor=self.colors['secondary'])
        
        style.map('Vertical.TScrollbar',
                 background=[('active', self.colors['secondary']),
                           ('pressed', self.colors['border'])],
                 arrowcolor=[('active', self.colors['text']),
                           ('pressed', self.colors['text'])])

    def check_user_font_directory(self):
        """Check and prepare user font directories."""
        possible_dirs = [
            os.path.join(os.path.expanduser('~'), 'AppData', 'Local', 'Microsoft', 'Windows', 'Fonts'),
            os.path.join(os.path.expanduser('~'), 'Documents', 'Fonts'),
        ]
        
        for directory in possible_dirs:
            try:
                os.makedirs(directory, exist_ok=True)
                # Test write permissions
                test_file = os.path.join(directory, '.test_write')
                with open(test_file, 'w') as f:
                    f.write('test')
                os.remove(test_file)
                return directory
            except:
                continue
        return None

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

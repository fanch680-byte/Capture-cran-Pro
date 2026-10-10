#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
📸 CAPTURE ÉCRAN PRO - 2026
Logiciel de capture d'écran avec CustomTkinter
"""

import customtkinter as ctk
import subprocess
import os
from datetime import datetime
import pyautogui
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class CaptureEcranPro(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("📸 Capture Écran Pro")
        self.geometry("600x760+450+05")
        self.minsize(450, 600)
        self.capture_folder = r"C:\Users\fanch\Pictures\Captures"
        self.capture_format = "PNG"
        self.capture_count = 0
        if not os.path.exists(self.capture_folder):
            os.makedirs(self.capture_folder)
        self.creer_interface()
        self.bind("<F9>", lambda e: self.capture_plein_ecran())
        self.bind("<F10>", lambda e: self.capture_zone_personnalisee())

    def creer_interface(self):
        titre_frame = ctk.CTkFrame(self)
        titre_frame.pack(fill="x", padx=20, pady=20)
        ctk.CTkLabel(titre_frame, text="📸 CAPTURE ÉCRAN PRO",
                     font=ctk.CTkFont(size=24, weight="bold")).pack(pady=10)
        ctk.CTkLabel(titre_frame, text="2026 - Python + CustomTkinter",
                     font=ctk.CTkFont(size=14), text_color="#2196F3").pack()
        modes_frame = ctk.CTkFrame(self)
        modes_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(modes_frame, text="🎯 Modes de capture :",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        ctk.CTkButton(modes_frame, text="🖥️ Plein écran (F9)",
                      command=self.capture_plein_ecran, height=45,
                      font=ctk.CTkFont(size=14), fg_color="#2196F3",
                      hover_color="#1976D2").pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(modes_frame, text="📏 Zone personnalisée (F10)",
                      command=self.capture_zone_personnalisee, height=45,
                      font=ctk.CTkFont(size=14), fg_color="#4CAF50",
                      hover_color="#388E3C").pack(fill="x", padx=20, pady=5)
        ctk.CTkButton(modes_frame, text="🪟 Zone Windows",
                      command=self.capture_zone_windows, height=45,
                      font=ctk.CTkFont(size=14), fg_color="#FF9800",
                      hover_color="#F57C00").pack(fill="x", padx=20, pady=5)
        params_frame = ctk.CTkFrame(self)
        params_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(params_frame, text="⚙️ Paramètres :",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        dossier_frame = ctk.CTkFrame(params_frame)
        dossier_frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(dossier_frame, text="📁 Dossier :",
                     font=ctk.CTkFont(size=12)).pack(side="left", padx=10)
        self.dossier_label = ctk.CTkLabel(dossier_frame,
                                          text=self.capture_folder,
                                          font=ctk.CTkFont(size=10),
                                          text_color="gray", wraplength=250)
        self.dossier_label.pack(side="left", padx=10)
        ctk.CTkButton(dossier_frame, text="Changer",
                      command=self.changer_dossier,
                      width=80, height=30).pack(side="right", padx=10)
        format_frame = ctk.CTkFrame(params_frame)
        format_frame.pack(fill="x", padx=20, pady=5)
        ctk.CTkLabel(format_frame, text="📄 Format :",
                     font=ctk.CTkFont(size=12)).pack(side="left", padx=10)
        self.format_var = ctk.StringVar(value="PNG")
        format_menu = ctk.CTkOptionMenu(format_frame,
                                        values=["PNG", "JPG", "BMP"],
                                        variable=self.format_var,
                                        command=self.changer_format,
                                        width=100)
        format_menu.pack(side="left", padx=10)
        stats_frame = ctk.CTkFrame(self)
        stats_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(stats_frame, text="📊 Statistiques :",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=10)
        self.stats_label = ctk.CTkLabel(stats_frame,
                                        text="Captures réalisées : 0",
                                        font=ctk.CTkFont(size=12))
        self.stats_label.pack(pady=5)
        ctk.CTkButton(self, text="📁 Ouvrir le dossier",
                      command=self.ouvrir_dossier, height=35,
                      fg_color="#9C27B0",
                      hover_color="#7B1FA2").pack(pady=10)
        raccourcis_frame = ctk.CTkFrame(self)
        raccourcis_frame.pack(fill="x", padx=20, pady=10)
        ctk.CTkLabel(raccourcis_frame, text="⌨️ Raccourcis clavier :",
                     font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)
        ctk.CTkLabel(raccourcis_frame,
                     text="F9 → Plein écran  |  F10 → Zone personnalisée",
                     font=ctk.CTkFont(size=13), text_color="#2196F3").pack(pady=5)

    def capture_plein_ecran(self):
        try:
            self.iconify()
            self.after(500, self._prendre_capture_plein_ecran)
        except Exception as e:
            self.deiconify()
            messagebox.showerror("Erreur", f"Erreur capture : {e}")

    def _prendre_capture_plein_ecran(self):
        try:
            screenshot = pyautogui.screenshot()
            date_heure = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"Capture_{date_heure}.{self.capture_format.lower()}"
            chemin_complet = os.path.join(self.capture_folder, nom_fichier)
            if self.capture_format == "JPG":
                screenshot.save(chemin_complet, quality=95)
            else:
                screenshot.save(chemin_complet)
            self.deiconify()
            self.capture_count += 1
            self.stats_label.configure(
                text=f"Captures réalisées : {self.capture_count}")
            messagebox.showinfo("✅ Capture réussie !",
                                f"Enregistré dans :\n{chemin_complet}")
        except Exception as e:
            self.deiconify()
            messagebox.showerror("Erreur", f"Erreur : {e}")

    def capture_zone_personnalisee(self):
        try:
            self.iconify()
            overlay = ctk.CTkToplevel(self)
            overlay.title("Sélectionnez la zone")
            overlay.attributes("-fullscreen", True)
            overlay.attributes("-alpha", 0.3)
            overlay.attributes("-topmost", True)
            overlay.configure(fg_color="black")
            canvas = ctk.CTkCanvas(overlay, bg="black",
                                   highlightthickness=0, cursor="crosshair")
            canvas.pack(fill="both", expand=True)
            rect = None
            start_x = None
            start_y = None

            def on_mouse_press(event):
                nonlocal start_x, start_y, rect
                start_x = event.x
                start_y = event.y
                rect = canvas.create_rectangle(start_x, start_y,
                                               start_x, start_y,
                                               outline="#00FF00", width=3)

            def on_mouse_drag(event):
                nonlocal rect
                if rect:
                    canvas.coords(rect, start_x, start_y, event.x, event.y)

            def on_mouse_release(event):
                nonlocal start_x, start_y
                if start_x and start_y:
                    x1 = min(start_x, event.x)
                    y1 = min(start_y, event.y)
                    x2 = max(start_x, event.x)
                    y2 = max(start_y, event.y)
                    overlay.destroy()
                    self.apres_selection_zone(x1, y1, x2, y2)

            canvas.bind("<ButtonPress-1>", on_mouse_press)
            canvas.bind("<B1-Motion>", on_mouse_drag)
            canvas.bind("<ButtonRelease-1>", on_mouse_release)
            canvas.create_text(overlay.winfo_screenwidth() // 2, 100,
                               text="📏 Cliquez et glissez pour sélectionner",
                               fill="white", font=("Arial", 20, "bold"))
            overlay.bind("<Escape>", lambda e: overlay.destroy())
        except Exception as e:
            self.deiconify()
            messagebox.showerror("Erreur", f"Erreur capture zone : {e}")

    def apres_selection_zone(self, x1, y1, x2, y2):
        self.after(500, lambda: self._prendre_capture_zone(x1, y1, x2, y2))

    def _prendre_capture_zone(self, x1, y1, x2, y2):
        try:
            screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))
            date_heure = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"Zone_{date_heure}.{self.capture_format.lower()}"
            chemin_complet = os.path.join(self.capture_folder, nom_fichier)
            if self.capture_format == "JPG":
                screenshot.save(chemin_complet, quality=95)
            else:
                screenshot.save(chemin_complet)
            self.deiconify()
            self.capture_count += 1
            self.stats_label.configure(
                text=f"Captures réalisées : {self.capture_count}")
            messagebox.showinfo("✅ Capture de zone réussie !",
                                f"Zone : {x2-x1}x{y2-y1} pixels\n\n"
                                f"Enregistré dans :\n{chemin_complet}")
        except Exception as e:
            self.deiconify()
            messagebox.showerror("Erreur", f"Erreur : {e}")

    def capture_zone_windows(self):
        """Ouvre l'outil de capture Windows"""
        try:
            messagebox.showinfo(
                "📏 Capture Windows",
                "📸 L'outil va s'ouvrir...\n\n"
                "Sélectionne ta zone avec la souris"
            )
            self.iconify()
            try:
                os.startfile("ms-screenclip:")
            except Exception:
                try:
                    subprocess.Popen(r"C:\Windows\System32\SnippingTool.exe")
                except Exception:
                    subprocess.Popen(
                        "powershell -command \"Add-Type -AssemblyName System.Windows.Forms; "
                        "[System.Windows.Forms.SendKeys]::SendWait('^{+}s')\"",
                        shell=True
                    )
            self.after(3000, self.deiconify)
        except Exception as e:
            self.deiconify()
            messagebox.showerror("Erreur", f"Erreur : {e}")

    def changer_dossier(self):
        nouveau_dossier = filedialog.askdirectory(
            title="Choisir le dossier de captures",
            initialdir=self.capture_folder)
        if nouveau_dossier:
            self.capture_folder = nouveau_dossier
            self.dossier_label.configure(text=self.capture_folder)
            if not os.path.exists(self.capture_folder):
                os.makedirs(self.capture_folder)
            messagebox.showinfo("✅ Dossier modifié !",
                                f"Nouveau dossier :\n{self.capture_folder}")

    def changer_format(self, choix):
        self.capture_format = choix
        messagebox.showinfo("📄 Format modifié !", f"Format : {choix}")

    def ouvrir_dossier(self):
        if not os.path.exists(self.capture_folder):
            os.makedirs(self.capture_folder)
        subprocess.Popen(f'explorer.exe "{self.capture_folder}"', shell=True)


if __name__ == "__main__":
    app = CaptureEcranPro()
    app.mainloop()
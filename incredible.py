import sublime
import sublime_plugin
import os

class RunPythonCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # Enregistrer le fichier avant de continuer
        self.view.run_command("save")

        # Récupérer le code sélectionné
        current_file = self.view.file_name()
        if current_file:
            error_count = self.compter_erreurs(current_file)
            sublime.message_dialog("Nombre d'erreurs : {}".format(error_count))
            self.afficher_image_erreur(error_count)
        else:
            sublime.message_dialog("Aucun fichier ouvert.")

    def compter_erreurs(self, current_file):
        error_count = 0
        with open(current_file, 'r') as file:
            # Lecture du contenu du fichier ligne par ligne
            for num_ligne, ligne in enumerate(file, start=1):
                try:
                    # Exécuter la ligne
                    exec(ligne)
                except Exception as e:
                    # Incrémenter le compteur si une erreur est levée
                    error_count += 1
                    print("Erreur à la ligne {}: {}".format(num_ligne, e))
        return error_count

    def afficher_image_erreur(self, error_count):
        if error_count == 0:
            os.system("feh ~/plugin/0.jpeg")
        elif 1 <= error_count <= 2:
            os.system("feh ~/plugin/1.png")
        elif 2 < error_count <= 4:
            os.system("feh ~/plugin/2.png")
        elif 4 < error_count <= 6:
            os.system("feh ~/plugin/3.png")
        else:
            os.system("feh ~/plugin/4.webp")
import gradio as gr
import navigium as navigium
import os
import extract_from_word as ex
import time


def main(input, filename="Vokabelliste.xlsx", export2by=False, anzahl_threads=20, progress=gr.Progress()):
    start_time = time.time()
    progress(0, desc="Starting...")
    if type(input) is str:
        text = input
        text = text.split("\n")
        words = navigium.split_into_words(text)
    elif type(input) is list:
        words = []
        tmp_names = []
        for file in input:
            if os.path.splitext(file)[1] == ".docx":
                tmp_names.append(os.path.splitext(os.path.basename(file))[0])
                words.extend(ex.extract_highlighted_words(file))
        if filename == "":
            filename = "_UND_".join(tmp_names)
    else:
        return

    progress(0.05, desc="Prepared...")

    progress(0.1, desc="Request to Navigium...")
    output = navigium.threaded_function(words, anzahl_threads=anzahl_threads)
    progress(0.61, desc="Sort and analyse...")
    sorted = navigium.sort_by_wordtype(output)
    vocabulary = navigium.advanced_formating(sorted)
    progress(0.83, desc="Exporting...")
    if filename == "":
        filepath_excel = "Vokabelliste.xlsx"
        filepath_by2 = "Vokabelliste.by2"
    elif filename.endswith(".xlsx"):
        filepath_by2 = f"{os.path.splitext(os.path.basename(filename))[0]}.by2"
    elif not filename.endswith(".xlsx"):
        filepath_excel = f"{filename}.xlsx"
        filepath_by2 = f"{filename}.by2"
    excel = navigium.save2excel(filepath_excel, vocabulary)
    if export2by == True:
        navigium.save2by2(excel, filepath_by2)
        progress(1, desc="Finished...")
        return [filepath_excel, filepath_by2]
    progress(1, desc="Finished...")
    end_time = time.time()
    duration = end_time - start_time
    print(f"Der Code hat {duration:.5f} Sekunden benötigt.")
    return [filepath_excel]

# Erstelle das Gradio Blocks Interface
with gr.Blocks(css="footer{display:none !important}") as demo:
    # Tabs für die Alternative zwischen Texteingabe und Datei-Upload
    gr.HTML("<h1 style='text-align: center;'>Vokabellisten Generator</h1>")
    gr.HTML("<p style='text-align: center;'>Einfach aus lateinischen Texten Vokabellisten generieren</p>")
    gr.HTML("<p style='text-align: center; color: red;'>!!!Achtung!!! Dies ist eine Beta-Version und unterstützt aktuell nur Nomen, Verben und Adjektive</p>")
    with gr.Tabs():
        with gr.TabItem("Texteingabe"):
            gr.HTML("<p style='text-align: left;'>Gib deinen lateinischen Text ein und lade dir anschließend die generierte Excel-Datei und optional auch die Brainyoo-Datei herunter.</p>")
            with gr.Row():
                with gr.Column():
                    name = gr.Textbox(placeholder="Gib den gewünschten Dateiname hier ein (Default: \"Vokabelliste.xlsx\")...", label="Dateiname(optional):", lines=1, max_lines=1)
                    textbox = gr.Textbox(placeholder="Gib deinen lateinischen Text hier ein...", label="Lateinischer Text:", lines=10, max_lines=10)
                    #box = gr.Checkbox(label="Convert Excel to PDF (kann bis zu 5min länger dauern)", value=False)
                    export2by2 = gr.Checkbox(label="Export nach Brainyoo (als .by2 Datei)", value=False)
                    slider = gr.Slider(minimum=1, maximum=128, value=20, label="Verändere die Anzahl an Threads. (Beeinflusst direkt die Geschwindigkeit)")
                    submit_btn = gr.Button("Absenden")
                with gr.Column():    
                    result_box = gr.Files(label="Download Excel-Datei und ggf. deine Brainyoo-Datei")
                    submit_btn.click(fn=main, inputs=[textbox, name, export2by2, slider], outputs=result_box)
        
        with gr.TabItem("Datei-Upload (.docx)"):
            gr.HTML("<p style='text-align: left;'>Lade eine Word-Datei hoch und lade dir anschließend die generierte Excel-Datei und optional auch die Brainyoo-Datei herunter.</p>")
            with gr.Row():
                with gr.Column():
                    name = gr.Textbox(placeholder="Gib den gewünschten Dateiname hier ein (Default: Dateiname der Word-Datei)...", label="Dateiname(optional):", lines=1, max_lines=1)
                    docx_file = gr.File(file_count="multiple", label="Lade eine Word-Datei hoch, welche in roter Textfarbe oder mit einem beliebigen Textmarker markierte Wörter enthält")
                    #box = gr.Checkbox(label="Convert Excel to PDF (kann bis zu 5min länger dauern)", value=False)
                    export2by2 = gr.Checkbox(label="Export nach Brainyoo (als .by2 Datei)", value=False)
                    slider = gr.Slider(minimum=1, maximum=128, value=20, label="Verändere die Anzahl an Threads. (Beeinflusst direkt die Geschwindigkeit)")
                    submit_btn = gr.Button("Absenden")
                with gr.Column():    
                    result_box = gr.Files(label="Download Excel-Datei und ggf. deine Brainyoo-Datei")
                    submit_btn.click(fn=main, inputs=[docx_file, name, export2by2, slider], outputs=result_box)
    #gr.Markdown("<hr>")
    gr.HTML(f"<a href='https://brainyoo.de/dokumentation/xml-die-browser-version/der-xml-reimport/'> Brainyoo Datei-Import Anleitung</a>")
    gr.HTML(f"<a href='https://github.com/BenniBoy602/Vokabellisten-Generator_Latein'> GitHub</a>")
    gr.HTML("<hr>")
    gr.HTML("<p style='text-align: center;'>Programmiert von: <a href='https://github.com/BenniBoy602'> Rostbraten</a></p>")
    link = "https://www.navigium.de/suchfunktion/_search?q={}"
    gr.HTML(f"<p style='text-align: center;'>Nutzt <a href={link}> {link}</a> als Wörterbuch</p>")


# Starte die Gradio App
demo.launch()
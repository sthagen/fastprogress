# AUTOGENERATED! DO NOT EDIT! File to edit: dev/00_core.ipynb (unless otherwise specified).

__all__ = ['format_time', 'html_progress_bar', 'text2html_table', 'in_colab', 'IN_COLAB', 'in_notebook', 'IN_NOTEBOOK']

# Cell
def format_time(t):
    "Format `t` (in seconds) to (h):mm:ss"
    t = int(t)
    h,m,s = t//3600, (t//60)%60, t%60
    if h!= 0: return f'{h}:{m:02d}:{s:02d}'
    else:     return f'{m:02d}:{s:02d}'

# Cell
def html_progress_bar(value, total, label, interrupted=False):
    "Html code for a progress bar `value`/`total` with `label`"
    bar_style = 'progress-bar-interrupted' if interrupted else ''
    return f"""
    <div>
        <style>
            /* Turns off some styling */
            progress {{
                /* gets rid of default border in Firefox and Opera. */
                border: none;
                /* Needs to be in here for Safari polyfill so background images work as expected. */
                background-size: auto;
            }}
            .progress-bar-interrupted, .progress-bar-interrupted::-webkit-progress-bar {{
                background: #F44336;
            }}
        </style>
      <progress value='{value}' class='{bar_style}' max='{total}', style='width:300px; height:20px; vertical-align: middle;'></progress>
      {label}
    </div>
    """

# Cell
def text2html_table(items):
    "Put the texts in `items` in an HTML table."
    html_code = f"""<table border="1" class="dataframe">\n"""
    html_code += f"""  <thead>\n    <tr style="text-align: left;">\n"""
    for i in items[0]: html_code += f"      <th>{i}</th>\n"
    html_code += f"    </tr>\n  </thead>\n  <tbody>\n"
    for line in items[1:]:
        html_code += "    <tr>\n"
        for i in line: html_code += f"      <td>{i}</td>\n"
        html_code += "    </tr>\n"
    html_code += "  </tbody>\n</table><p>"
    return html_code

# Cell
def in_colab():
    "Check if the code is running in Google Colaboratory"
    try:
        from google import colab
        return True
    except: return False

IN_COLAB = in_colab()

# Cell
def in_notebook():
    "Check if the code is running in a jupyter notebook"
    if in_colab(): return True
    try:
        shell = get_ipython().__class__.__name__
        if shell == 'ZMQInteractiveShell': # Jupyter notebook, Spyder or qtconsole
            import IPython
            #IPython version lower then 6.0.0 don't work with output you update
            return IPython.__version__ >= '6.0.0'
        elif shell == 'TerminalInteractiveShell': return False  # Terminal running IPython
        else: return False  # Other type (?)
    except NameError: return False      # Probably standard Python interpreter

IN_NOTEBOOK = in_notebook()
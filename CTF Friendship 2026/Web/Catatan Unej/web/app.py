from flask import Flask, request, redirect, url_for, render_template_string, render_template,Markup, session
import uuid
import re
import os
import time

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.url_map.merge_slashes = False 

notes = {
    "sample_id": {"icon": "📢", "content": "Selamat datang di Dashboard Mahasiswa.", "created_at": time.time()}
}

@app.before_request
def security_filter():
    if re.match(r"^/note", request.path):
        return render_template('error/404.html'), 403

@app.route('/')
def index():
    if os.path.exists('unej.html'):
        with open('unej.html', 'r') as f:
            return f.read()
    return "File unej.html missing."

def render_dashboard():
    notes_html = ""

    for note_id, note in notes.items():
        notes_html += f'<div data-icon="{note["icon"]}">{note["content"]}</div>'
    
    return render_template('dashboard.html', notes=notes_html)

@app.route('/<path:subpath>')
@app.route('/note') 
def handler(subpath=None):
    target = request.path
    if "note" in target:
        notes_html = ""
        current_time = time.time()
        
        for note_id, note in list(notes.items()):
            if 'created_at' in note:
                if current_time - note['created_at'] > 60: 
                    del notes[note_id]
                    continue
            
            html_part = f'<div data-icon="{note["icon"]}">{note["content"]}</div>'
            notes_html += html_part
        
        return render_template('dashboard.html', notes=Markup(notes_html))
    return redirect(url_for('index'))

@app.route('/api/submit', methods=['POST'])
def submit():
    content = request.form.get('content', '')
    icon = request.form.get('icon', '📝')

    note_id = str(uuid.uuid4())
    notes[note_id] = {"icon": icon, "content": content, "created_at": time.time()}
    return redirect('/?msg=NoteCreated')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
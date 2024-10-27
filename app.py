from fileinput import filename
from logic import everything_function
from flask import Flask, request, render_template, send_file, after_this_request
import os  

app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   

def success():   
    if request.method == 'POST':
        f = request.files['file']
        
        # Check if the uploaded file is a .docx file
        if not (f.filename.endswith('.docx') or f.filename.endswith('.doc')):
            return "Error: Please upload a .docx or .doc file.", 400  # Return an error response
        
        # Save the uploaded file
        f.save(f.filename)
        
        # Process the file
        everything_function(f.filename)
        
        output_file = 'draft-chronology.docx'
        
        @after_this_request
        def remove_output_file(response):
            try:
                os.remove(output_file)
                print(f"Removed {output_file}")
            except Exception as error:
                print(f"Error removing {output_file}: {error}")
            return response

        return send_file(output_file, download_name='draft-chronology.docx', as_attachment=True)

if __name__ == '__main__':   
    app.run(debug=True)
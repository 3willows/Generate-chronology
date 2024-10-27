from fileinput import filename
from logic import everything_function
from flask import Flask, request, render_template, send_file, after_this_request
import os  

app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/convert', methods = ['POST'])   

def success():   
    if request.method == 'POST':
        f = request.files['file']
        
        # Check if the uploaded file is a .docx file
        if not f.filename.endswith('.docx'):
            return render_template("error.html", message="Error: Please upload a .docx file. .doc files are not supported; please convert to .docx within Word.", 
                link_url="https://www.youtube.com/watch?v=q4QOMUn8amc", 
                link_text="Click here for conversion instructions"
            ), 400
        
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

@app.route('/word-example')   
def example():   
    return send_file('static/example.docx',
    download_name='example.docx',  as_attachment=True)

if __name__ == '__main__':   
    app.run(debug=True)
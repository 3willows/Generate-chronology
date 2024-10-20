from distutils.log import debug 
from fileinput import filename
from utils import everything_function
from flask import *
import os  

app = Flask(__name__)   
  
@app.route('/')   
def main():   
    return render_template("index.html")   
  
@app.route('/success', methods = ['POST'])   
def success():   
    if request.method == 'POST':   
        f = request.files['file'] 
        f.save(f.filename)
        # print(f.filename)
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

        return  send_file(output_file, download_name='draft-chronology.docx', as_attachment=True )

if __name__ == '__main__':   
    app.run(debug=True)
import os
from pathlib import Path

def generate_html_for_models():
    # Define the folder where your .glb files are stored
    models_dir = Path("models")
    
    # Check if the models directory exists
    if not models_dir.exists() or not models_dir.is_dir():
        print(f"Error: The directory '{models_dir}' does not exist.")
        print("Please create it and place your .glb files inside.")
        return

    # The HTML boilerplate using model-viewer
    # Note: Double curly braces {{ }} are used in the CSS so Python's .format() ignores them
    html_template = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{model_name} - NOSTALGEEK</title>
    
    <script type="module" src="https://ajax.googleapis.com/ajax/libs/model-viewer/4.2.0/model-viewer.min.js"></script>
    
    <style>
        body {{
            margin: 0;
            padding: 0;
            width: 100vw;
            height: 100vh;
            background-color: #2c2c2c; /* Dark background to make models pop */
        }}
        model-viewer {{
            width: 100%;
            height: 100%;
        }}
    </style>
</head>
<body>
    <model-viewer 
        src="{model_path}" 
        alt="A 3D model of {model_name}" 
        ar 
        auto-rotate 
        autoplay
        camera-controls 
        shadow-intensity="1">
    </model-viewer>
</body>
</html>"""

    count = 0
    
    # Iterate through all .glb files in the models folder
    for glb_file in models_dir.glob("*.glb"):
        model_name = glb_file.stem
        # Create a relative path for the HTML to reference (e.g., "models/my_model.glb")
        # Forward slashes are used so it works properly in URLs across all operating systems
        model_path = f"{models_dir.name}/{glb_file.name}" 
        html_filename = f"{model_name}.html"
        
        # Inject the variables into the HTML template
        html_content = html_template.format(
            model_name=model_name,
            model_path=model_path
        )
        
        # Write the HTML file to the current directory
        with open(html_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
            
        print(f"Created viewer: {html_filename}")
        count += 1
        
    if count == 0:
        print(f"No .glb files were found inside the '{models_dir}' folder.")
    else:
        print(f"\nSuccess! Generated {count} HTML files.")

if __name__ == "__main__":
    generate_html_for_models()
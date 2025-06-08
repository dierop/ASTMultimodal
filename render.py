import nbformat as nbf

def render_notebook(path):
    """
    Renderiza el cuaderno de Jupyter y elimina la clave 'widgets' del metadata.
    """
    # Cargar el cuaderno
    nb = nbf.read(path, as_version=nbf.NO_CONVERT)
    
    # Eliminar la clave 'widgets' del metadata
    nb.metadata.pop("widgets", None)  # Elimina la clave si existe
    
    # Guardar el cuaderno modificado
    nbf.write(nb, path)

if __name__ == "__main__":
    # Get name of the notebook to render
    import sys
    if len(sys.argv) != 2:
        print("Uso: python render.py <nombre_del_cuaderno.ipynb>")
        sys.exit(1)
    notebook_path = sys.argv[1]
    render_notebook(notebook_path)

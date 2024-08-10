import json
import os

# path to json models
models_file = 'src/data/models.json'

def load_data(file_path: str) -> dict[str, any]:
    """Carrega os dados do arquivo JSON."""
    if not os.path.exists(file_path):
        return {}
    with open(file_path, 'r') as file:
        return json.load(file)

def save_data(data, file_path):
    """Salva os dados no arquivo JSON."""
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def create_species(data, species_name):
    """Cria uma nova espécie no JSON."""
    if species_name not in data:
        data[species_name] = {}
        save_data(data, models_file)
        print(f"Species '{species_name}' created.")
    else:
        print(f"Species '{species_name}' already exists.")

def create_variety(data, species_name, variety_name):
    """Cria uma nova variedade para uma espécie existente."""
    if species_name in data:
        if variety_name not in data[species_name]:
            data[species_name][variety_name] = {}
            save_data(data, models_file)
            print(f"Variety '{variety_name}' added to species '{species_name}'.")
        else:
            print(f"Variety '{variety_name}' already exists in species '{species_name}'.")
    else:
        print(f"Species '{species_name}' does not exist.")

def create_model(data, species_name, variety_name, model_name, model, description, citation):
    """Cria um novo modelo para uma variedade existente."""
    if species_name in data:
        if variety_name in data[species_name]:
            if model_name not in data[species_name][variety_name]:
                data[species_name][variety_name][model_name] = {
                    "model": model,
                    "description": description,
                    "citation": citation
                }
                save_data(data, models_file)
                print(f"Model '{model_name}' added to variety '{variety_name}' of species '{species_name}'.")
            else:
                print(f"Model '{model_name}' already exists in variety '{variety_name}'.")
        else:
            print(f"Variety '{variety_name}' does not exist in species '{species_name}'.")
    else:
        print(f"Species '{species_name}' does not exist.")

def read_data(data):
    """Lê e imprime todos os dados do JSON."""
    for species, varieties in data.items():
        print(f"Species: {species}")
        for variety, models in varieties.items():
            print(f"  Variety: {variety}")
            for model, details in models.items():
                print(f"    Model: {model}")
                print(f"      Formula: {details['model']}")
                print(f"      Description: {details['description']}")
                print(f"      Citation: {details['citation']}")
    print("")

def update_model(data, species_name, variety_name, model_name, new_model=None, new_description=None, new_citation=None):
    """Atualiza um modelo existente."""
    if species_name in data:
        if variety_name in data[species_name]:
            if model_name in data[species_name][variety_name]:
                model_data = data[species_name][variety_name][model_name]
                if new_model is not None:
                    model_data['model'] = new_model
                if new_description is not None:
                    model_data['description'] = new_description
                if new_citation is not None:
                    model_data['citation'] = new_citation
                save_data(data, models_file)
                print(f"Model '{model_name}' in variety '{variety_name}' updated.")
            else:
                print(f"Model '{model_name}' does not exist in variety '{variety_name}'.")
        else:
            print(f"Variety '{variety_name}' does not exist in species '{species_name}'.")
    else:
        print(f"Species '{species_name}' does not exist.")

def delete_model(data, species_name, variety_name, model_name):
    """Remove um modelo existente."""
    if species_name in data:
        if variety_name in data[species_name]:
            if model_name in data[species_name][variety_name]:
                del data[species_name][variety_name][model_name]
                save_data(data, models_file)
                print(f"Model '{model_name}' deleted from variety '{variety_name}'.")
            else:
                print(f"Model '{model_name}' does not exist in variety '{variety_name}'.")
        else:
            print(f"Variety '{variety_name}' does not exist in species '{species_name}'.")
    else:
        print(f"Species '{species_name}' does not exist.")

def delete_variety(data, species_name, variety_name):
    """Remove uma variedade existente."""
    if species_name in data:
        if variety_name in data[species_name]:
            del data[species_name][variety_name]
            save_data(data, models_file)
            print(f"Variety '{variety_name}' deleted from species '{species_name}'.")
        else:
            print(f"Variety '{variety_name}' does not exist in species '{species_name}'.")
    else:
        print(f"Species '{species_name}' does not exist.")

def delete_species(data, species_name):
    """Remove uma espécie existente."""
    if species_name in data:
        del data[species_name]
        save_data(data, models_file)
        print(f"Species '{species_name}' deleted.")
    else:
        print(f"Species '{species_name}' does not exist.")

# Exemplo de uso do script
if __name__ == "__main__":
    # Carregar dados do JSON
    data = load_data(models_file)

    # Exibir dados existentes
    print("Current data:")
    read_data(data)

    # Criar uma nova espécie
    create_species(data, "new species")

    # Criar uma nova variedade
    create_variety(data, "new species", "new variety")

    # Criar um novo modelo
    create_model(
        data,
        "new species",
        "new variety",
        "new model",
        "1.0 * L * W + 1.0",
        "Example model description",
        "New Citation"
    )

    # Atualizar um modelo existente
    update_model(
        data,
        "new species",
        "new variety",
        "new model",
        new_model="1.5 * L * W + 2.0"
    )

    # Exibir dados após adições
    print("Data after additions:")
    read_data(data)

    # Remover um modelo
    delete_model(data, "new species", "new variety", "new model")

    # Remover uma variedade
    delete_variety(data, "new species", "new variety")

    # Remover uma espécie
    delete_species(data, "new species")

    # Exibir dados após remoções
    print("Data after deletions:")
    read_data(data)

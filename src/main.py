from app import select_model_app, result_model_app

if __name__ == "__main__":
    model_input = select_model_app()
    if model_input[-1] is not None:
        result_model_app(model_input)

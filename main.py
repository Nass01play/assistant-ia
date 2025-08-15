import gradio as gr

def assistant(question):
    # Réponse simple pour commencer
    return f"Tu m'as demandé : {question}. Voici ma réponse : je suis encore en apprentissage, mais je vais m'améliorer !"

# Interface utilisateur
gr.Interface(fn=assistant, inputs="text", outputs="text", title="Assistant IA de Nass").launch()
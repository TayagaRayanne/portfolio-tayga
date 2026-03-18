from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    # certificados atuais Hard Skills
    hard_skills = [
        {"titulo": "AWS Code Girls", "escola": "AWS", "arquivo": "aws_code_girls.png"},
        {"titulo": "Copilot Studio", "escola": "Microsoft/Outros", "arquivo": "copilot_studio.png"},
        {"titulo": "Desenvolvimento Orientado a Testes (TDD)", "escola": "DIO", "arquivo": "desenvolvimento_orientado_a_testes.png"},
        {"titulo": "Dotnet Developer", "escola": "DIO", "arquivo": "dotnet_developer.png"},
        {"titulo": "Formação Python Fundamentals", "escola": "DIO", "arquivo": "formacao_python_fundamentals.png"},
        {"titulo": "Gerenciamento de Pacotes e Boas Práticas Python", "escola": "DIO", "arquivo": "gerenciamento_de_pacotes_boas_praticas_python.png"},
        {"titulo": "HTML5 e CSS3", "escola": "Curso em Vídeo", "arquivo": "html5_e_css3.png"},
        {"titulo": "Microserviços com Python e FastAPI", "escola": "DIO", "arquivo": "implementando_microsservicos_com_py_e_fastapi.png"},
        {"titulo": "Jornada Full Stack", "escola": "Hashtag Treinamentos", "arquivo": "jornada_full_stack.png"},
        {"titulo": "Jornada Python", "escola": "Hashtag Treinamentos", "arquivo": "jornada_python.png"},
        {"titulo": "Lógica de Programação DIO", "escola": "DIO", "arquivo": "logica_de_programacao_dio.png"},
        {"titulo": "Lógica de Programação Essencial", "escola": "DIO", "arquivo": "logica_de_programacao_essencial.png"},
        {"titulo": "Consultas Relacionais no SQL Server", "escola": "DIO", "arquivo": "montando_consultas_relacionais_no_sql_server.png"},
        {"titulo": "Python Curso em Vídeo", "escola": "Curso em Vídeo", "arquivo": "python_curso_em_video.png"},
        {"titulo": "Agendamento de Tarefas com Entity Framework", "escola": "DIO", "arquivo": "sistema_de_agendamento_de_tarefas_com_entity_framework.png"},
        {"titulo": "SQL Server: Tabelas e Tipos de Dados", "escola": "DIO", "arquivo": "sql_server_dominando_tabelas_e_tipos_de_dados.png"},
        {"titulo": "SQL Server: Manipulando Dados", "escola": "DIO/Alura", "arquivo": "sql_server_manipulando_dados.png"}
    ]

    # certificados de Soft Skills
    soft_skills = [
        {"titulo": "Pensamento Crítico & Resolução de Problemas", "escola": "Santander Open Academy", "arquivo": "pensamento_critico_e_resolucao_de_problemas.png"},
        {"titulo": "Comunicação Estratégica e Trabalho em Equipe", "escola": "Santander Open Academy", "arquivo": "comunicacao_estrategica_e_trabalho_em_equipe.png"},
        {"titulo": "Inovação e Criatividade", "escola": "Santander Open Academy", "arquivo": "inovacao_e_criatividade.png"},
    ]

    return render_template("index.html", hard_skills=hard_skills, soft_skills=soft_skills)
    # Esse trecho de código define a rota principal ("/") do aplicativo Flask. Ele cria duas listas de dicionários: uma para as hard skills e outra para as soft skills, cada uma contendo o título, a escola e o nome do arquivo da imagem do certificado. Em seguida, ele renderiza o template "index.html", passando as listas de hard skills e soft skills como variáveis para serem usadas no template.

# Essa condição verifica se o script está sendo executado diretamente (em vez de importado como um módulo). Se for o caso, ele inicia o servidor Flask em modo de depuração, permitindo que você veja mensagens de erro detalhadas e recarregue automaticamente o servidor quando fizer alterações no código.
if __name__ == "__main__":
    app.run(debug=True)